from typing import List, Optional
from datetime import datetime

from AzuracastPy.constants import API_ENDPOINTS

class Links:
    def __init__(self_, self: str, broadcasts: str, art: str):
        self_.self = self
        self_.broadcasts = broadcasts
        self_.art = art

    def __repr__(self):
        return f"Links(self={self.self!r}, broadcasts={self.broadcasts!r}, art={self.art!r})"

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
            f"start_date={self.start_date!r}, end_date={self.end_date!r}, days={self.days!r}, "
            f"loop_once={self.loop_once!r}, id={self.id!r})"
        )

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
        return (
            f"Streamer(id={self.id!r}, streamer_username={self.streamer_username!r}, "
            f"streamer_password={self.streamer_password!r}, display_name={self.display_name!r}, "
            f"comments={self.comments!r}, is_active={self.is_active!r}, "
            f"enforce_schedule={self.enforce_schedule!r}, reactivate_at={self.reactivate_at!r}, "
            f"art_updated_at={self.art_updated_at!r}, schedule_items={self.schedule_items!r}, "
            f"links={self.links!r}, has_custom_art={self.has_custom_art!r}, art={self.art!r})"
        )
    
    def edit(
        self, streamer_username: Optional[str] = None, display_name: Optional[str] = None,
        comments: Optional[str] = None, is_active: Optional[bool] = None, enforce_schedule: Optional[bool] = None
    ):
        old_streamer = self._station.streamer(self.id)

        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(
            old_streamer, streamer_username, display_name, comments, is_active,
            enforce_schedule
        )

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_streamer, streamer_username, display_name, comments, is_active,
                enforce_schedule
            )
            
        return response
    
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
        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _build_update_body(
        self, old_streamer: "Streamer", streamer_username, display_name, comments, is_active,
        enforce_schedule
    ):
        return {
            "streamer_username": streamer_username if streamer_username else old_streamer.streamer_username,
            "display_name": display_name if display_name else old_streamer.display_name,
            "comments": comments if comments else old_streamer.comments,
            "is_active": is_active if is_active is not None else old_streamer.is_active,
            "enforce_schedule": enforce_schedule if enforce_schedule is not None else old_streamer.enforce_schedule
        }
    
    def _update_properties(
        self, old_streamer: "Streamer", streamer_username, display_name, comments, is_active,
        enforce_schedule
    ):
        self.streamer_username = streamer_username if streamer_username else old_streamer.streamer_username
        self.display_name = display_name if display_name else old_streamer.display_name
        self.comments = comments if comments else old_streamer.comments
        self.is_active = is_active if is_active is not None else old_streamer.is_active
        self.enforce_schedule = enforce_schedule if enforce_schedule is not None else old_streamer.enforce_schedule

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