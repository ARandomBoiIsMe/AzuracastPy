from datetime import datetime
from typing import Any, Dict, List, Optional

from AzuracastPy.util.general_util import generate_repr_string

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Export:
    def __init__(
        self, 
        pls: str, 
        m3u: str
    ):
        self.pls = pls
        self.m3u = m3u

    def __repr__(self) -> str:
        return generate_repr_string(self)

class Links:
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
        self._self = _self
        self.toggle = toggle
        self.clone = clone
        self.queue = queue
        self._import = _import
        self.reshuffle = reshuffle
        self.applyto = applyto
        self.empty = empty
        self.export = export

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
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        self.days = days
        self.loop_once = loop_once
        self.id = id

    def __repr__(self) -> str:
        return generate_repr_string(self)

class Playlist:
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

    def __repr__(self) -> str:
        return generate_repr_string(self)
    
    def edit(
        self, 
        name: Optional[str] = None, 
        type: Optional[str] = None, 
        source: Optional[str] = None,
        order: Optional[str] = None, 
        remote_url: Optional[str] = None, 
        remote_type: Optional[str] = None,
        remote_buffer: Optional[int] = None, 
        play_per_value: Optional[int] = None, 
        weight: Optional[int] = None,
        include_in_requests: Optional[bool] = None, 
        include_in_on_demand: Optional[bool] = None,
        avoid_duplicates: Optional[bool] = None, 
        is_jingle: Optional[bool] = None
    ):
        """
        Edits the playlist's properties.

        :param name:
        :param type:
        :param source:
        :param order:
        :param remote_url:
        :param remote_type:
        :param remote_buffer:
        :param play_per_value:
        :param weight:
        :param include_in_requests:
        :param include_in_on_demand:
        :param avoid_duplicates:
        :param is_jingle:
        """
        return edit_station_resource(
            self, "station_playlist", name, type, source, order, remote_url, remote_type, remote_buffer,
            is_jingle, play_per_value, weight, include_in_requests, include_in_on_demand, avoid_duplicates
        )
    
    def delete(self):
        """
        Deletes the playlist from the station.
        """
        return delete_station_resource(self, "station_playlist")
    
    def _build_update_body(
        self, 
        name, 
        type, 
        source, 
        order, 
        remote_url, 
        remote_type, 
        remote_buffer, 
        is_jingle,
        play_per_value, 
        weight, 
        include_in_requests, 
        include_in_on_demand, 
        avoid_duplicates
    ):
        return {
            "name": name if name else self.name,
            "type": type if type else self.type,
            "source": source if source else self.source,
            "order": order if order else self.order,
            "remote_url": remote_url if remote_url else self.remote_url,
            "remote_type": remote_type if remote_type else self.remote_type,
            "remote_buffer": remote_buffer if remote_buffer else self.remote_buffer,
            "is_jingle": is_jingle if is_jingle is not None else self.is_jingle,
            "play_per_songs": play_per_value if type == "once_per_x_songs" else self.play_per_songs,
            "play_per_minutes": play_per_value if type == "once_per_x_minutes" else self.play_per_minutes,
            "play_per_hour_minute": play_per_value if type == "once_per_hour" else self.play_per_hour_minute,
            "weight": weight if weight is not None else self.weight,
            "include_in_requests": include_in_requests if include_in_requests is not None else self.include_in_requests,
            "include_in_on_demand": include_in_on_demand if include_in_on_demand is not None else self.include_in_on_demand,
            "avoid_duplicates": avoid_duplicates if avoid_duplicates is not None else self.avoid_duplicates
        }
    
    def _update_properties(
        self, 
        name, 
        type, 
        source, 
        order, 
        remote_url, 
        remote_type, 
        remote_buffer, 
        is_jingle,
        play_per_value, 
        weight, 
        include_in_requests, 
        include_in_on_demand, 
        avoid_duplicates
    ):
        self.name = name if name else self.name
        self.type = type if type else self.type
        self.source = source if source else self.source
        self.order = order if order else self.order
        self.remote_url = remote_url if remote_url else self.remote_url
        self.remote_type = remote_type if remote_type else self.remote_type
        self.remote_buffer = remote_buffer if remote_buffer else self.remote_buffer
        self.is_jingle = is_jingle if is_jingle is not None else self.is_jingle
        self.play_per_songs = play_per_value if type == "once_per_x_songs" else self.play_per_songs
        self.play_per_minutes = play_per_value if type == "once_per_x_minutes" else self.play_per_minutes
        self.play_per_hour_minute = play_per_value if type == "once_per_hour" else self.play_per_hour_minute
        self.weight = weight if weight is not None else self.weight
        self.include_in_requests = include_in_requests if include_in_requests is not None else self.include_in_requests
        self.include_in_on_demand = include_in_on_demand if include_in_on_demand is not None else self.include_in_on_demand
        self.avoid_duplicates = avoid_duplicates if avoid_duplicates is not None else self.avoid_duplicates

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