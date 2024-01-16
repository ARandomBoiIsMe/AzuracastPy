from datetime import datetime, timedelta

from typing import List, Dict, Any, Optional

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string, get_language_code
from AzuracastPy.util.media_util import get_resource_art
from .util.station_resource_operations import edit_resource, delete_resource

from .podcast_episode import PodcastEpisode

class Links:
    def __init__(
            self_, self: str, episodes: str, public_episodes: str, public_feed: str, art: str,
            episode_new_art: str, episode_new_media: str
        ):
        self_.self = self
        self_.episodes = episodes
        self_.public_episodes = public_episodes
        self_.public_feed = public_feed
        self_.art = art
        self_.episode_new_art = episode_new_art
        self_.episode_new_media = episode_new_media

    def __repr__(self):
        return generate_repr_string(self)

class Podcast:
    def __init__(
        self, id: str, storage_location_id: int, title: str, link: str, description: str, language: str,
        author: str, email: str, has_custom_art: bool, art: str, art_updated_at: int, categories: List[str],
        episodes: List[str], links: Links, _station
    ):
        self.id = id
        self.storage_location_id = storage_location_id
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.author = author
        self.email = email
        self.has_custom_art = has_custom_art
        self.art = art
        self.art_updated_at = art_updated_at
        self.categories = categories
        self.episodes = episodes
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, title: Optional[str] = None, description: Optional[str] = None, language: Optional[str] = None,
        categories: Optional[List[str]] = None, author: Optional[str] = None, email: Optional[str] = None,
        website: Optional[str] = None
    ):
        if language is not None and len(language) > 2:
            language = language.lower().replace(' ', '_')
            language = get_language_code(language)

        return edit_resource(
            self, "station_podcast", title, description, language, author, email, website, categories
        )

    def delete(self):
        return delete_resource(self, "station_podcast")
    
    def _build_update_body(
        self, title, description, language, author, email, website, categories
    ):
        return {
            "title": title if title else self.title,
            "description": description if description else self.description,
            "language": language if language else self.language,
            "author": author if author else self.author,
            "email": email if email else self.email,
            "link": website if website else self.link,
            "categories": categories if categories else self.categories
        }
    
    def _update_properties(
        self, title, description, language, author, email, website, categories
    ):
        self.title = title if title else self.title
        self.description = description if description else self.description
        self.language = language if language else self.language
        self.author = author if author else self.author
        self.email = email if email else self.email
        self.link = website if website else self.link
        self.categories = categories if categories else self.categories

    def _clear_properties(self):
        self.id = None
        self.storage_location_id = None
        self.title = None
        self.link = None
        self.description = None
        self.language = None
        self.author = None
        self.email = None
        self.has_custom_art = None
        self.art = None
        self.art_updated_at = None
        self.categories = None
        self.episodes = None
        self.links = None
        self._station = None

    def get_art(self) -> bytes:
        return get_resource_art(self)

    # TODO: Media and art require file uploads
    # TODO: Schedule episode release
    def add_episode(
        self, title: str, description: str, explicit: bool = False, publish_date: Optional[str] = None,
        publish_time: Optional[str] = None
    ):
        publish_at = None
        if publish_date is not None and publish_time is not None:
            # Generate UTC based off of station timezone
            pass

        url = url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            podcast_id=self.id
        )

        body = {
            "title": title,
            "description": description,
            "explicit": explicit,
            "publish_at": publish_at
        }

        response = self._station._request_handler.post(url, body)

        return PodcastEpisode(**response, _podcast=self)

    def get_episodes(self) -> List[PodcastEpisode]:
        url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            podcast_id=self.id
        )

        response = self._station._request_handler.get(url)

        return [PodcastEpisode(**pe, _podcast=self) for pe in response]
    
    def get_episode(self, id: str) -> PodcastEpisode:
        if type(id) is not str:
            raise TypeError("id param should be of type string.")
        
        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            podcast_id=self.id,
            id=id
        )

        response = self._station._request_handler.get(url)

        return PodcastEpisode(**response, _podcast=self)