from .listeners import Listeners
from .song import Song
from .station import Station
from .song_history import SongHistory

from typing import List

class Live:
    def __init__(self, is_live: bool, streamer_name: str, broadcast_start, art: str):
        self.is_live = is_live
        self.streamer_name = streamer_name
        self.broadcast_start = broadcast_start
        self.art = art

    def __repr__(self):
        return (
            f"Live(is_live={self.is_live!r}, streamer_name={self.streamer_name!r}, "
            f"broadcast_start={self.broadcast_start!r}, art={self.art!r})"
        )

class CurrentSong:
    def __init__(
        self, sh_id: int, played_at: int, duration: int, playlist: str, streamer: str, is_request: bool,
        song: Song, elapsed: int, remaining: int
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
        return (
            f"CurrentSong(sh_id={self.sh_id!r}, played_at={self.played_at!r}, "
            f"duration={self.duration!r}, playlist={self.playlist!r}, streamer={self.streamer!r}, "
            f"is_request={self.is_request!r}, song={self.song!r}, elapsed={self.elapsed!r}, "
            f"remaining={self.remaining!r})"
        )

class PlayingNext:
    def __init__(
        self, cued_at: int, played_at: int, duration: int, playlist: str, is_request: bool, song: Song
    ):
        self.cued_at = cued_at
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.is_request = is_request
        self.song = song

    def __repr__(self):
        return (
            f"PlayingNext(cued_at={self.cued_at!r}, played_at={self.played_at!r}, "
            f"duration={self.duration!r}, playlist={self.playlist!r}, "
            f"is_request={self.is_request!r}, song={self.song!r})"
        )

class NowPlaying:
    def __init__(self, station: Station, listeners: Listeners, live: Live, now_playing: CurrentSong, playing_next: PlayingNext, song_history: List[SongHistory], is_online: bool, cache: str):
        self.station = station
        self.listeners = listeners
        self.live = live
        self.now_playing = now_playing
        self.playing_next = playing_next
        self.song_history = song_history
        self.is_online = is_online
        self.cache = cache

    def __repr__(self):
        return (
            f"NowPlaying(station={self.station!r}, listeners={self.listeners!r}, "
            f"live={self.live!r}, now_playing={self.now_playing!r}, "
            f"playing_next={self.playing_next!r}, song_history={self.song_history!r}, "
            f"is_online={self.is_online!r}, cache={self.cache!r})"
        )