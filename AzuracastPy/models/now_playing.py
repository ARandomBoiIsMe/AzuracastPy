"""Class for a station's nowplaying data."""

from typing import List

from ..util.general_util import generate_repr_string

from .listeners import Listeners
from .song import Song
from .station import Station
from .song_history import SongHistory

class Live:
    """Represents live status and info of the currently-playing song on a station."""
    def __init__(
        self,
        is_live: bool,
        streamer_name: str,
        broadcast_start, art: str
    ):
        """
        Initializes a :class:`Live` object for a :class:`NowPlaying` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``now_playing.live``.
        """
        self.is_live = is_live
        self.streamer_name = streamer_name
        self.broadcast_start = broadcast_start
        self.art = art

    def __repr__(self):
        return generate_repr_string(self)

class CurrentSong:
    """Represents the currently-playing song on a station."""
    def __init__(
        self,
        sh_id: int,
        played_at: int,
        duration: int,
        playlist: str,
        streamer: str,
        is_request: bool,
        song: Song,
        elapsed: int,
        remaining: int
    ):
        """
        Initializes a :class:`CurrentSong` object for a :class:`NowPlaying` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``now_playing.now_playing``.
        """
        self.sh_id = sh_id
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.streamer = streamer
        self.is_request = is_request
        self.song = Song(**song)
        self.elapsed = elapsed
        self.remaining = remaining

    def __repr__(self):
        return generate_repr_string(self)

class PlayingNext:
    """Represents the data of the next song to be played on a station."""
    def __init__(
        self,
        cued_at: int,
        played_at: int,
        duration: int,
        playlist: str,
        is_request: bool,
        song: Song
    ):
        """
        Initializes a :class:`PlayingNext` object for a :class:`NowPlaying` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``now_playing.playing_next``.
        """
        self.cued_at = cued_at
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.is_request = is_request
        self.song = song

    def __repr__(self):
        return generate_repr_string(self)

class NowPlaying:
    """Represents the data of the current status of a station."""
    def __init__(
        self,
        station: Station,
        listeners: Listeners,
        live: Live,
        now_playing: CurrentSong,
        playing_next: PlayingNext,
        song_history: List[SongHistory],
        is_online: bool,
        cache: str
    ):
        """
        Initializes a :class:`NowPlaying` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.AzuracastClient.now_playing`.
        """
        self.station = Station(**station)
        self.listeners = Listeners(**listeners)
        self.live = Live(**live)
        self.now_playing = CurrentSong(**now_playing)
        self.playing_next = PlayingNext(**playing_next)
        self.song_history = [SongHistory(**sh) for sh in song_history] if song_history else []
        self.is_online = is_online
        self.cache = cache

    def __repr__(self):
        return generate_repr_string(self)
