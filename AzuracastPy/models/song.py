from typing import List

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

    def __repr__(self):
        return (
            f"Song(id={self.id!r}, artist={self.artist!r}, title={self.title!r}, album={self.album!r}, "
            f"genre={self.genre!r}, isrc={self.isrc!r})"
        )