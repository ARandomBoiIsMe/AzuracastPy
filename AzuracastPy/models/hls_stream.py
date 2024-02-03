"""Class for a station HLS Stream"""

from typing import Optional

from ..enums import Formats, Bitrates
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string, generate_enum_error_text

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_,
        self: str
    ):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class HLSStream:
    def __init__(
        self,
        name: str,
        format: str,
        bitrate: int,
        listeners: int,
        id: int,
        links: Links,
        _station
    ):
        self.name = name
        self.format = format
        self.bitrate = bitrate
        self.listeners = listeners
        self.id = id
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        name: Optional[str] = None,
        format: Optional[Formats] = None,
        bitrate: Optional[Bitrates] = None
    ):
        """
        Edits the HTTP Live Streaming (HLS) stream's properties.

        Updates all edited attributes of the current :class:`HLSStream` object.

        :param name: (Optional) The new name of the hls stream. Default: ``None``.
        :param format: (Optional) The new format of the hls stream. Default: ``None``.
        :param bitrate: (Optional) The new bitrate of the hls stream. Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import Formats, Bitrates

            station.hls_stream(1).edit(
                name="New name",
                format=Formats.OPUS,
                bitrate=Bitrates.BITRATE_128
            )
        """
        if format:
            if not isinstance(format, Formats):
                raise ClientException(generate_enum_error_text("format", Formats))

            format = format.value

        if bitrate:
            if not isinstance(bitrate, Bitrates):
                raise ClientException(generate_enum_error_text("bitrate", Bitrates))

            bitrate = bitrate.value

        return edit_station_resource(self, "hls_stream", name, format, bitrate)

    def delete(self):
        """
        Deletes the HTTP Live Streaming (HLS) stream from the station.

        Sets all attributes of the current :class:`HLSStream` object to ``None``.

        Usage:
        .. code-block:: python

            station.hls_stream(1).delete()
        """
        return delete_station_resource(self, "hls_stream")

    def _build_update_body(
        self,
        name,
        format,
        bitrate
    ):
        return {
            "name": name or self.name,
            "format": format or self.format,
            "bitrate": bitrate or self.bitrate
        }

    def _update_properties(
        self,
        name,
        format,
        bitrate
    ):
        self.name = name or self.name
        self.format = format or self.format
        self.bitrate = bitrate or self.bitrate

    def _clear_properties(self):
        self.name = None
        self.format = None
        self.bitrate = None
        self.listeners = None
        self.id = None
        self.links = None
        self._station = None
