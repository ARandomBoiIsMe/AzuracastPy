"""Class for a station playlist."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from ..constants import API_ENDPOINTS
from ..exceptions import ClientException
from ..enums import PlaylistTypes, PlaylistSources, PlaylistOrders, PlaylistRemoteTypes
from ..util.general_util import generate_repr_string, generate_enum_error_text

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Export:
    def __init__(
        self,
        pls: str,
        m3u: str
    ):
        """
        Initializes a :class:`Export` object for a :class:`Links` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``playlist.links.export``.
        """
        self.pls = pls
        self.m3u = m3u

    def __repr__(self) -> str:
        return generate_repr_string(self)

class Links:
    """Represents the links associated with a playlist."""
    def __init__(
        self,
        _self: str,
        toggle: str,
        clone: str,
        queue: str,
        _import: str,
        reshuffle: str,
        applyto: str,
        empty: str,
        export: Export
    ):
        """
        Initializes a :class:`Links` object for a playlist.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``playlist.links``.
        """
        self._self = _self
        self.toggle = toggle
        self.clone = clone
        self.queue = queue
        self._import = _import
        self.reshuffle = reshuffle
        self.applyto = applyto
        self.empty = empty
        self.export = Export(**export)

    def __repr__(self) -> str:
        return generate_repr_string(self)

    @classmethod
    def from_dict(
        cls,
        links_dict: Dict[str, Any]
    ):
        return cls(
            _self=links_dict.get("self"),
            toggle=links_dict.get("toggle"),
            clone=links_dict.get("clone"),
            queue=links_dict.get("queue"),
            _import=links_dict.get("import"),
            reshuffle=links_dict.get("reshuffle"),
            applyto=links_dict.get("applyto"),
            empty=links_dict.get("empty"),
            export=links_dict.get("export")
        )

class ScheduleItem:
    """Represents a single item in a playlist's schedule."""
    def __init__(
        self,
        start_time: int,
        end_time: int,
        start_date: str,
        end_date: str,
        days: List[int],
        loop_once: bool,
        id: int
    ):
        """
        Initializes a :class:`ScheduleItem` object for a playlist.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``playlist.schedule_items``.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        self.days = days
        self.loop_once = loop_once
        self.id = id

    def __repr__(self) -> str:
        return generate_repr_string(self)

def _get_schedule_item_json(schedule_item):
    if not schedule_item:
        return {}

    start_date_formatted = schedule_item.start_date.strftime("%Y-%m-%d") if schedule_item.start_date else None
    end_date_formatted = schedule_item.end_date.strftime("%Y-%m-%d") if schedule_item.end_date else None

    return {
        "start_time": schedule_item.start_time,
        "end_time": schedule_item.end_time,
        "start_date": start_date_formatted,
        "end_date": end_date_formatted,
        "days": schedule_item.days,
        "loop_once": schedule_item.loop_once
    }

class ScheduleHelper:
    """Provides functions for working with the schedule of a playlist."""
    def __init__(
        self,
        _playlist
    ):
        """
        Initializes a :class:`ScheduleHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``playlist.schedule``.
        """
        self._playlist = _playlist

    def add(
        self,
        *args: Dict[str, Any]
    ):
        """
        Adds one or more new schedule items to the playlist of the station.

        :param args: The new schedule item(s) to be added to the playlist.

        Usage:

        .. code-block:: python

            item = station.playlist.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"]
            )

            playlist.schedule.add(item)
        """
        schedule_items = [_get_schedule_item_json(item) for item in self._playlist.schedule_items]

        for arg in args:
            schedule_items.append(arg)

        url = API_ENDPOINTS["station_playlist"].format(
            radio_url=self._playlist._station._request_handler.radio_url,
            station_id=self._playlist._station.id,
            id=self._playlist.id
        )

        body = {
            "schedule_items": schedule_items
        }

        response = self._playlist._station._request_handler.put(url, body)

        if response['success'] is True:
            # Updates the playlist's properties on the object.
            # Inefficient, but can't think of a better way.
            self._playlist.schedule_items = self._playlist._station.playlist(self._playlist.id).schedule_items

        return response

    def remove(
        self,
        id: int
    ):
        """
        Removes a schedule item from the playlist's current schedule.

        :param id: The ID of the schedule item to be removed.

        Usage:

        .. code-block:: python

            playlist.schedule.remove(1)
        """
        item_exists_in_schedule = any(item.id == id for item in self._playlist.schedule_items)

        if not item_exists_in_schedule:
            message = f"No schedule item of id '{id}' exists in this playlist's current schedule."
            raise ClientException(message)

        schedule_items = [_get_schedule_item_json(item) for item in self._playlist.schedule_items if item.id != id]

        # Now for the request.
        url = API_ENDPOINTS["station_playlist"].format(
            radio_url=self._playlist._station._request_handler.radio_url,
            station_id=self._playlist._station.id,
            id=self._playlist.id
        )

        body = {
            "schedule_items": schedule_items
        }

        response = self._playlist._station._request_handler.put(url, body)

        if response['success'] is True:
            # Updates the playlist's properties on the object.
            # Inefficient, but can't think of a better way.
            self._playlist.schedule_items = self._playlist._station.playlist(self._playlist.id).schedule_items

        return response

class Playlist:
    """Represents a playlist on a station."""
    def __init__(
        self,
        name: str,
        type: str,
        source: str,
        order: str,
        remote_url: str,
        remote_type: str,
        remote_buffer: int,
        is_enabled: bool,
        is_jingle: bool,
        play_per_songs: int,
        play_per_minutes: int,
        play_per_hour_minute: int,
        weight: int,
        include_in_requests: bool,
        include_in_on_demand: bool,
        backend_options: List[str],
        avoid_duplicates: bool,
        played_at: int,
        queue_reset_at: int,
        schedule_items: List[ScheduleItem],
        id: int,
        short_name: str,
        num_songs: int,
        total_length: int,
        links: Dict[str, Any],
        _station
    ):
        """
        Initializes a :class:`Playlist` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.models.helpers.PlaylistHelper.create`,
            :meth:`~.models.helpers.PlaylistHelper.__call__` or
            :meth:`~.models.Station.playlists`.
        """
        self.name = name
        self.type = type
        self.source = source
        self.order = order
        self.remote_url = remote_url
        self.remote_type = remote_type
        self.remote_buffer = remote_buffer
        self.is_enabled = is_enabled
        self.is_jingle = is_jingle
        self.play_per_songs = play_per_songs
        self.play_per_minutes = play_per_minutes
        self.play_per_hour_minute = play_per_hour_minute
        self.weight = weight
        self.include_in_requests = include_in_requests
        self.include_in_on_demand = include_in_on_demand
        self.backend_options = backend_options
        self.avoid_duplicates = avoid_duplicates
        self.played_at = played_at
        self.queue_reset_at = queue_reset_at
        self.schedule_items = [ScheduleItem(**si) for si in schedule_items] if schedule_items else []
        self.id = id
        self.short_name = short_name
        self.num_songs = num_songs
        self.total_length = total_length
        self.links = Links.from_dict(links) if links else None
        self._station = _station

        self.schedule = ScheduleHelper(_playlist=self)
        """
        An instance of :class:`.ScheduleHelper`.

        Provides the interface for working with this playlist's schedule.

        For example, to add an item to the schedule:

        .. code-block:: python

            item = station.playlist.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"]
            )

            playlist.schedule.add(item)

        To remove an item whose id is ``1`` from the schedule:

        .. code-block:: python

            playlist.schedule.remove(1)
        """

    def __repr__(self) -> str:
        return generate_repr_string(self)

    def edit(
        self,
        name: Optional[str] = None,
        source: Optional[PlaylistSources] = None,
        type: Optional[PlaylistTypes] = None,
        order: Optional[PlaylistOrders] = None,
        avoid_duplicates: Optional[bool] = None,
        allow_requests: Optional[bool] = None,
        play_per_value: Optional[int] = None,
        weight: Optional[int] = None,
        include_in_on_demand: Optional[bool] = None,
        is_jingle: Optional[bool] = None,
        remote_url: Optional[str] = None,
        remote_type: Optional[PlaylistRemoteTypes] = None,
        remote_buffer: Optional[int] = None,
        schedule: Optional[List[Dict[str, Any]]] = None
    ):
        """
        Edits the playlist's properties.

        Updates all edited attributes of the current :class:`Playlist` object.

        :param name: (Optional) The new name of the playlist. Default: ``None``.
        :param source: (Optional) Specify where the playlist gets its contents from.
            Default: ``None``.
        :param type: (Optional) The internal play-type of the playlist. Not needed if playlist's
            source is set to ``PlaylistSources.REMOTE_URL``. Default: ``None``.
        :param order: (Optional) Determines the playback order of the songs in the playlist.
            Not needed if playlist's source is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``None``.
        :param avoid_duplicates: (Optional) Determines whether duplicate artists and track titles
            will be avoided when playing media from this playlist. Not needed if playlist's source
            is set to ``PlaylistSources.REMOTE_URL``. Default: ``None``.
        :param allow_requests: (Optional) Determines whether users will be able to request media
            that is on this playlist. Not needed if playlist's source is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``None``.
        :param play_per_value: (Optional) The new value for the
            ``ONCE_PER_X_SONGS``, ``ONCE_PER_X_HOURS`` and ``ONCE_PER_X_MINUTES`` playlist types.
            Not needed if playlist's source is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``None``.
        :param weight: (Optional) The new frequency of the playlist to be played when compared to
            other playlists. This is the value for the ``DEFAULT`` playlist type.
            Not needed if playlist's source is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``None``.
        :param include_in_on_demand: (Optional) Determines whether only songs that are in playlists
            with this setting enabled will be visible. Not needed if playlist's source is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``None``.
        :param is_jingle: (Optional) Determines if metadata will be sent to the AutoDJ for
            files in this playlist.
            Not needed if playlist's source is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``None``.
        :param remote_url: (Optional) The new source URL for the playlist's contents. Not needed if
            playlist's source is set to ``PlaylistSources.SONGS``. Default: ``None``.
        :param remote_type: (Optional) Specify the type of the ``remote_url``. Not needed if
            playlist's source is set to ``PlaylistSources.SONGS``. Default: ``None``.
        :param remote_buffer: (Optional) The new length of playback time that Liquidsoap should
            buffer when playing this remote playlist. Not needed if playlist's source is set to
            ``PlaylistSources.SONGS``. Default: ``None``.
        :param schedule: (Optional) The new structure representing the schedule list of the
            playlist. This can be generated using the :meth:`.generate_schedule_items` function.
            Default: ``None``.

            .. warning::

                This will overwrite the playlist's existing schedule.
                Use the :meth:`~.models.playlist.ScheduleHelper.add` and
                :meth:`~.models.playlist.ScheduleHelper.remove` methods to
                interact with the playlist's existing schedule.

        Usage:

        .. code-block:: python

            playlist.edit(
                name="New name lol",
                allow_requests=False,
                avoid_duplicates=False
            )
        """
        if type:
            if not isinstance(type, PlaylistTypes):
                raise ClientException(generate_enum_error_text("type", PlaylistTypes))

            type = type.value

        if source:
            if not isinstance(source, PlaylistSources):
                raise ClientException(generate_enum_error_text("source", PlaylistSources))

            source = source.value

        if order:
            if not isinstance(order, PlaylistOrders):
                raise ClientException(generate_enum_error_text("order", PlaylistOrders))

            order = order.value

        if remote_type:
            if not isinstance(remote_type, PlaylistRemoteTypes):
                raise ClientException(generate_enum_error_text("remote_type", PlaylistRemoteTypes))

            remote_type = remote_type.value

        return edit_station_resource(
            self, "station_playlist", name, source, type, order, avoid_duplicates, allow_requests,
            play_per_value, weight, include_in_on_demand, is_jingle, remote_url, remote_type,
            remote_buffer, schedule
        )

    def delete(self):
        """
        Deletes the playlist from the station.

        Sets all attributes of the current :class:`Playlist` object to ``None``.

        Usage:

        .. code-block:: python

            playlist.delete()
        """
        return delete_station_resource(self, "station_playlist")

    def _build_update_body(
        self,
        name,
        source,
        type,
        order,
        avoid_duplicates,
        allow_requests,
        play_per_value,
        weight,
        include_in_on_demand,
        is_jingle,
        remote_url,
        remote_type,
        remote_buffer,
        schedule
    ):
        return {
            "name": name or self.name,
            "type": type or self.type,
            "source": source or self.source,
            "order": order or self.order,
            "remote_url": remote_url or self.remote_url,
            "remote_type": remote_type or self.remote_type,
            "remote_buffer": remote_buffer or self.remote_buffer,
            "is_jingle": is_jingle if is_jingle is not None else self.is_jingle,
            "play_per_songs": play_per_value if type == "once_per_x_songs" else self.play_per_songs,
            "play_per_minutes": play_per_value if type == "once_per_x_minutes" else self.play_per_minutes,
            "play_per_hour_minute": play_per_value if type == "once_per_hour" else self.play_per_hour_minute,
            "weight": weight or self.weight,
            "include_in_requests": allow_requests if allow_requests is not None else self.include_in_requests,
            "include_in_on_demand": include_in_on_demand if include_in_on_demand is not None else self.include_in_on_demand,
            "avoid_duplicates": avoid_duplicates if avoid_duplicates is not None else self.avoid_duplicates,
            "schedule_items": schedule or [_get_schedule_item_json(item) for item in self.schedule_items]
        }

    def _update_properties(
        self,
        name,
        source,
        type,
        order,
        avoid_duplicates,
        allow_requests,
        play_per_value,
        weight,
        include_in_on_demand,
        is_jingle,
        remote_url,
        remote_type,
        remote_buffer,
        schedule
    ):
        self.name = name or self.name
        self.type = type or self.type
        self.source = source or self.source
        self.order = order or self.order
        self.remote_url = remote_url or self.remote_url
        self.remote_type = remote_type or self.remote_type
        self.remote_buffer = remote_buffer or self.remote_buffer
        self.is_jingle = is_jingle if is_jingle is not None else self.is_jingle
        self.play_per_songs = play_per_value if type == "once_per_x_songs" else self.play_per_songs
        self.play_per_minutes = play_per_value if type == "once_per_x_minutes" else self.play_per_minutes
        self.play_per_hour_minute = play_per_value if type == "once_per_hour" else self.play_per_hour_minute
        self.weight = weight or self.weight
        self.include_in_requests = allow_requests if allow_requests is not None else self.include_in_requests
        self.include_in_on_demand = include_in_on_demand if include_in_on_demand is not None else self.include_in_on_demand
        self.avoid_duplicates = avoid_duplicates if avoid_duplicates is not None else self.avoid_duplicates
        self.schedule_items = self.schedule_items if schedule is None else self._station.playlist(self.id).schedule_items # I'm sorry.

    def _clear_properties(self):
        self.name = None
        self.type = None
        self.source = None
        self.order = None
        self.remote_url = None
        self.remote_type = None
        self.remote_buffer = None
        self.is_enabled = None
        self.is_jingle = None
        self.play_per_songs = None
        self.play_per_minutes = None
        self.play_per_hour_minute = None
        self.weight = None
        self.include_in_requests = None
        self.include_in_on_demand = None
        self.backend_options = None
        self.avoid_duplicates = None
        self.played_at = None
        self.queue_reset_at = None
        self.schedule_items = None
        self.id = None
        self.short_name = None
        self.num_songs = None
        self.total_length = None
        self.links = None
        self._station = None
