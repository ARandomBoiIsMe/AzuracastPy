"""Class for data of requestable songs of a station."""

from ..util.general_util import generate_repr_string

from .song import Song

class RequestableSong:
    """Represents a song that can be requested on the station."""
    def __init__(
        self,
        request_id: str,
        request_url: str,
        song: Song
    ):
        """
        Initializes a :class:`RequestableSong` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.requestable_songs()``.
        """
        self.request_id = request_id
        self.request_url = request_url
        self.song = Song(**song)

    def __repr__(self):
        return generate_repr_string(self)
