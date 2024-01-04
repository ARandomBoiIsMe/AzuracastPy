from .song import Song

class RequestableSong:
    def __init__(self, request_id: str, request_url: str, song: Song):
        self.request_id = request_id
        self.request_url = request_url
        self.song = song

    def __repr__(self):
        return (
            f"RequestableSong(request_id={self.request_id!r}, request_url={self.request_url!r}, "
            f"song={self.song!r})"
        )