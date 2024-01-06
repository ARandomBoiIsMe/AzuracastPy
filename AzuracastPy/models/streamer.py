from typing import List

class Streamer:
    def __init__(self, id: int, streamer_username: str, streamer_password: str, display_name: str, comments: str, is_active: bool, enforce_schedule: bool, reactivate_at: int, schedule_items: List[str]):
        self.id = id
        self.streamer_username = streamer_username
        self.streamer_password = streamer_password
        self.display_name = display_name
        self.comments = comments
        self.is_active = is_active
        self.enforce_schedule = enforce_schedule
        self.reactivate_at = reactivate_at
        self.schedule_items = schedule_items
    
    def __repr__(self):
        return (
            f"Streamer(id={self.id!r}, streamer_username={self.streamer_username!r}, "
            f"streamer_password={self.streamer_password!r}, display_name={self.display_name!r}, "
            f"comments={self.comments!r}, is_active={self.is_active!r}, "
            f"enforce_schedule={self.enforce_schedule!r}, reactivate_at={self.reactivate_at!r}, "
            f"schedule_items={self.schedule_items!r})"
        )