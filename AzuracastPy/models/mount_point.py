"""Class for a station mount point."""

from typing import Optional, Dict, Any, Union

from ..util.general_util import generate_repr_string, generate_enum_error_text
from ..enums import Formats, Bitrates
from ..exceptions import ClientException

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_,
        self: str,
        intro: str,
        listen: str
    ):
        self_.self = self
        self_.intro = intro
        self_.listen = listen

    def __repr__(self):
        return generate_repr_string(self)

class MountPoint:
    def __init__(
        self,
        name: str,
        display_name: str,
        is_visible_on_public_pages: bool,
        is_default: bool,
        is_public: bool,
        fallback_mount,
        relay_url: str,
        authhash: str,
        max_listener_duration: int,
        enable_autodj: bool,
        autodj_format: str,
        autodj_bitrate: int,
        custom_listen_url: str,
        intro_path: str,
        frontend_config,
        listeners_unique: int,
        listeners_total: int,
        id: int,
        links: Links,
        _station
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
        self,
        mount_point_url: Optional[str] = None,
        display_name: Optional[str] = None,
        show_on_public_pages: Optional[bool] = None,
        is_default: Optional[bool] = None,
        is_public: Optional[bool] = None,
        relay_stream_url: Optional[str] = None,
        max_listener_duration: Optional[int] = None,
        fallback_mount: Optional[str] = None,
        enable_autodj: Optional[bool] = None,
        autodj_format: Optional[Formats] = None,
        autodj_bitrate: Optional[Bitrates] = None,
        custom_url: Optional[str] = None,
        custom_frontend_config: Optional[Union[Dict[str, Any], str]] = None
    ):
        """
        Edits the mount point's properties.

        Updates all edited attributes of the current :class:`MountPoint` object.

        :param mount_point_url: (Optional) The new URL assigned to the mount point.
            Must be a valid URL, such as ``"/autodj.mp3"``. Default: ``None``.
        :param display_name: (Optional) The new display name assigned to this mount point when
            viewing it on administrative or public pages. Default: ``None``.
        :param show_on_public_pages: (Optional) Determines whether listeners are allowed to select
            this mount point on this station's public pages. Default: ``None``.
        :param is_default: (Optional) Determines whether this mount will be played on the radio
            preview and the public radio page in this system. Default: ``None``.
        :param is_public: (Optional) Determines whether this mount will be advertised on
            "Yellow Pages" public radio directories. Default: ``None``.
        :param relay_stream_url: (Optional) The new full URL of another stream to relay its
            broadcast through this mount point. Default: ``None``.
        :param max_listener_duration: (Optional) The length of time (seconds) a listener will stay
            connected to the stream. Set to ``0`` to let listeners stay connected infinitely.
            Default: ``None``.
        :param fallback_mount: (Optional) The new mount point users will be redirected to if this
            mount point is not playing audio. Default: ``None``.
        :param enable_autodj: (Optional) Determines whether the AutoDJ will automatically play
            music to this mount point. Default: ``None``.
        :param autodj_format: (Optional) The new format of the audio AutoDJ will play on this
            mount point. Default: ``None``.
        :param autodj_bitrate: (Optional) The new bitrate of the audio AutoDJ will play on this
            mount point. Default: ``None``.
        :param custom_url: (Optional) The new custom URL for this stream that AzuraCast will use
            when referring to it. Default: ``None``.
        :param custom_frontend_config: (Optional) New special mount point settings, in either
            JSON { key: 'value' } format or XML <key>value</key>. Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import Formats, Bitrates

            station.mount_point(1).edit(
                display_name="New display name",
                enable_autodj=True,
                autodj_format=Formats.OPUS,
                autodj_bitrate=Bitrates.BITRATE_32
            )
        """
        if autodj_format:
            if not isinstance(autodj_format, Formats):
                raise ClientException(generate_enum_error_text("autodj_format", Formats))

            autodj_format = autodj_format.value

        if autodj_bitrate:
            if not isinstance(autodj_bitrate, Bitrates):
                raise ClientException(generate_enum_error_text("autodj_bitrate", Bitrates))

            autodj_bitrate = autodj_bitrate.value

        return edit_station_resource(
            self, "station_mount_point", mount_point_url, display_name, show_on_public_pages,
            is_default, is_public, relay_stream_url, max_listener_duration, fallback_mount,
            enable_autodj, autodj_format, autodj_bitrate, custom_url, custom_frontend_config
        )

    def delete(self):
        """
        Deletes the mount point from the station.

        Sets all attributes of the current :class:`MountPoint` object to ``None``.

        Usage:
        .. code-block:: python

            station.mount_point(1).delete()
        """
        return delete_station_resource(self, "station_mount_point")

    def _build_update_body(
        self,
        mount_point_url,
        display_name,
        show_on_public_pages,
        is_default,
        is_public,
        relay_stream_url,
        max_listener_duration,
        fallback_mount,
        enable_autodj,
        autodj_format,
        autodj_bitrate,
        custom_url,
        custom_frontend_config
    ):
        return {
            "name": mount_point_url or self.name,
            "display_name": display_name or self.display_name,
            "is_visible_on_public_pages": show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages,
            "is_default": is_default if is_default is not None else self.is_default,
            "is_public": is_public if is_public is not None else self.is_public,
            "fallback_mount": fallback_mount or self.fallback_mount,
            "relay_url": relay_stream_url or self.relay_url,
            "max_listener_duration": max_listener_duration or self.max_listener_duration,
            "enable_autodj": enable_autodj if enable_autodj is not None else self.enable_autodj,
            "autodj_format": autodj_format or self.autodj_format,
            "autodj_bitrate": autodj_bitrate or self.autodj_bitrate,
            "custom_listen_url": custom_url or self.custom_listen_url,
            "frontend_config": custom_frontend_config or self.frontend_config,
        }

    def _update_properties(
        self,
        mount_point_url,
        display_name,
        show_on_public_pages,
        is_default,
        is_public,
        relay_stream_url,
        max_listener_duration,
        fallback_mount,
        enable_autodj,
        autodj_format,
        autodj_bitrate,
        custom_url,
        custom_frontend_config
    ):
        self.name = mount_point_url or self.name
        self.display_name = display_name or self.display_name
        self.is_visible_on_public_pages = show_on_public_pages if show_on_public_pages is not None else self.is_visible_on_public_pages
        self.is_default = is_default if is_default is not None else self.is_default
        self.is_public = is_public if is_public is not None else self.is_public
        self.fallback_mount = fallback_mount or self.fallback_mount
        self.relay_url = relay_stream_url or self.relay_url
        self.max_listener_duration = max_listener_duration or self.max_listener_duration
        self.enable_autodj = enable_autodj if enable_autodj is not None else self.enable_autodj
        self.autodj_format = autodj_format or self.autodj_format
        self.autodj_bitrate = autodj_bitrate or self.autodj_bitrate
        self.custom_listen_url = custom_url or self.custom_listen_url
        self.frontend_config = custom_frontend_config or self.frontend_config

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
