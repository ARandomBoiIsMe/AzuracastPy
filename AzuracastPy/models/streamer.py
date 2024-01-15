from typing import List, Optional
from datetime import datetime

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string
from .util.station_resource_operations import edit_resource, delete_resource

class Links:
    def __init__(self_, self: str, broadcasts: str, art: str):
        self_.self = self
        self_.broadcasts = broadcasts
        self_.art = art

    def __repr__(self):
        return generate_repr_string(self)

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
        return generate_repr_string(self)

class Streamer:
    def __init__(
        self, streamer_username: str, streamer_password: str, display_name: str, comments: str,
        is_active: bool, enforce_schedule: bool, reactivate_at: int, art_updated_at: int,
        schedule_items: List[ScheduleItem], id: int, links: Links, has_custom_art: bool,
        art: str, _station
    ):
        self.streamer_username = streamer_username
        self.streamer_password = streamer_password
        self.display_name = display_name
        self.comments = comments
        self.is_active = is_active
        self.enforce_schedule = enforce_schedule
        self.reactivate_at = reactivate_at
        self.art_updated_at = art_updated_at
        self.schedule_items = schedule_items
        self.id = id
        self.links = links
        self.has_custom_art = has_custom_art
        self.art = art
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self) 
    
    def edit(
        self, streamer_username: Optional[str] = None, display_name: Optional[str] = None,
        comments: Optional[str] = None, is_active: Optional[bool] = None, enforce_schedule: Optional[bool] = None
    ):
        return edit_resource(
            self, "station_streamer", streamer_username, display_name, comments, is_active,
            enforce_schedule
        )
    
    def update_password(self, password: str):
        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = {
            "streamer_password": password
        }

        response = self._station._request_handler.put(url, body)

        return response
    
    def delete(self):
        return delete_resource(self, "station_streamer")
    
    def _build_update_body(
        self, streamer_username, display_name, comments, is_active,
        enforce_schedule
    ):
        return {
            "streamer_username": streamer_username if streamer_username else self.streamer_username,
            "display_name": display_name if display_name else self.display_name,
            "comments": comments if comments else self.comments,
            "is_active": is_active if is_active is not None else self.is_active,
            "enforce_schedule": enforce_schedule if enforce_schedule is not None else self.enforce_schedule
        }
    
    def _update_properties(
        self, streamer_username, display_name, comments, is_active,
        enforce_schedule
    ):
        self.streamer_username = streamer_username if streamer_username else self.streamer_username
        self.display_name = display_name if display_name else self.display_name
        self.comments = comments if comments else self.comments
        self.is_active = is_active if is_active is not None else self.is_active
        self.enforce_schedule = enforce_schedule if enforce_schedule is not None else self.enforce_schedule

    def _clear_properties(self):
        self.streamer_username = None
        self.streamer_password = None
        self.display_name = None
        self.comments = None
        self.is_active = None
        self.enforce_schedule = None
        self.reactivate_at = None
        self.art_updated_at = None
        self.schedule_items = None
        self.id = None
        self.links = None
        self.has_custom_art = None
        self.art = None
        self._station = None