from typing import List, Dict, Any

from AzuracastPy.request_handler import RequestHandler

from AzuracastPy.constants import API_ENDPOINTS

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
            episodes: List[str], links: Links, station_id: int = None, _request_handler: RequestHandler = None
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
        self.station_id = station_id
        self._request_handler = _request_handler

    def __repr__(self):
        return (
            f"Podcast(id={self.id!r}, storage_location_id={self.storage_location_id!r}, "
            f"title={self.title!r}, link={self.link!r}, description={self.description!r}, "
            f"language={self.language!r}, author={self.author!r}, email={self.email!r}, "
            f"has_custom_art={self.has_custom_art!r}, art={self.art!r}, "
            f"art_updated_at={self.art_updated_at!r}, categories={self.categories!r}, "
            f"episodes={self.episodes!r}, links={self.links!r})"
        )
    
    def podcast_episodes(self) -> List[PodcastEpisode]:
        url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.station_id,
            podcast_id=self.id
        )

        response = self._request_handler.get(url)

        params = {
            "station_id": self.station_id,
            "podcast_id": self.id
        }

        return [PodcastEpisode(**pe, params=params, _request_handler=self._request_handler) for pe in response]
    
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

        params = {
            "station_id": self.station_id,
            "podcast_id": self.id
        }

        return PodcastEpisode(**response, params=params, _request_handler=self._request_handler)