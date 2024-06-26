"""Class for an item in a station queue."""

from .song import Song

from typing import List

from ..constants import API_ENDPOINTS
from ..util.general_util import generate_repr_string

class Links:
    """Represents the links associated with an item in a queue."""
    def __init__(
        self_,
        self: str
    ):
        """
        Initializes a :class:`Links` object for a queue item.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``queue_item.links``.
        """
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class QueueItem:
    """Represents a single item in the queue of a station."""
    def __init__(
        self,
        cued_at: int,
        played_at: int,
        duration: int,
        playlist: str,
        is_request: bool,
        song: Song,
        sent_to_autodj: bool,
        is_played: bool,
        autodj_custom_uri: str,
        log: List[str],
        links: Links,
        _station
    ):
        """
        Initializes a :class:`QueueItem` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.models.helpers.QueueHelper.__call__`.
        """
        self.cued_at = cued_at
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.is_request = is_request
        self.song = Song(**song)
        self.sent_to_autodj = sent_to_autodj
        self.is_played = is_played
        self.autodj_custom_uri = autodj_custom_uri
        self.log = log
        self.links = Links(**links)
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)

    # # Doesn't work lol
    # def delete(self):
    #     queue = self._station.queue()

    #     # Linear search. Yay.
    #     id = 0
    #     for item in queue:
    #         if item == self:
    #             break

    #         id = id + 1

    #     id = id + 1 # Returning id back to normal format.
    #     url = API_ENDPOINTS["station_queue_item"].format(
    #         radio_url=self._station._request_handler.radio_url,
    #         station_id=self._station.id,
    #         id=id
    #     )

    #     response = self._station._request_handler.delete(url)

    #     if response['success'] is True:
    #         self._clear_properties()

    #     return response

    # def _clear_properties(self):
    #     self.cued_at = None
    #     self.played_at = None
    #     self.duration = None
    #     self.playlist = None
    #     self.is_request = None
    #     self.song = None
    #     self.sent_to_autodj = None
    #     self.is_played = None
    #     self.autodj_custom_uri = None
    #     self.log = None
    #     self.links = None
    #     self._station = None
