from .links import Links

from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.constants import API_ENDPOINTS
from .util.station_resource_operations import edit_resource, delete_resource

from typing import Optional, Dict, Any, Union

class MountPoint:
    def __init__(
        self, name: str, display_name: str, is_visible_on_public_pages: bool, is_default: bool,
        is_public: bool, fallback_mount, relay_url: str, authhash: str, max_listener_duration: int,
        enable_autodj: bool, autodj_format: str, autodj_bitrate: int, custom_listen_url: str,
        intro_path: str, frontend_config, listeners_unique: int, listeners_total: int, id: int,
        links: Links, _station
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
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, mount_point_url: Optional[str] = None, display_name: Optional[str] = None,
        show_on_public_pages: Optional[bool] = None, is_default: Optional[bool] = None,
        is_public: Optional[bool] = None, relay_stream_url: Optional[str] = None,
        max_listener_duration: Optional[int] = None, fallback_mount: Optional[str] = None,
        enable_autodj: Optional[bool] = None, autodj_format: Optional[str] = None,
        autodj_bitrate: Optional[int] = None, custom_url: Optional[str] = None,
        custom_frontend_config: Optional[Union[Dict[str, Any], str]] = None
    ):
        return edit_resource(
            self, "station_mount_point", mount_point_url, display_name, show_on_public_pages, is_default,
            is_public, relay_stream_url, max_listener_duration, fallback_mount, enable_autodj, autodj_format,
            autodj_bitrate, custom_url, custom_frontend_config
        )
    
    def delete(self):
        return delete_resource(self, "station_mount_point")
    
    def _build_update_body(
        self, mount_point_url, display_name, show_on_public_pages, is_default,
        is_public, relay_stream_url, max_listener_duration, fallback_mount, enable_autodj, autodj_format,
        autodj_bitrate, custom_url, custom_frontend_config
    ):
        return {
            "name": mount_point_url if mount_point_url else self.name,
            "display_name": display_name if display_name else self.display_name,
            "is_visible_on_public_pages": show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages,
            "is_default": is_default if is_default is not None else self.is_default,
            "is_public": is_public if is_public is not None else self.is_public,
            "fallback_mount": fallback_mount if fallback_mount else self.fallback_mount,
            "relay_url": relay_stream_url if relay_stream_url else self.relay_url,
            "max_listener_duration": max_listener_duration if max_listener_duration else self.max_listener_duration,
            "enable_autodj": enable_autodj if enable_autodj is not None else self.enable_autodj,
            "autodj_format": autodj_format if autodj_format else self.autodj_format,
            "autodj_bitrate": autodj_bitrate if autodj_bitrate else self.autodj_bitrate,
            "custom_listen_url": custom_url if custom_url else self.custom_listen_url,
            "frontend_config": custom_frontend_config if custom_frontend_config else self.frontend_config,
        }
    
    def _update_properties(
        self, mount_point_url, display_name, show_on_public_pages, is_default,
        is_public, relay_stream_url, max_listener_duration, fallback_mount, enable_autodj, autodj_format,
        autodj_bitrate, custom_url, custom_frontend_config
    ):
        self.name = mount_point_url if mount_point_url else self.name
        self.display_name = display_name if display_name else self.display_name
        self.is_visible_on_public_pages = show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages
        self.is_default = is_default if is_default is not None else self.is_default
        self.is_public = is_public if is_public is not None else self.is_public
        self.fallback_mount = fallback_mount if fallback_mount else self.fallback_mount
        self.relay_url = relay_stream_url if relay_stream_url else self.relay_url
        self.max_listener_duration = max_listener_duration if max_listener_duration else self.max_listener_duration
        self.enable_autodj = enable_autodj if enable_autodj is not None else self.enable_autodj
        self.autodj_format = autodj_format if autodj_format else self.autodj_format
        self.autodj_bitrate = autodj_bitrate if autodj_bitrate else self.autodj_bitrate
        self.custom_listen_url = custom_url if custom_url else self.custom_listen_url
        self.frontend_config = custom_frontend_config if custom_frontend_config else self.frontend_config

    def _clear_properties(self):
        self.name = None
        self.display_name = None
        self.is_visible_on_public_pages = None
        self.is_default = None
        self.is_public = None
        self.fallback_mount = None
        self.relay_url = None
        self.authhash = None
        self.max_listener_duration = None
        self.enable_autodj = None
        self.autodj_format = None
        self.autodj_bitrate = None
        self.custom_listen_url = None
        self.intro_path = None
        self.frontend_config = None
        self.listeners_unique = None
        self.listeners_total = None
        self.id = None
        self.links = None
        self._station = None