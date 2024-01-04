from .listeners import Listeners

class Mount:
    def __init__(
            self, id: int, name: str, url: str, bitrate: int, format: str, path: str, is_default: bool,
            listeners: Listeners
        ):
        self.id = id
        self.name = name
        self.url = url
        self.bitrate = bitrate
        self.format = format
        self.listeners = listeners
        self.path = path
        self.is_default = is_default

    def __repr__(self):
        return (
            f"Mount(id={self.id}, name={self.name!r}, url={self.url!r}, bitrate={self.bitrate}, "
            f"format={self.format!r}, path={self.path!r}, is_default={self.is_default}, "
            f"listeners={self.listeners!r})"
        )