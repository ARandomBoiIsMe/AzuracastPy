from datetime import datetime
from typing import Any, Dict, List, Optional

from AzuracastPy.constants import API_ENDPOINTS

class Export:
    def __init__(self, pls: str, m3u: str):
        self.pls = pls
        self.m3u = m3u

    def __repr__(self):
        return f"Export(pls={self.pls!r}, m3u={self.m3u!r})"

class Links:
    def __init__(
        self, _self: str, toggle: str, clone: str, queue: str, _import: str, reshuffle: str,
        applyto: str, empty: str, export: Export
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

    def __repr__(self):
        return (
            f"Links(self={self._self!r}, toggle={self.toggle!r}, clone={self.clone!r}, "
            f"queue={self.queue!r}, import={self._import!r}, reshuffle={self.reshuffle!r}, "
            f"applyto={self.applyto!r}, empty={self.empty!r}, export={self.export!r})"
        )

    @classmethod
    def from_dict(cls, links_dict: Dict[str, Any]):
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
        self, start_time: int, end_time: int, start_date: str, end_date: str, days: List[int],
        loop_once: bool, id: int
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        self.days = days
        self.loop_once = loop_once
        self.id = id

    def __repr__(self):
        return (
            f"ScheduleItem(start_time={self.start_time!r}, end_time={self.end_time!r}, "
            f"start_date={self.start_date!r}, end_date={self.end_date!r}, "
            f"days={self.days!r}, loop_once={self.loop_once!r}, id={self.id!r})"
        )

class Playlist:
    def __init__(
        self, name: str, type:str, source: str, order: str, remote_url: str, remote_type: str,
        remote_buffer: int, is_enabled: bool, is_jingle: bool, play_per_songs: int, play_per_minutes: int,
        play_per_hour_minute: int, weight: int, include_in_requests: bool, include_in_on_demand: bool,
        backend_options: List[str], avoid_duplicates: bool, played_at: int, queue_reset_at: int,
        schedule_items: List[ScheduleItem], id: int, short_name: str, num_songs: int, total_length: int,
        links: Dict[str, Any], _station
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
        self.schedule_items = schedule_items
        self.id = id
        self.short_name = short_name
        self.num_songs = num_songs
        self.total_length = total_length
        self.links = Links.from_dict(links) if links else None
        self._station = _station

    def __repr__(self):
        return (
            f"Playlist(name={self.name!r}, type={self.type!r}, source={self.source!r}, "
            f"order={self.order!r}, remote_url={self.remote_url!r}, remote_type={self.remote_type!r}, "
            f"remote_buffer={self.remote_buffer!r}, is_enabled={self.is_enabled!r}, is_jingle={self.is_jingle!r}, "
            f"play_per_songs={self.play_per_songs!r}, play_per_minutes={self.play_per_minutes!r}, "
            f"play_per_hour_minute={self.play_per_hour_minute!r}, weight={self.weight!r}, "
            f"include_in_requests={self.include_in_requests!r}, include_in_on_demand={self.include_in_on_demand!r}, "
            f"backend_options={self.backend_options!r}, avoid_duplicates={self.avoid_duplicates!r}, "
            f"played_at={self.played_at!r}, queue_reset_at={self.queue_reset_at!r}, "
            f"schedule_items={self.schedule_items!r}, id={self.id!r}, short_name={self.short_name!r}, "
            f"num_songs={self.num_songs!r}, total_length={self.total_length!r}, "
            f"links={self.links!r})"
        )
    
    def edit(
        self, name: Optional[str] = None, type: Optional[str] = None, source: Optional[str] = None,
        order: Optional[str] = None, remote_url: Optional[str] = None, remote_type: Optional[str] = None,
        remote_buffer: Optional[int] = None, play_per_value: Optional[int] = None, weight: Optional[int] = None,
        include_in_requests: Optional[bool] = None, include_in_on_demand: Optional[bool] = None,
        avoid_duplicates: Optional[bool] = None, is_jingle: Optional[bool] = None
    ):
        old_playlist = self._station.playlist(self.id)

        url = API_ENDPOINTS["station_playlist"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(
            old_playlist, name, type, source, order, remote_url, remote_type, remote_buffer, is_jingle,
            play_per_value, weight, include_in_requests, include_in_on_demand, avoid_duplicates
        )

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_playlist, name, type, source, order, remote_url, remote_type, remote_buffer, is_jingle,
                play_per_value, weight, include_in_requests, include_in_on_demand, avoid_duplicates
            )

        return response
    
    def delete(self):
        url = API_ENDPOINTS["station_playlist"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _build_update_body(
        self, old_playlist: "Playlist", name, type, source, order, remote_url, remote_type, remote_buffer, is_jingle,
        play_per_value, weight, include_in_requests, include_in_on_demand, avoid_duplicates
    ):
        return {
            "name": name if name else old_playlist.name,
            "type": type if type else old_playlist.type,
            "source": source if source else old_playlist.source,
            "order": order if order else old_playlist.order,
            "remote_url": remote_url if remote_url else old_playlist.remote_url,
            "remote_type": remote_type if remote_type else old_playlist.remote_type,
            "remote_buffer": remote_buffer if remote_buffer else old_playlist.remote_buffer,
            "is_jingle": is_jingle if is_jingle is not None else old_playlist.is_jingle,
            "play_per_songs": play_per_value if type == "once_per_x_songs" else old_playlist.play_per_songs,
            "play_per_minutes": play_per_value if type == "once_per_x_minutes" else old_playlist.play_per_minutes,
            "play_per_hour_minute": play_per_value if type == "once_per_hour" else old_playlist.play_per_hour_minute,
            "weight": weight if weight is not None else old_playlist.weight,
            "include_in_requests": include_in_requests if include_in_requests is not None else old_playlist.include_in_requests,
            "include_in_on_demand": include_in_on_demand if include_in_on_demand is not None else old_playlist.include_in_on_demand,
            "avoid_duplicates": avoid_duplicates if avoid_duplicates is not None else old_playlist.avoid_duplicates
        }
    
    def _update_properties(
        self, old_playlist: "Playlist", name, type, source, order, remote_url, remote_type, remote_buffer, is_jingle,
        play_per_value, weight, include_in_requests, include_in_on_demand, avoid_duplicates
    ):
        self.name = name if name else old_playlist.name,
        self.type = type if type else old_playlist.type,
        self.source = source if source else old_playlist.source,
        self.order = order if order else old_playlist.order,
        self.remote_url = remote_url if remote_url else old_playlist.remote_url,
        self.remote_type = remote_type if remote_type else old_playlist.remote_type,
        self.remote_buffer = remote_buffer if remote_buffer else old_playlist.remote_buffer,
        self.is_jingle = is_jingle if is_jingle is not None else old_playlist.is_jingle,
        self.play_per_songs = play_per_value if type == "once_per_x_songs" else old_playlist.play_per_songs,
        self.play_per_minutes = play_per_value if type == "once_per_x_minutes" else old_playlist.play_per_minutes,
        self.play_per_hour_minute = play_per_value if type == "once_per_hour" else old_playlist.play_per_hour_minute,
        self.weight = weight if weight is not None else old_playlist.weight,
        self.include_in_requests = include_in_requests if include_in_requests is not None else old_playlist.include_in_requests,
        self.include_in_on_demand = include_in_on_demand if include_in_on_demand is not None else old_playlist.include_in_on_demand,
        self.avoid_duplicates = avoid_duplicates if avoid_duplicates is not None else old_playlist.avoid_duplicates

    def _clear_properties(self):
        self.name = None
        self.type = None
        self.source = None
        self.order = None
        self.remote_url = None
        self.remote_type = None
        self.remote_buffer = None
        self.is_jingle = None
        self.play_per_songs = None
        self.play_per_minutes = None
        self.play_per_hour_minute = None
        self.weight = None
        self.include_in_requests = None
        self.include_in_on_demand = None
        self.avoid_duplicates = None
        self._station = None