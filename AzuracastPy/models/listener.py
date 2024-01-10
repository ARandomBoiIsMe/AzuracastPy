from AzuracastPy.util.general_util import generate_repr_string

class Device:
    def __init__(
            self, client: str, is_browser: bool, is_mobile: bool, is_bot: bool, browser_family: str,
            os_family: str
        ):
        self.client = client
        self.is_browser = is_browser
        self.is_mobile = is_mobile
        self.is_bot = is_bot
        self.browser_family = browser_family
        self.os_family = os_family

    def __repr__(self):
        return generate_repr_string(self)

class Location:
    def __init__(self, description: str, region: str, city: str, country: str, lat, lon):
        self.description = description
        self.region = region
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return generate_repr_string(self)

class Listener:
    def __init__(
            self, ip: str, user_agent: str, hash: str, mount_is_local: bool, mount_name: str,
            connected_on: int, connected_until: int, connected_time: int,
            device: Device, location: Location
        ):
        self.ip = ip
        self.user_agent = user_agent
        self.hash = hash
        self.mount_is_local = mount_is_local
        self.mount_name = mount_name
        self.connected_on = connected_on
        self.connected_until = connected_until
        self.connected_time = connected_time
        self.device = device
        self.location = location

    def __repr__(self):
        return generate_repr_string(self)