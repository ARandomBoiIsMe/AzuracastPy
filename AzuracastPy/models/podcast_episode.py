from typing import List, Dict, Any, Optional

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util import file_upload_util

class Links:
    def __init__(self_, self: str, public: str, download: str, art: str, media: str):
        self_.self = self
        self_.public = public
        self_.download = download
        self_.art = art
        self_.media = media

    def __repr__(self_):
        return (
            f"Links(self={self_.self!r}, public={self_.public!r}, download={self_.download!r}, "
            f"art={self_.art!r}, media={self_.media!r})"
        )

class Media:
    def __init__(self, id: str, original_name: str, length: int, length_text: str, path: str):
        self.id = id
        self.original_name = original_name
        self.length = length
        self.length_text = length_text
        self.path = path

    def __repr__(self):
        return (
            f"Media(id={self.id!r}, original_name={self.original_name!r}, length={self.length!r}, "
            f"length_text={self.length_text!r}, path={self.path!r})"
        )

class PodcastEpisode:
    def __init__(
        self, id: str, title: str, description: str, explicit: bool, publish_at: int, has_media: bool,
        media: Media, has_custom_art: bool, art: str, art_updated_at: int, links: Links,
        _podcast
    ):
        self.id = id
        self.title = title
        self.description = description
        self.explicit = explicit
        self.publish_at = publish_at
        self.has_media = has_media
        self.media = media
        self.has_custom_art = has_custom_art
        self.art = art
        self.art_updated_at = art_updated_at
        self.links = links
        self._podcast = _podcast

    def __repr__(self):
        return (
            f"PodcastEpisode(id={self.id!r}, title={self.title!r}, description={self.description!r}, "
            f"explicit={self.explicit!r}, publish_at={self.publish_at!r}, has_media={self.has_media!r}, "
            f"media={self.media!r}, has_custom_art={self.has_custom_art!r}, art={self.art!r}, "
            f"art_updated_at={self.art_updated_at!r}, links={self.links!r})"
        )
    
    def edit(
        self, title: Optional[str] = None, description: Optional[str] = None, explicit: Optional[bool] = None
    ):
        old_episode = self._podcast.get_episode(self.id)

        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id,
            id=self.id
        )

        body = self._build_update_body(
            old_episode, title, description, explicit
        )

        response = self._podcast._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_episode, title, description, explicit
            )

        return response

    def delete(self):
        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id,
            id=self.id
        )

        response = self._podcast._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response

    def get_art(self):
        return self._podcast._station._request_handler.get(self.art)

    def _build_update_body(
        self, old_episode: "PodcastEpisode", title, description, explicit
    ):
        return {
            "title": title if title else old_episode.title,
            "description": description if description else old_episode.description,
            "explicit": explicit if explicit else old_episode.explicit
        }
    
    def _update_properties(
        self, old_episode: "PodcastEpisode", title, description, explicit
    ):
        self.title = title if title else old_episode.title
        self.description = description if description else old_episode.description
        self.explicit = explicit if explicit else old_episode.explicit

    def _clear_properties(self):
        self.id = None
        self.title = None
        self.description = None
        self.explicit = None
        self.publish_at = None
        self.has_media = None
        self.media = None
        self.has_custom_art = None
        self.art = None
        self.art_updated_at = None
        self.links = None
        self._podcast = None