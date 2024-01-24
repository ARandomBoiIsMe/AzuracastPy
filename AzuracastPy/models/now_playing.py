from .listeners import Listeners
from .song import Song
from .station import Station
from .song_history import SongHistory

from typing import List

from AzuracastPy.util.general_util import generate_repr_string

class Live:
    def __init__(
        self, 
        is_live: bool, 
        streamer_name: str, 
        broadcast_start, art: str
    ):
        self.is_live = is_live
        self.streamer_name = streamer_name
        self.broadcast_start = broadcast_start
        self.art = art

    def __repr__(self):
        return generate_repr_string(self)

class CurrentSong:
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
        self.sh_id = sh_id
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.streamer = streamer
        self.is_request = is_request
        self.song = song
        self.elapsed = elapsed
        self.remaining = remaining

    def __repr__(self):
        return generate_repr_string(self)

class PlayingNext:
    def __init__(
        self, 
        cued_at: int,
        played_at: int, 
        duration: int, 
        playlist: str, 
        is_request: bool, 
        song: Song
    ):
        self.cued_at = cued_at
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.is_request = is_request
        self.song = song

    def __repr__(self):
        return generate_repr_string(self)

class NowPlaying:
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
        self.station = station
        self.listeners = listeners
        self.live = live
        self.now_playing = now_playing
        self.playing_next = playing_next
        self.song_history = song_history
        self.is_online = is_online
        self.cache = cache

    def __repr__(self):
        return generate_repr_string(self)