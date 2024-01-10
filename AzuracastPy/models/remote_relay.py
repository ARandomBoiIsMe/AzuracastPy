from typing import List

from AzuracastPy.util.general_util import generate_repr_string

class RemoteRelay:
    def __init__(
            self, links: List[str], id: int, display_name: str, is_visible_on_public_pages: bool,
            type: str, is_editable: bool, enable_autodj: bool, autodj_format: str, autodj_bitrate: int,
            custom_listen_url: str, url: str, mount: str, admin_password: str, source_port: int,
            source_mount: str, source_username: str, source_password: str, is_public: bool,
            listeners_unique: int, listeners_total: int
        ):
        self.links = links
        self.id = id
        self.display_name = display_name
        self.is_visible_on_public_pages = is_visible_on_public_pages
        self.type = type
        self.is_editable = is_editable
        self.enable_autodj = enable_autodj
        self.autodj_format = autodj_format
        self.autodj_bitrate = autodj_bitrate
        self.custom_listen_url = custom_listen_url
        self.url = url
        self.mount = mount
        self.admin_password = admin_password
        self.source_port = source_port
        self.source_mount = source_mount
        self.source_username = source_username
        self.source_password = source_password
        self.is_public = is_public
        self.listeners_unique = listeners_unique
        self.listeners_total = listeners_total

    def __repr__(self):
        return generate_repr_string(self)