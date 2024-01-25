from typing import List, Optional, Dict, Any

from datetime import datetime

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.util.media_util import get_resource_art

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_, 
        self: str, 
        broadcasts: str, art: str
    ):
        self_.self = self
        self_.broadcasts = broadcasts
        self_.art = art

    def __repr__(self):
        return generate_repr_string(self)

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

    def __repr__(self):
        return generate_repr_string(self)

class Streamer:
    def __init__(
        self, 
        streamer_username: str, 
        streamer_password: str, 
        display_name: str, 
        comments: str,
        is_active: bool, 
        enforce_schedule: bool, 
        reactivate_at: int, 
        art_updated_at: int,
        schedule_items: List[ScheduleItem], 
        id: int, 
        links: Links, 
        has_custom_art: bool,
        art: str, 
        _station
    ):
        self.streamer_username = streamer_username
        self.streamer_password = streamer_password
        self.display_name = display_name
        self.comments = comments
        self.is_active = is_active
        self.enforce_schedule = enforce_schedule
        self.reactivate_at = reactivate_at
        self.art_updated_at = art_updated_at
        self.schedule_items = [ScheduleItem(**item) for item in schedule_items] if schedule_items else []
        self.id = id
        self.links = links
        self.has_custom_art = has_custom_art
        self.art = art
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, 
        streamer_username: Optional[str] = None, 
        display_name: Optional[str] = None,
        comments: Optional[str] = None, 
        is_active: Optional[bool] = None,
        enforce_schedule: Optional[bool] = None,
        schedule: Optional[List[Dict[str, Any]]] = None
    ):
        """
        Edits the streamer's properties.

        :param streamer_username:
        :param display_name:
        :param comments:
        :param is_active:
        :param enforce_schedule:
        :param schedule:
        """
        return edit_station_resource(
            self, "station_streamer", streamer_username, display_name, comments, is_active,
            enforce_schedule, schedule
        )
    
    def add_schedule_item(
        self,
        schedule_item: Dict[str, Any]
    ):
        """
        Adds a new schedule item to the streamer of the station.

        :param schedule_item: The new schedule item to be added.
        """
        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        # Adds the new schedule item.
        schedule_items = [self._get_schedule_item_json(item) for item in self.schedule_items]
        schedule_items.append(schedule_item)
        body = {
            "schedule_items": schedule_items
        }

        response = self._station._request_handler.put(url, body)

        # Updates the streamer's properties on the object.
        # Inefficient, but can't think of a better way.
        self.schedule_items = self._station.streamer(self.id).schedule_items

        return response

    def update_password(
        self, 
        password: str
    ):
        """
        Updates the streamer's password.

        :param password: The streamer's new password.
        """
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
        """
        Deletes the streamer from the station.
        """
        return delete_station_resource(self, "station_streamer")
    
    def _build_update_body(
        self, 
        streamer_username, 
        display_name, 
        comments, 
        is_active,
        enforce_schedule,
        schedule
    ):
        return {
            "streamer_username": streamer_username if streamer_username else self.streamer_username,
            "display_name": display_name if display_name else self.display_name,
            "comments": comments if comments else self.comments,
            "is_active": is_active if is_active is not None else self.is_active,
            "enforce_schedule": enforce_schedule if enforce_schedule is not None else self.enforce_schedule,
            "schedule_items": schedule if schedule else [self._get_schedule_item_json(item) for item in self.schedule_items]
        }
    
    def _update_properties(
        self, 
        streamer_username, 
        display_name, 
        comments, 
        is_active,
        enforce_schedule,
        schedule
    ):
        self.streamer_username = streamer_username if streamer_username else self.streamer_username
        self.display_name = display_name if display_name else self.display_name
        self.comments = comments if comments else self.comments
        self.is_active = is_active if is_active is not None else self.is_active
        self.enforce_schedule = enforce_schedule if enforce_schedule is not None else self.enforce_schedule
        self.schedule_items = self.schedule_items if schedule is None else self._station.streamer(self.id).schedule_items # I'm sorry.

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

    # Reformats the schedule item of a streamer from a ScheduleItem to a valid schedule item json
    # object to be sent in requests.
    def _get_schedule_item_json(self, schedule_item):
        if schedule_item is None:
            return {}

        start_date_formatted = schedule_item.start_date.strftime("%Y-%m-%d") if schedule_item.start_date else None
        end_date_formatted = schedule_item.end_date.strftime("%Y-%m-%d") if schedule_item.end_date else None

        return {
            "start_time": schedule_item.start_time,
            "end_time": schedule_item.end_time,
            "start_date": start_date_formatted,
            "end_date": end_date_formatted,
            "days": schedule_item.days
        }

    def get_art(self) -> bytes:
        return get_resource_art(self)