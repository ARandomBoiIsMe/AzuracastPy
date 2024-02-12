"""Class for a listener of a station."""

from ..util.general_util import generate_repr_string

class Device:
    """Represents the device of a listener."""
    def __init__(
        self,
        client: str,
        is_browser: bool,
        is_mobile: bool,
        is_bot: bool,
        browser_family: str,
        os_family: str
    ):
        """
        Initializes a :class:`Device` object for a :class:`Listener` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``listener.device``.
        """
        self.client = client
        self.is_browser = is_browser
        self.is_mobile = is_mobile
        self.is_bot = is_bot
        self.browser_family = browser_family
        self.os_family = os_family

    def __repr__(self):
        return generate_repr_string(self)

class Location:
    """Represents the location of a listener."""
    def __init__(
        self,
        description: str,
        region: str,
        city: str,
        country: str,
        lat,
        lon
    ):
        """
        Initializes a :class:`Location` object for a :class:`Listener` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``listener.location``.
        """
        self.description = description
        self.region = region
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return generate_repr_string(self)

class Listener:
    """Represents a single listener on a station."""
    def __init__(
        self,
        ip: str,
        user_agent: str,
        hash: str,
        mount_is_local: bool,
        mount_name: str,
        connected_on: int,
        connected_until: int,
        connected_time: int,
        device: Device,
        location: Location
    ):
        """
        Initializes a :class:`Listener` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.listeners()``.
        """
        self.ip = ip
        self.user_agent = user_agent
        self.hash = hash
        self.mount_is_local = mount_is_local
        self.mount_name = mount_name
        self.connected_on = connected_on
        self.connected_until = connected_until
        self.connected_time = connected_time
        self.device = Device(**device)
        self.location = Location(**location)

    def __repr__(self):
        return generate_repr_string(self)
