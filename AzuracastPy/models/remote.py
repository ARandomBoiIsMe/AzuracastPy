from .listeners import Listeners

class Remote:
    def __init__(self, id: int, name: str, url: str, bitrate: int, format: str, listeners: Listeners):
        self.id = id
        self.name = name
        self.url = url
        self.bitrate = bitrate
        self.format = format
        self.listeners = listeners

    def __repr__(self):
        return (
            f"Remote(id={self.id}, name={self.name!r}, url={self.url!r}, bitrate={self.bitrate}, "
            f"format={self.format!r}, listeners={self.listeners!r})"
        )