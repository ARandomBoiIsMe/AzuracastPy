from .links import Links

class MountPoint:
    def __init__(
            self, name: str, display_name: str, is_visible_on_public_pages: bool, is_default: bool,
            is_public: bool, fallback_mount, relay_url: str, authhash: str, max_listener_duration: int,
            enable_autodj: bool, autodj_format: str, autodj_bitrate: int, custom_listen_url: str,
            intro_path: str, frontend_config, listeners_unique: int, listeners_total: int, id: int,
            links: Links
        ):
        self.name = name
        self.display_name = display_name
        self.is_visible_on_public_pages = is_visible_on_public_pages
        self.is_default = is_default
        self.is_public = is_public
        self.fallback_mount = fallback_mount
        self.relay_url = relay_url
        self.authhash = authhash
        self.max_listener_duration = max_listener_duration
        self.enable_autodj = enable_autodj
        self.autodj_format = autodj_format
        self.autodj_bitrate = autodj_bitrate
        self.custom_listen_url = custom_listen_url
        self.intro_path = intro_path
        self.frontend_config = frontend_config
        self.listeners_unique = listeners_unique
        self.listeners_total = listeners_total
        self.id = id
        self.links = links

    def __repr__(self):
        return (
            f"MountPoint(name={self.name!r}, display_name={self.display_name!r}, "
            f"is_visible_on_public_pages={self.is_visible_on_public_pages!r}, is_default={self.is_default!r}, "
            f"is_public={self.is_public!r}, relay_url={self.relay_url!r}, authhash={self.authhash!r}, "
            f"max_listener_duration={self.max_listener_duration!r}, enable_autodj={self.enable_autodj!r}, "
            f"autodj_format={self.autodj_format!r}, autodj_bitrate={self.autodj_bitrate!r}, "
            f"custom_listen_url={self.custom_listen_url!r}, intro_path={self.intro_path!r}, "
            f"listeners_unique={self.listeners_unique!r}, listeners_total={self.listeners_total!r}, id={self.id!r}, "
            f"links={self.links!r})"
        )
