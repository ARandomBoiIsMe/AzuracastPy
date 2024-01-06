from typing import List

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
        return (
            f"RemoteRelay(links={self.links!r}, id={self.id!r}, display_name={self.display_name!r}, "
            f"is_visible_on_public_pages={self.is_visible_on_public_pages}, type={self.type!r}, "
            f"is_editable={self.is_editable}, enable_autodj={self.enable_autodj}, "
            f"autodj_format={self.autodj_format!r}, autodj_bitrate={self.autodj_bitrate!r}, "
            f"custom_listen_url={self.custom_listen_url!r}, url={self.url!r}, mount={self.mount!r}, "
            f"admin_password={self.admin_password!r}, source_port={self.source_port!r}, "
            f"source_mount={self.source_mount!r}, source_username={self.source_username!r}, "
            f"source_password={self.source_password!r}, is_public={self.is_public}, "
            f"listeners_unique={self.listeners_unique!r}, listeners_total={self.listeners_total!r})"
        )