from .song import Song

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
        return (
            f"SongHistory(sh_id={self.sh_id}, played_at={self.played_at}, duration={self.duration}, "
            f"playlist={self.playlist!r}, streamer={self.streamer!r}, is_request={self.is_request}, "
            f"song={self.song!r}, listeners_start={self.listeners_start}, listeners_end={self.listeners_end}, "
            f"delta_total={self.delta_total}, is_visible={self.is_visible})"
        )