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
        return (
            f"Device(client={self.client!r}, is_browser={self.is_browser}, is_mobile={self.is_mobile}, "
            f"is_bot={self.is_bot}, browser_family={self.browser_family!r}, os_family={self.os_family!r})"
        )

class Location:
    def __init__(self, description: str, region: str, city: str, country: str, lat, lon):
        self.description = description
        self.region = region
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return (
            f"Location(description={self.description!r}, region={self.region!r}, city={self.city!r}, "
            f"country={self.country!r}, lat={self.lat}, lon={self.lon})"
        )

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
        return (
            f"Listener(ip={self.ip!r}, user_agent={self.user_agent!r}, hash={self.hash!r}, "
            f"mount_is_local={self.mount_is_local}, mount_name={self.mount_name!r}, "
            f"connected_on={self.connected_on}, connected_until={self.connected_until}, "
            f"connected_time={self.connected_time}, device={self.device!r}, location={self.location!r})"
        )