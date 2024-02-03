""""Class for a podcast episode."""

from typing import Optional

from ..constants import API_ENDPOINTS
from ..util.media_util import get_resource_art
from ..util.general_util import generate_repr_string

class Links:
    def __init__(
        self_,
        self: str,
        public: str,
        download: str,
        art: str,
        media: str
    ):
        self_.self = self
        self_.public = public
        self_.download = download
        self_.art = art
        self_.media = media

    def __repr__(self):
        return generate_repr_string(self)

class Media:
    def __init__(
        self,
        id: str,
        original_name: str,
        length: int,
        length_text: str,
        path: str
    ):
        self.id = id
        self.original_name = original_name
        self.length = length
        self.length_text = length_text
        self.path = path

    def __repr__(self):
        return generate_repr_string(self)

class PodcastEpisode:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        explicit: bool,
        publish_at: int,
        has_media: bool,
        media: Media,
        has_custom_art: bool,
        art: str,
        art_updated_at: int,
        links: Links,
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
        return generate_repr_string(self)

    def edit(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        explicit: Optional[bool] = None
    ):
        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id,
            id=self.id
        )

        body = self._build_update_body(title, description, explicit)

        response = self._podcast._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(title, description, explicit)

        return response

    def delete(self):
        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id,
            id=self.id
        )

        response = self._podcast._station._request_handler.delete(url)

        if response['success']:
            self._clear_properties()

        return response

    def _build_update_body(
        self,
        title,
        description,
        explicit
    ):
        return {
            "title": title or self.title,
            "description": description or self.description,
            "explicit": explicit if explicit is not None else self.explicit
        }

    def _update_properties(
        self,
        title,
        description,
        explicit
    ):
        self.title = title or self.title
        self.description = description or self.description
        self.explicit = explicit if explicit is not None else self.explicit

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

    def get_art(self) -> bytes:
        return get_resource_art(self)
