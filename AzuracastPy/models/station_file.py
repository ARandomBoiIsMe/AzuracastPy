from typing import List

class Links:
    def __init__(self_, self: str, **kwargs):
        self_.self = self
        self_.__dict__.update(kwargs) # Incase there are other attributes in the link object from the API
    
    def __repr__(self):
        return f"Links(self={self.self!r}, {', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"

class Playlist:
    def __init__(self, id: int, name: str, weight: int):
        self.id = id
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Playlist(id={self.id!r}, name={self.name!r}, weight={self.weight!r})"

class StationFile:
    def __init__(
            self, unique_id: str, album: str, genre: str, lyrics: str, isrc: str, length: float,
            length_text: str, path: str, mtime: int, amplify, fade_overlap, fade_in, fade_out, cue_in,
            cue_out, art_updated_at: int, playlists: List[Playlist], id: int, song_id: str, text: str,
            artist: str, title: str, custom_fields: List[str], links: Links
        ):
        self.unique_id = unique_id
        self.album = album
        self.genre = genre
        self.lyrics = lyrics
        self.isrc = isrc
        self.length = length
        self.length_text = length_text
        self.path = path
        self.mtime = mtime
        self.amplify = amplify
        self.fade_overlap = fade_overlap
        self.fade_in = fade_in
        self.fade_out = fade_out
        self.cue_in = cue_in
        self.cue_out = cue_out
        self.art_updated_at = art_updated_at
        self.playlists = playlists
        self.id = id
        self.song_id = song_id
        self.text = text
        self.artist = artist
        self.title = title
        self.custom_fields = custom_fields
        self.links = links

    def __repr__(self):
        return (
            f"StationFile(unique_id={self.unique_id!r}, album={self.album!r}, genre={self.genre!r}, "
            f"lyrics={self.lyrics!r}, isrc={self.isrc!r}, length={self.length!r}, length_text={self.length_text!r}, "
            f"path={self.path!r}, mtime={self.mtime!r}, playlists={self.playlists!r}, id={self.id!r}, "
            f"song_id={self.song_id!r}, text={self.text!r}, artist={self.artist!r}, title={self.title!r}, "
            f"custom_fields={self.custom_fields!r}, links={self.links!r})"
        )