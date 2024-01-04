from datetime import datetime

class ScheduleTime:
    def __init__(
            self, id: int, type: str, name: str, title: str, description: str, start_timestamp: int,
            start: str, end_timestamp: int, end: str, is_now: bool
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
        return (
            f"ScheduleTime(id={self.id!r}, type={self.type!r}, name={self.name!r}, title={self.title!r}, "
            f"description={self.description!r}, start_timestamp={self.start_timestamp}, "
            f"start={self.start!r}, end_timestamp={self.end_timestamp}, end={self.end!r}, is_now={self.is_now!r})"
        )