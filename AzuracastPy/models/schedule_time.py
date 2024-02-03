"""Class for the schedule of a station."""

from datetime import datetime

from ..util.general_util import generate_repr_string

class ScheduleTime:
    def __init__(
        self,
        id: int,
        type: str,
        name: str,
        title: str,
        description: str,
        start_timestamp: int,
        start: str,
        end_timestamp: int,
        end: str,
        is_now: bool
    ):
        self.id = id
        self.type = type
        self.name = name
        self.title = title
        self.description = description
        self.start_timestamp = start_timestamp
        self.start = datetime.fromisoformat(start) if start else None
        self.end_timestamp = end_timestamp
        self.end = datetime.fromisoformat(end) if end else None
        self.is_now = is_now

    def __repr__(self):
        return generate_repr_string(self)
