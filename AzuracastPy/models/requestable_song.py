from .song import Song

from AzuracastPy.util.general_util import generate_repr_string

class RequestableSong:
    def __init__(
        self, 
        request_id: str, 
        request_url: str, 
        song: Song
    ):
        self.request_id = request_id
        self.request_url = request_url
        self.song = song

    def __repr__(self):
        return generate_repr_string(self)