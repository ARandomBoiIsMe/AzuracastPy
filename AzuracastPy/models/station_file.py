"""Class for a media file on a station."""

from typing import List, Optional

from ..util.general_util import generate_repr_string
from ..util.media_util import get_media_file_art

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
        self.playlists = [Playlist(**p) for p in playlists] or []
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

        Updates all edited attributes of the current :class:`StationFile` object.

        :param title: (Optional) The new title of the song. Default: ``None``.
        :param artist: (Optional) The new artist of the song. Default: ``None``.
        :param path: (Optional) The new relative path of the song in the station's media directory.
            Default: ``None``.
        :param genre: (Optional) The new genre of the song. Default: ``None``.
        :param album: (Optional) The new album of the song. Default: ``None``.
        :param lyrics: (Optional) The new lyrics of the song. Default: ``None``.
        :param isrc: (Optional) The new International Standard Recording Code of the song.
            Default: ``None``.
        :param playlists: (Optional) The new list of playlists that the song has been added to.
            Default: ``None``.
        :param amplify: (Optional) The volume in decibels to amplify the track with.
            Leave as ``None`` to use the system default. Default: ``None``.
        :param fade_overlap: (Optional) The time that this song should overlap its surrounding
            songs when fading. Leave as ``None`` to use the system default. Default: ``None``.
        :param fade_in: (Optional) The time period that the song should fade in.
            Leave as ``None`` to use the system default. Default: ``None``.
        :param fade_out: (Optional) The time period that the song should fade out.
            Leave as ``None`` to use the system default. Default: ``None``.
        :param cue_in: (Optional) Seconds from the start of the song that the AutoDJ should start
            playing. Default: ``None``.
        :param cue_out: (Optional) Seconds from the start of the song that the AutoDJ should stop
            playing. Default: ``None``.

        Usage:
        .. code-block:: python

            station.file.edit(
                title="Never gonna give you up",
                artist="Lil Wayne",
                lyrics="I'm so tired"
            )
        """
        return edit_station_resource(
            self, "station_file", title, artist, path, genre, album, lyrics, isrc,
            playlists, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
        )

    def delete(self):
        """
        Deletes the file from the station.

        Sets all attributes of the current :class:`StationFile` object to ``None``.

        Usage:
        .. code-block:: python

            station.file.delete()
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
            "artist": artist or self.artist,
            "title": title or self.title,
            "album": album or self.album,
            "genre": genre or self.genre,
            "lyrics": lyrics or self.lyrics,
            "path": path or self.path,
            "isrc": isrc or self.isrc,
            "amplify": amplify or self.amplify,
            "fade_overlap": fade_overlap or self.fade_overlap,
            "fade_in": fade_in or self.fade_in,
            "fade_out": fade_out or self.fade_out,
            "cue_in": cue_in or self.cue_in,
            "cue_out": cue_out or self.cue_out,
            "playlists": playlists or self.playlists
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
        self.album = album or self.album
        self.genre = genre or self.genre
        self.lyrics = lyrics or self.lyrics
        self.isrc = isrc or self.isrc
        self.path = path or self.path
        self.amplify = amplify or self.amplify
        self.fade_overlap = fade_overlap or self.fade_overlap
        self.fade_in = fade_in or self.fade_in
        self.fade_out = fade_out or self.fade_out
        self.cue_in = cue_in or self.cue_in
        self.cue_out = cue_out or self.cue_out
        self.playlists = playlists or self.playlists
        self.artist = artist or self.artist
        self.title = title or self.title

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
