"""Class for encapsulating basic mount point info across objects."""

from ..util.general_util import generate_repr_string

from .listeners import Listeners

class Mount:
    "Represents basic info for station mount point."
    def __init__(
        self,
        id: int,
        name: str,
        url: str,
        bitrate: int,
        format: str,
        path: str,
        is_default: bool,
        listeners: Listeners
    ):
        """
        Initializes a :class:`Mount` object.

        .. note::

            This class should not be initialized directly. Instead, an instance will be made
            available as an attribute of other classes: :class:`~.models.Station` or
            :class:`~.models.administration.relay.Relay`.
        """
        self.id = id
        self.name = name
        self.url = url
        self.bitrate = bitrate
        self.format = format
        self.listeners = Listeners(**listeners)
        self.path = path
        self.is_default = is_default

    def __repr__(self):
        return generate_repr_string(self)
