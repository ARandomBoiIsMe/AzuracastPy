"""Class for a station remote relay."""

from typing import Optional

from ..util.general_util import generate_repr_string, generate_enum_error_text
from ..enums import RemoteTypes, Bitrates, Formats
from ..exceptions import ClientException
from ..models.util.station_resource_operations import delete_station_resource, edit_station_resource

class Links:
    """Represents the links associated with a remote relay."""
    def __init__(
        self_,
        self
    ):
        """
        Initializes a :class:`Links` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``remote_relay.links``.
        """
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class RemoteRelay:
    """Represents a remote relay on a station."""
    def __init__(
        self,
        id: int,
        display_name: str,
        is_visible_on_public_pages: bool,
        type: str,
        is_editable: bool,
        enable_autodj: bool,
        autodj_format: str,
        autodj_bitrate: int,
        custom_listen_url: str,
        url: str,
        mount: str,
        admin_password: str,
        source_port: int,
        source_mount: str,
        source_username: str,
        source_password: str,
        is_public: bool,
        listeners_unique: int,
        listeners_total: int,
        links: Links,
        _station
    ):
        """
        Initializes a :class:`RemoteRelay` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.remote_relay.create()``, ``station.remote_relay(id)`` or
            ``station.remote_relays()``.
        """
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
        self.links = Links(**links)
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        station_listening_url: Optional[str] = None,
        remote_type: Optional[RemoteTypes] = None,
        display_name: Optional[str] = None,
        station_listening_mount_point: Optional[str] = None,
        station_admin_password: Optional[str] = None,
        show_on_public_pages: Optional[bool] = None,
        enable_autodj: Optional[bool] = None,
        autodj_format: Optional[Formats] = None,
        autodj_bitrate: Optional[Bitrates] = None,
        station_source_port: Optional[int] = None,
        station_source_mount_point: Optional[str] = None,
        station_source_username: Optional[str] = None,
        station_source_password: Optional[str] = None,
        is_public: Optional[bool] = None
    ):
        """
        Edits the remote relay's properties.

        Updates all edited attributes of the current :class:`RemoteRelay` object.

        :param station_listening_url: (Optional) The new URL of the listening station.
            Default: ``None``.
        :param remote_type: (Optional) The new type of the remote station. Default: ``None``.
        :param display_name: (Optional) The new display name of this relay when viewing it on
            administrative or public pages. Default: ``None``.
        :param station_listening_mount_point: (Optional)
        :param station_admin_password: (Optional) The new admin password. Default: ``None``.
        :param show_on_public_pages: (Optional) Determines whether listeners can select this
            relay on this station's public pages. Default: ``None``.
        :param enable_autodj: (Optional) Determines whether the AutoDJ on this installation will
            automatically play music to this mount point. Default: ``None``.
        :param autodj_format: (Optional) The format of the music played by AutoDJ.
            Default: ``None``.
        :param autodj_bitrate: (Optional) The bitrate of the music played by AutoDJ.
            Default: ``None``.
        :param station_source_port: (Optional)
        :param station_source_mount_point: (Optional)
        :param station_source_username: (Optional) If you are broadcasting using AutoDJ, enter the
            source username here. This may be blank. Default: ``None``.
        :param station_source_password: (Optional) If you are broadcasting using AutoDJ, enter the
            source password here. Default: ``None``.
        :param is_public: (Optional) Determines whether this relay will be advertised on
            "Yellow Pages" public radio directories. Default: ``None``.

        Usage:
        .. code-block:: python

            remote_relay.edit(
                display_name="New display name",
                enable_autodj=False
            )
        """
        if remote_type:
            if not isinstance(remote_type, RemoteTypes):
                raise ClientException(generate_enum_error_text("remote_type", RemoteTypes))

            remote_type = remote_type.value

        if autodj_format:
            if not isinstance(autodj_format, Formats):
                raise ClientException(generate_enum_error_text("autodj_format", Formats))

            autodj_format = autodj_format.value

        if autodj_bitrate:
            if not isinstance(autodj_bitrate, Bitrates):
                raise ClientException(generate_enum_error_text("autodj_bitrate", Bitrates))

            autodj_bitrate = autodj_bitrate.value

        return edit_station_resource(
            self, "station_remote_relay_item",
            station_listening_url, remote_type, display_name, station_listening_mount_point,
            station_admin_password, show_on_public_pages, enable_autodj, autodj_format,
            autodj_bitrate, station_source_port, station_source_mount_point,
            station_source_username, station_source_password, is_public
        )

    def delete(self):
        """
        Deletes the remote relay from the station.

        Sets all attributes of the current :class:`RemoteRelay` object to ``None``.

        Usage:
        .. code-block:: python

            remote_relay.delete()
        """
        return delete_station_resource(self, "station_remote_relay_item")

    def _build_update_body(
        self,
        station_listening_url,
        remote_type,
        display_name,
        station_listening_mount_point,
        station_admin_password,
        show_on_public_pages,
        enable_autodj,
        autodj_format,
        autodj_bitrate,
        station_source_port,
        station_source_mount_point,
        station_source_username,
        station_source_password,
        is_public
    ):
        return {
            "display_name": display_name or self.display_name,
            "is_visible_on_public_pages": show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages,
            "type": remote_type or self.type,
            "enable_autodj": enable_autodj if enable_autodj is not None else self.enable_autodj,
            "autodj_format": autodj_format or self.autodj_format,
            "autodj_bitrate": autodj_bitrate or self.autodj_bitrate,
            "url": station_listening_url or self.url,
            "mount": station_listening_mount_point or self.mount,
            "admin_password": station_admin_password or self.admin_password,
            "source_port": station_source_port or self.source_port,
            "source_mount": station_source_mount_point or self.source_mount,
            "source_username": station_source_username or self.source_username,
            "source_password": station_source_password or self.source_password,
            "is_public": is_public if is_public is not None else self.is_public
        }

    def _update_properties(
        self,
        station_listening_url,
        remote_type,
        display_name,
        station_listening_mount_point,
        station_admin_password,
        show_on_public_pages,
        enable_autodj,
        autodj_format,
        autodj_bitrate,
        station_source_port,
        station_source_mount_point,
        station_source_username,
        station_source_password,
        is_public
    ):
        self.display_name = display_name or self.display_name
        self.is_visible_on_public_pages = show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages
        self.type = remote_type or self.type
        self.enable_autodj = enable_autodj if enable_autodj is not None else self.enable_autodj
        self.autodj_format = autodj_format or self.autodj_format
        self.autodj_bitrate = autodj_bitrate or self.autodj_bitrate
        self.url = station_listening_url or self.url
        self.mount = station_listening_mount_point or self.mount
        self.admin_password = station_admin_password or self.admin_password
        self.source_port = station_source_port or self.source_port
        self.source_mount = station_source_mount_point or self.source_mount
        self.source_username = station_source_username or self.source_username
        self.source_password = station_source_password or self.source_password
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
