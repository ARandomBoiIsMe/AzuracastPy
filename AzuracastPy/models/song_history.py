from .song import Song

from AzuracastPy.util.general_util import generate_repr_string

class SongHistory:
    def __init__(
            self, sh_id: int, played_at: int, duration: int, playlist: str, streamer: str,
            is_request: bool, song: Song, listeners_start: int, listeners_end: int, delta_total: int,
            is_visible: bool
        ):
        self.sh_id = sh_id
        self.played_at = played_at
        self.duration = duration
        self.playlist = playlist
        self.streamer = streamer
        self.is_request = is_request
        self.song = song
        self.listeners_start = listeners_start
        self.listeners_end = listeners_end
        self.delta_total = delta_total
        self.is_visible = is_visible

    def __repr__(self):
        return generate_repr_string(self)