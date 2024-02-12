"""Class for encapsulating basic remote relay info across objects."""

from ..util.general_util import generate_repr_string

from .listeners import Listeners

class Remote:
    def __init__(
        self,
        id: int,
        name: str,
        url: str,
        bitrate: int,
        format: str,
        listeners: Listeners
    ):
        self.id = id
        self.name = name
        self.url = url
        self.bitrate = bitrate
        self.format = format
        self.listeners = Listeners(**listeners)

    def __repr__(self):
        return generate_repr_string(self)
