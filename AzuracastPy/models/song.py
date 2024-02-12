"""Class for a song on a station."""

from typing import Dict

from ..util.general_util import generate_repr_string

class Song:
    """Represents a song object."""
    def __init__(
        self,
        id: str,
        text: str,
        artist: str,
        title: str,
        album: str,
        genre: str,
        isrc: str,
        lyrics: str,
        art: str,
        custom_fields: Dict[str, str]
    ):
        """
        Initializes a :class:`Song` object.

        .. note::

            This class should not be initialized directly. Instead, an instance will be made
            available as an attribute of other classes: :class:`RequestableSong`,
            :class:`SongHistory`, :class:`QueueItem`, :class:`CurrentSong`,
            :class:`PlayingNext`.
        """
        self.id = id
        self.text = text
        self.artist = artist
        self.title = title
        self.album = album
        self.genre = genre
        self.isrc = isrc
        self.lyrics = lyrics
        self.art = art
        self.custom_fields = custom_fields

    def __repr__(self) -> str:
        return generate_repr_string(self)
