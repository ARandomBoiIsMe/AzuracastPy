from typing import List, Optional

from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.util.media_util import get_media_file_art

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_,
        self: str
    ):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class Playlist:
    def __init__(
        self, 
        id: int, 
        name: str, 
        weight: int
    ):
        self.id = id
        self.name = name
        self.weight = weight

    def __repr__(self):
        return generate_repr_string(self)

class StationFile:
    def __init__(
        self, 
        unique_id: str, 
        album: str, 
        genre: str, 
        lyrics: str, 
        isrc: str, 
        length: float,
        length_text: str, 
        path: str, 
        mtime: int, 
        amplify, 
        fade_overlap,
        fade_in, 
        fade_out, 
        cue_in,
        cue_out, 
        art_updated_at: int, 
        playlists: List[Playlist], 
        id: int, 
        song_id: str, 
        text: str,
        artist: str, 
        title: str, 
        custom_fields: List[str], 
        links: Links, 
        _station
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
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, 
        title: Optional[str] = None, 
        artist: Optional[str] = None, 
        path: Optional[str] = None,
        genre: Optional[str] = None, 
        album: Optional[str] = None, 
        lyrics: Optional[str] = None,
        isrc: Optional[str] = None, 
        playlists: Optional[List[str]] = None, 
        amplify: Optional[int] = None,
        fade_overlap: Optional[int] = None, 
        fade_in: Optional[int] = None, 
        fade_out: Optional[int] = None,
        cue_in: Optional[int] = None, 
        cue_out: Optional[int] = None
    ):
        """
        Edits the file's properties.

        :param title:
        :param artist:
        :param path:
        :param genre:
        :param album:
        :param lyrics:
        :param isrc:
        :param playlists:
        :param amplify:
        :param fade_overlap:
        :param fade_in:
        :param fade_out:
        :param cue_in:
        :param cue_out:
        """
        return edit_station_resource(
            self, "station_file", title, artist, path, genre, album, lyrics, isrc,
            playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
        )
    
    def delete(self):
        """
        Deletes the file from the station.
        """
        return delete_station_resource(self, "station_file")

    def _build_update_body(
        self, 
        title, 
        artist, 
        path, 
        genre, 
        album, 
        lyrics, 
        isrc,
        playlists, 
        amplify, 
        fade_overlap, 
        fade_in, 
        fade_out, 
        cue_in, 
        cue_out
    ):
        return {
            "artist": artist if artist else self.artist,
            "title": title if title else self.title,
            "album": album if album else self.album,
            "genre": genre if genre else self.genre,
            "lyrics": lyrics if lyrics else self.lyrics,
            "path": path if path else self.path,
            "isrc": isrc if isrc else self.isrc,
            "amplify": amplify if amplify else self.amplify,
            "fade_overlap": fade_overlap if fade_overlap else self.fade_overlap,
            "fade_in": fade_in if fade_in else self.fade_in,
            "fade_out": fade_out if fade_out else self.fade_out,
            "cue_in": cue_in if cue_in else self.cue_in,
            "cue_out": cue_out if cue_out else self.cue_out,
            "playlists": playlists if playlists else self.playlists
        }
    
    def _update_properties(
        self, 
        title, 
        artist, 
        path, 
        genre, 
        album, 
        lyrics, 
        isrc,
        playlists, 
        amplify, 
        fade_overlap, 
        fade_in, 
        fade_out, 
        cue_in, 
        cue_out
    ):
        self.album = album if album else self.album
        self.genre = genre if genre else self.genre
        self.lyrics = lyrics if lyrics else self.lyrics
        self.isrc = isrc if isrc else self.isrc
        self.path = path if path else self.path
        self.amplify = amplify if amplify else self.amplify
        self.fade_overlap = fade_overlap if fade_overlap else self.fade_overlap
        self.fade_in = fade_in if fade_in else self.fade_in
        self.fade_out = fade_out if fade_out else self.fade_out
        self.cue_in = cue_in if cue_in else self.cue_in
        self.cue_out = cue_out if cue_out else self.cue_out
        self.playlists = playlists if playlists else self.playlists
        self.artist = artist if artist else self.artist
        self.title = title if title else self.title

    def _clear_properties(self):
        self.unique_id = None
        self.album = None
        self.genre = None
        self.lyrics = None
        self.isrc = None
        self.length = None
        self.length_text = None
        self.path = None
        self.mtime = None
        self.amplify = None
        self.fade_overlap = None
        self.fade_in = None
        self.fade_out = None
        self.cue_in = None
        self.cue_out = None
        self.art_updated_at = None
        self.playlists = None
        self.id = None
        self.song_id = None
        self.text = None
        self.artist = None
        self.title = None
        self.custom_fields = None
        self.links = None
        self._station = None

    def get_art(self) -> bytes:
        return get_media_file_art(self)