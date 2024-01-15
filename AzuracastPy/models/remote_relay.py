from typing import List, Optional

from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.constants import API_ENDPOINTS, BITRATES, HLS_FORMATS
from AzuracastPy.exceptions import ClientException
from AzuracastPy.models.util.station_resource_operations import delete_resource, edit_resource

class Links:
    def __init__(self_, self):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class RemoteRelay:
    def __init__(
        self, id: int, display_name: str, is_visible_on_public_pages: bool, type: str, is_editable: bool,
        enable_autodj: bool, autodj_format: str, autodj_bitrate: int, custom_listen_url: str, url: str, mount: str,
        admin_password: str, source_port: int, source_mount: str, source_username: str, source_password: str,
        is_public: bool, listeners_unique: int, listeners_total: int, links: Links, _station
    ):
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
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, station_listening_url: Optional[str] = None, remote_type: Optional[str] = None,
        display_name: Optional[str] = None, station_listening_mount_point: Optional[str] = None,
        station_admin_password: Optional[str] = None, show_on_public_pages: Optional[bool] = None,
        enable_autodj: Optional[bool] = None, autodj_format: Optional[str] = None,
        autodj_bitrate: Optional[int] = None, station_source_port: Optional[int] = None,
        station_source_mount_point: Optional[str] = None, station_source_username: Optional[str] = None,
        station_source_password: Optional[str] = None, is_public: Optional[bool] = None
    ):
        if remote_type is not None:
            if remote_type not in ["icecast", "shoutcast1", "shoutcast2"]:
                message = "remote_type param has to be one of: icecast, shoutcast1, shoutcast2"
                raise ClientException(message)
        
        if autodj_format is not None:
            if autodj_format not in HLS_FORMATS:
                message = f"autodj_format param must be one of: {', '.join(HLS_FORMATS)}"
                raise ClientException(message)
        
        if autodj_bitrate is not None:
            if autodj_bitrate not in BITRATES:
                message = f"autodj_bitrate param must be one of: {', '.join(BITRATES)}"
                raise ClientException(message)
            
        return edit_resource(
            self, "station_remote_relay_item",
            station_listening_url, remote_type, display_name, station_listening_mount_point, station_admin_password,
            show_on_public_pages, enable_autodj, autodj_format, autodj_bitrate, station_source_port,
            station_source_mount_point, station_source_username, station_source_password, is_public
        )
    
    def delete(self):
        return delete_resource(self, "station_remote_relay_item")
    
    def _build_update_body(
        self, station_listening_url, remote_type, display_name, station_listening_mount_point, station_admin_password,
        show_on_public_pages, enable_autodj, autodj_format, autodj_bitrate, station_source_port,
        station_source_mount_point, station_source_username, station_source_password, is_public
    ):
        return {
            "display_name": display_name if display_name else self.display_name,
            "is_visible_on_public_pages": show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages,
            "type": remote_type if remote_type else self.type,
            "enable_autodj": enable_autodj if enable_autodj is not None else self.enable_autodj,
            "autodj_format": autodj_format if autodj_format else self.autodj_format,
            "autodj_bitrate": autodj_bitrate if autodj_bitrate else self.autodj_bitrate,
            "url": station_listening_url if station_listening_url else self.url,
            "mount": station_listening_mount_point if station_listening_mount_point else self.mount,
            "admin_password": station_admin_password if station_admin_password else self.admin_password,
            "source_port": station_source_port if station_source_port else self.source_port,
            "source_mount": station_source_mount_point if station_source_mount_point else self.source_mount,
            "source_username": station_source_username if station_source_username else self.source_username,
            "source_password": station_source_password if station_source_password else self.source_password,
            "is_public": is_public if is_public is not None else self.is_public
        }
    
    def _update_properties(
        self, station_listening_url, remote_type, display_name, station_listening_mount_point, station_admin_password,
        show_on_public_pages, enable_autodj, autodj_format, autodj_bitrate, station_source_port,
        station_source_mount_point, station_source_username, station_source_password, is_public
    ):
        self.display_name = display_name if display_name else self.display_name
        self.is_visible_on_public_pages = show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages
        self.type = remote_type if remote_type else self.type
        self.enable_autodj = enable_autodj if enable_autodj is not None else self.enable_autodj
        self.autodj_format = autodj_format if autodj_format else self.autodj_format
        self.autodj_bitrate = autodj_bitrate if autodj_bitrate else self.autodj_bitrate
        self.url = station_listening_url if station_listening_url else self.url
        self.mount = station_listening_mount_point if station_listening_mount_point else self.mount
        self.admin_password = station_admin_password if station_admin_password else self.admin_password
        self.source_port = station_source_port if station_source_port else self.source_port
        self.source_mount = station_source_mount_point if station_source_mount_point else self.source_mount
        self.source_username = station_source_username if station_source_username else self.source_username
        self.source_password = station_source_password if station_source_password else self.source_password
        self.is_public = is_public if is_public is not None else self.is_public

    def _clear_properties(self):
        self.id = None
        self.display_name = None
        self.is_visible_on_public_pages = None
        self.type = None
        self.is_editable = None
        self.enable_autodj = None
        self.autodj_format = None
        self.autodj_bitrate = None
        self.custom_listen_url = None
        self.url = None
        self.mount = None
        self.admin_password = None
        self.source_port = None
        self.source_mount = None
        self.source_username = None
        self.source_password = None
        self.is_public = None
        self.listeners_unique = None
        self.listeners_total = None
        self.links = None
        self._station = None