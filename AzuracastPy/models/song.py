from typing import List

from AzuracastPy.util.general_util import generate_repr_string

class Song:
    def __init__(
            self, id: str, text: str, artist: str, title: str, album: str, genre: str, isrc: str,
            lyrics: str, art: str, custom_fields: List[str]
        ):
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