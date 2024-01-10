from .song import Song

from typing import List

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string

class Links:
    def __init__(self_, self: str):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class QueueItem:
    def __init__(
        self, cued_at: int, played_at: int, duration: int, playlist: str, is_request: bool,
        song: Song, sent_to_autodj: bool, is_played: bool, autodj_custom_uri: str, log: List[str],
        links: Links, _station
    ):
        self.cued_at = cued_at
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.is_request = is_request
        self.song = song
        self.sent_to_autodj = sent_to_autodj
        self.is_played = is_played
        self.autodj_custom_uri = autodj_custom_uri
        self.log = log
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    # Doesn't work lol
    def delete(self):
        queue_response = self._station._request_multiple_instances_of("station_queue")
        queue = [QueueItem(**qi, _station=self._station) for qi in queue_response]
        id = queue.index(self)

        url = API_ENDPOINTS["station_queue_item"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _clear_properties(self):
        self.cued_at = None
        self.played_at = None
        self.duration = None
        self.playlist = None
        self.is_request = None
        self.song = None
        self.sent_to_autodj = None
        self.is_played = None
        self.autodj_custom_uri = None
        self.log = None
        self.links = None
        self._station = None