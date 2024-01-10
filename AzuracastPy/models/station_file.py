from typing import List, Optional

from .links import Links

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string

class Playlist:
    def __init__(self, id: int, name: str, weight: int):
        self.id = id
        self.name = name
        self.weight = weight

    def __repr__(self):
        return generate_repr_string(self)

class StationFile:
    def __init__(
        self, unique_id: str, album: str, genre: str, lyrics: str, isrc: str, length: float,
        length_text: str, path: str, mtime: int, amplify, fade_overlap, fade_in, fade_out, cue_in,
        cue_out, art_updated_at: int, playlists: List[Playlist], id: int, song_id: str, text: str,
        artist: str, title: str, custom_fields: List[str], links: Links, _station
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
        self, title: Optional[str] = None, artist: Optional[str] = None, path: Optional[str] = None,
        genre: Optional[str] = None, album: Optional[str] = None, lyrics: Optional[str] = None,
        isrc: Optional[str] = None, playlists: Optional[List[str]] = None, amplify: Optional[int] = None,
        fade_overlap: Optional[int] = None, fade_in: Optional[int] = None, fade_out: Optional[int] = None,
        cue_in: Optional[int] = None, cue_out: Optional[int] = None
    ):
        old_file = self._station.file(self.id)

        url = API_ENDPOINTS["station_file"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(
            old_file, title, artist, path, genre, album, lyrics, isrc,
            playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
        )

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_file, title, artist, path, genre, album, lyrics, isrc,
                playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
            )
            
        return response
    
    def delete(self):
        url = API_ENDPOINTS["station_file"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self.station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response

    def _build_update_body(
        self, old_file: "StationFile", title, artist, path, genre, album, lyrics, isrc,
        playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
    ):
        return {
            "artist": artist if artist else old_file.artist,
            "title": title if title else old_file.title,
            "album": album if album else old_file.album,
            "genre": genre if genre else old_file.genre,
            "lyrics": lyrics if lyrics else old_file.lyrics,
            "path": path if path else old_file.path,
            "isrc": isrc if isrc else old_file.isrc,
            "amplify": amplify if amplify else old_file.amplify,
            "fade_overlap": fade_overlap if fade_overlap else old_file.fade_overlap,
            "fade_in": fade_in if fade_in else old_file.fade_in,
            "fade_out": fade_out if fade_out else old_file.fade_out,
            "cue_in": cue_in if cue_in else old_file.cue_in,
            "cue_out": cue_out if cue_out else old_file.cue_out,
            "playlists": playlists if playlists else old_file.playlists
        }
    
    def _update_properties(
        self, old_file: "StationFile", title, artist, path, genre, album, lyrics, isrc,
        playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
    ):
        self.album = album if album else old_file.album
        self.genre = genre if genre else old_file.genre
        self.lyrics = lyrics if lyrics else old_file.lyrics
        self.isrc = isrc if isrc else old_file.isrc
        self.path = path if path else old_file.path
        self.amplify = amplify if amplify else old_file.amplify
        self.fade_overlap = fade_overlap if fade_overlap else old_file.fade_overlap
        self.fade_in = fade_in if fade_in else old_file.fade_in
        self.fade_out = fade_out if fade_out else old_file.fade_out
        self.cue_in = cue_in if cue_in else old_file.cue_in
        self.cue_out = cue_out if cue_out else old_file.cue_out
        self.playlists = playlists if playlists else old_file.playlists
        self.artist = artist if artist else old_file.artist
        self.title = title if title else old_file.title

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
        self.station = None