from typing import List, Dict, Any, Optional

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util import general_util

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

    def __repr__(self_):
        return (
            f"Links(self={self_.self!r}, episodes={self_.episodes!r}, "
            f"public_episodes={self_.public_episodes!r}, public_feed={self_.public_feed!r}, "
            f"art={self_.art!r}, episode_new_art={self_.episode_new_art!r}, "
            f"episode_new_media={self_.episode_new_media!r})"
        )

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
        return (
            f"Podcast(id={self.id!r}, storage_location_id={self.storage_location_id!r}, "
            f"title={self.title!r}, link={self.link!r}, description={self.description!r}, "
            f"language={self.language!r}, author={self.author!r}, email={self.email!r}, "
            f"has_custom_art={self.has_custom_art!r}, art={self.art!r}, "
            f"art_updated_at={self.art_updated_at!r}, categories={self.categories!r}, "
            f"episodes={self.episodes!r}, links={self.links!r})"
        )
    
    def edit(
        self, title: Optional[str] = None, description: Optional[str] = None, language: Optional[str] = None,
        categories: Optional[List[str]] = None, author: Optional[str] = None, email: Optional[str] = None,
        website: Optional[str] = None
    ):
        old_podcast = self._station.podcast(self.id)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        if language is not None and len(language) > 2:
            language = language.lower().replace(' ', '_')
            language = general_util.get_language_code(language)

        body = self._build_update_body(
            old_podcast, title, description, language, author, email, website, categories
        )

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_podcast, title, description, language, author, email, website, categories
            )

        return response

    def delete(self):
        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response

    def _build_update_body(
        self, old_podcast: "Podcast", title, description, language, author, email, website, categories
    ):
        return {
            "title": title if title else old_podcast.title,
            "description": description if description else old_podcast.description,
            "language": language if language else old_podcast.language,
            "author": author if author else old_podcast.author,
            "email": email if email else old_podcast.email,
            "link": website if website else old_podcast.link,
            "categories": categories if categories else old_podcast.categories
        }
    
    def _update_properties(
        self, old_podcast: "Podcast", title, description, language, author, email, website, categories
    ):
        self.title = title if title else old_podcast.title
        self.description = description if description else old_podcast.description
        self.language = language if language else old_podcast.language
        self.author = author if author else old_podcast.author
        self.email = email if email else old_podcast.email
        self.link = website if website else old_podcast.link
        self.categories = categories if categories else old_podcast.categories

    def _clear_properties(self):
        self.title = None
        self.description = None
        self.language = None
        self.author = None
        self.email = None
        self.link = None
        self.categories = None
        self._station = None

    def podcast_episodes(self) -> List[PodcastEpisode]:
        url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.station_id,
            podcast_id=self.id
        )

        response = self._request_handler.get(url)

        return [PodcastEpisode(**pe, _podcast=self) for pe in response]
    
    def podcast_episode(self, id: str) -> PodcastEpisode:
        if type(id) is not str:
            raise TypeError("id param should be of type string.")
        
        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.station_id,
            podcast_id=self.id,
            id=id
        )

        response = self._request_handler.get(url)

        return PodcastEpisode(**response, _podcast=self)