"""Class for a media file on a station."""

from typing import List, Optional

from ..exceptions import ClientException
from ..constants import API_ENDPOINTS
from ..util.general_util import generate_repr_string
from ..util.media_util import get_media_file_art

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    """Represents the links for a file on a station."""
    def __init__(
        self_,
        self: str
    ):
        """
        Initializes a :class:`Links` instance for a file.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``file.links``.
        """
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class Playlist:
    """Represents playlists that contain the current file."""
    def __init__(
        self,
        id: int,
        name: str,
        weight: int
    ):
        """
        Initializes a :class:`Playlist` instance for a file.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``file.playlists``.
        """
        self.id = id
        self.name = name
        self.weight = weight

    def __repr__(self):
        return generate_repr_string(self)

def _get_playlist_json(playlist):
    return {
        "id": playlist.id,
        "name": playlist.name,
        "weight": playlist.weight
    }

class PlaylistHelper:
    """Provides functions for working with the playlists of a file."""
    def __init__(
        self,
        _file
    ):
        """
        Initializes a :class:`PlaylistHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``file.playlist``.
        """
        self._file = _file

    def add(
        self,
        *args: str
    ):
        """
        Adds the file to one or more playlists.

        :param args: The name(s) of the playlist(s) that the file will be added to.
            All arguments must be strings.

        Usage:
        .. code-block:: python

            file.playlist.add("playlist")

            file.playlist.add("playlist1", "playlist2")
        """
        valid_playlists = [(playlist.id, playlist.name, playlist.weight) for playlist in self._file._station.playlists()]

        playlists = [_get_playlist_json(playlist) for playlist in self._file.playlists]

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be a string."
                raise ClientException(message)

            if not any(arg == playlist[1] for playlist in valid_playlists):
                names = [playlist[1] for playlist in valid_playlists]
                message = f"'{arg}' is not a playlist on this radio station. Valid playlists: "\
                          f"{', '.join(names)}"
                raise ClientException(message)

            if any(arg == playlist['name'] for playlist in playlists):
                message = f"This file is already in the '{arg}' playlist."
                raise ClientException(message)

            # Generates structure for new playlist addition.
            for playlist in valid_playlists:
                if playlist[1] == arg:
                    obj = {
                        "id": playlist[0],
                        "name": playlist[1],
                        "weight": playlist[2]
                    }

            playlists.append(obj)

        url = API_ENDPOINTS["station_file"].format(
            radio_url=self._file._station._request_handler.radio_url,
            station_id=self._file._station.id,
            id=self._file.id
        )

        body = {
            "playlists": playlists
        }

        response = self._file._station._request_handler.put(url, body)

        if response['success'] is True:
            # I hate this.
            self._file.playlists = self._file._station.file(self._file.id).playlists

        return response

    def remove(
        self,
        *args: str
    ):
        """
        Removes the file from one or more playlists.

        :param args: The name(s) of the playlist(s) that the file will be removed from.
            All arguments must be strings.

        Usage:
        .. code-block:: python

            file.playlist.remove("playlist")

            file.playlist.remove("playlist1", "playlist2")
        """
        valid_playlists = [(playlist.id, playlist.name, playlist.weight) for playlist in self._file._station.playlists()]

        playlists = [_get_playlist_json(playlist) for playlist in self._file.playlists]

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be a string."
                raise ClientException(message)

            if not any(arg == playlist[1] for playlist in valid_playlists):
                names = [playlist[1] for playlist in valid_playlists]
                message = f"'{arg}' is not a playlist on this radio station. Valid playlists: "\
                          f"{', '.join(names)}"
                raise ClientException(message)

            if not any(arg == playlist['name'] for playlist in playlists):
                message = f"This file is not in the '{arg}' playlist."
                raise ClientException(message)

            # Deletes playlist. Yes, I hate this too.
            i = 0
            for playlist in playlists:
                if playlist['name'] == arg:
                    del playlists[i]
                    break

                i = i + 1

        url = API_ENDPOINTS["station_file"].format(
            radio_url=self._file._station._request_handler.radio_url,
            station_id=self._file._station.id,
            id=self._file.id
        )

        body = {
            "playlists": playlists
        }

        response = self._file._station._request_handler.put(url, body)

        if response['success'] is True:
            # I hate this.
            self._file.playlists = self._file._station.file(self._file.id).playlists

        return response

class StationFile:
    """Represents an uploaded file on a station."""
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
        """
        Initializes a :class:`StationFile` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.file(id)`` or ``station.files()``.
        """
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
        self.playlists = [Playlist(**p) for p in playlists] if playlists else []
        self.id = id
        self.song_id = song_id
        self.text = text
        self.artist = artist
        self.title = title
        self.custom_fields = custom_fields
        self.links = Links(**links)
        self._station = _station

        self.playlist = PlaylistHelper(_file=self)
        """
        An instance of :class:`.PlaylistHelper`.

        Provides the interface for working with the playlists that this file is in.

        For example, to add the file to one or more playlists:

        .. code-block:: python

            file.playlist.add("playlist")

            file.playlist.add("playlist1", "playlist2")

        To remove the file from one or more playlists:

        .. code-block:: python

            file.playlist.remove("playlist")

            file.playlist.remove("playlist1", "playlist2")
        """

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
            Note: This will overwrite the file's existing playlists.
                  Use the :meth:`.playlist.add` and :meth:`.playlist.remove` methods to
                  interact with the file's existing playlists.
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
                lyrics="I'm so tired",
                playlists=["playlist1", "playlist2"]
            )
        """
        valid_playlists = [(playlist.id, playlist.name, playlist.weight) for playlist in self._station.playlists()]

        playlists_json = []

        for playlist in playlists:
            if not isinstance(playlist, str):
                message = "Each playlist name must be a string."
                raise ClientException(message)

            if not any(playlist == playlist_tuple[1] for playlist_tuple in valid_playlists):
                names = [playlist_tuple[1] for playlist_tuple in valid_playlists]
                message = f"'{playlist}' is not a playlist on this radio station. "\
                          f"Valid playlists: {', '.join(names)}"
                raise ClientException(message)

            # Generates structure for new playlist addition.
            for playlist_tuple in valid_playlists:
                if playlist_tuple[1] == playlist:
                    playlists_json.append(
                        {
                            "id": playlist_tuple[0],
                            "name": playlist_tuple[1],
                            "weight": playlist_tuple[2]
                        }
                    )

        return edit_station_resource(
            self, "station_file", title, artist, path, genre, album, lyrics, isrc,
            playlists_json, amplify, fade_overlap, fade_in, fade_out, cue_in, cue_out
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
        playlists_json,
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
            "playlists": playlists_json or [_get_playlist_json(playlist) for playlist in self.playlists]
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
        playlists_json,
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
        self.playlists = self.playlists if playlists_json is None else self._station.file(self.id).playlists # I'm sorry.
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
