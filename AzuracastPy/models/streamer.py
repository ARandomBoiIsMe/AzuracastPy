"""Class for a station streamer."""

from typing import List, Optional, Dict, Any

from datetime import datetime

from ..constants import API_ENDPOINTS
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string
from ..util.media_util import get_resource_art

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    """Represents the links associated with a streamer."""
    def __init__(
        self_,
        self: str,
        broadcasts: str,
        art: str
    ):
        """
        Initializes a :class:`Links` object for a streamer.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``streamer.links``.
        """
        self_.self = self
        self_.broadcasts = broadcasts
        self_.art = art

    def __repr__(self):
        return generate_repr_string(self)

class ScheduleItem:
    """Represents a single item in a streamer's schedule."""
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
        Initializes a :class:`ScheduleItem` for a streamer.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``streamer.schedule_items``.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        self.days = days
        self.loop_once = loop_once
        self.id = id

    def __repr__(self):
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
        "days": schedule_item.days
    }

class ScheduleHelper:
    """Provides functions for working with the schedule of a streamer."""
    def __init__(
        self,
        _streamer
    ):
        """
        Initializes a :class:`ScheduleHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``streamer.schedule``.
        """
        self._streamer = _streamer

    def add(
        self,
        *args: Dict[str, Any]
    ):
        """
        Adds one or more new schedule items to the streamer of the station.

        :param args: The new schedule item(s) to be added to the station.

        Usage:
        .. code-block:: python

            item = station.streamer.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"]
            )

            streamer.schedule.add(item)
        """
        schedule_items = [_get_schedule_item_json(item) for item in self._playlist.schedule_items]

        for arg in args:
            schedule_items.append(arg)

        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._streamer._station._request_handler.radio_url,
            station_id=self._streamer._station.id,
            id=self._streamer.id
        )

        body = {
            "schedule_items": schedule_items
        }

        response = self._streamer._station._request_handler.put(url, body)

        if response['success']:
            # Updates the streamer's properties on the object.
            # Inefficient, but can't think of a better way.
            self._streamer.schedule_items = self._streamer._station.streamer(self._streamer.id).schedule_items

        return response

    def remove(
        self,
        id: int
    ):
        """
        Removes a schedule item from the streamer's current schedule.

        :param id: The ID of the schedule item to be removed.

        Usage:
        .. code-block:: python

            streamer.schedule.remove(1)
        """
        item_exists_in_schedule = any(item.id == id for item in self._streamer.schedule_items)

        if not item_exists_in_schedule:
            message = f"No schedule item of id '{id}' exists in this streamer's current schedule."
            raise ClientException(message)

        schedule_items = [_get_schedule_item_json(item) for item in self._streamer.schedule_items if item.id != id]

        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._streamer._station._request_handler.radio_url,
            station_id=self._streamer._station.id,
            id=self._streamer.id
        )

        body = {
            "schedule_items": schedule_items
        }

        response = self._streamer._station._request_handler.put(url, body)

        if response['success']:
            # Updates the streamer's properties on the object.
            # Inefficient, but can't think of a better way.
            self._streamer.schedule_items = self._streamer._station.streamer(self._streamer.id).schedule_items

        return response

class Streamer:
    """Represents a streamer on a station."""
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
        """
        Initializes a :class:`Streamer` instance for a streamer.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``streamer.links``.
        """
        self.streamer_username = streamer_username
        self.streamer_password = streamer_password
        self.display_name = display_name
        self.comments = comments
        self.is_active = is_active
        self.enforce_schedule = enforce_schedule
        self.reactivate_at = reactivate_at
        self.art_updated_at = art_updated_at
        self.schedule_items = [ScheduleItem(**si) for si in schedule_items] if schedule_items else []
        self.id = id
        self.links = Links(**links)
        self.has_custom_art = has_custom_art
        self.art = art
        self._station = _station

        self.schedule = ScheduleHelper(_streamer=self)
        """
        An instance of :class:`.ScheduleHelper`.

        Provides the interface for working with this streamer's schedule.

        For example, to add an item to the schedule:

        .. code-block:: python

            item = station.streamer.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"]
            )

            streamer.schedule.add(item)

        To remove an item whose id is ``1`` from the schedule:

        .. code-block:: python

            streamer.schedule.remove(1)
        """

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        username: Optional[str] = None,
        display_name: Optional[str] = None,
        comments: Optional[str] = None,
        is_active: Optional[bool] = None,
        enforce_schedule: Optional[bool] = None,
        schedule: Optional[List[Dict[str, Any]]] = None
    ):
        """
        Edits the streamer's properties.

        Updates all edited attributes of the current :class:`Streamer` object.

        :param username: (Optional) The streamer's new username.
        :param display_name: (Optional) The streamer's new display_name. Default: ``None``.
        :param comments: (Optional) Updated internal notes or comments about the streamer.
            Default: ``None``.
        :param is_active: (Optional) Determines whether this streamer can log in and stream.
            Default: ``None``.
        :param enforce_schedule: (Optional) Determines whether this streamer will only be able to
            connect during their scheduled broadcast times. Default: ``None``.
        :param schedule: (Optional) The new structure representing the schedule list of the
            streamer. This can be generated using the :meth:`.generate_schedule_items` function.
            Note: This will overwrite the streamer's existing schedule.
                  Use the :meth:`.schedule.add` and :meth:`.schedule.remove` methods to
                  interact with the streamer's existing schedule.
            Default: ``None``.

        Usage:
        .. code-block:: python

            streamer.edit(
                username="New username",
                display_name="The name which is displayed"
            )
        """
        return edit_station_resource(
            self, "station_streamer", username, display_name, comments, is_active,
            enforce_schedule, schedule
        )

    def update_password(
        self,
        password: str
    ):
        """
        Updates the streamer's password.

        :param password: The streamer's new password.

        Usage:
        .. code-block:: python

            streamer.update_password(
                password="new password"
            )
        """
        url = API_ENDPOINTS["station_streamer"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self._station.id
        )

        body = {
            "streamer_password": password
        }

        response = self._station._request_handler.put(url, body)

        return response

    def delete(self):
        """
        Deletes the streamer from the station.

        Sets all attributes of the current :class:`Streamer` object to ``None``.

        Usage:
        .. code-block:: python

            streamer.delete()
        """
        return delete_station_resource(self, "station_streamer")

    def _build_update_body(
        self,
        username,
        display_name,
        comments,
        is_active,
        enforce_schedule,
        schedule
    ):
        return {
            "streamer_username": username or self.streamer_username,
            "display_name": display_name or self.display_name,
            "comments": comments or self.comments,
            "is_active": is_active if is_active is not None else self.is_active,
            "enforce_schedule": enforce_schedule if enforce_schedule is not None else self.enforce_schedule,
            "schedule_items": schedule or [_get_schedule_item_json(item) for item in self.schedule_items]
        }

    def _update_properties(
        self,
        username,
        display_name,
        comments,
        is_active,
        enforce_schedule,
        schedule
    ):
        self.streamer_username = username or self.streamer_username
        self.display_name = display_name or self.display_name
        self.comments = comments or self.comments
        self.is_active = is_active if is_active is not None else self.is_active
        self.enforce_schedule = enforce_schedule if enforce_schedule is not None else self.enforce_schedule
        self.schedule_items = self.schedule_items if not schedule else self._station.streamer(self.id).schedule_items # I'm sorry.

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

    def get_art(self) -> bytes:
        return get_resource_art(self)
