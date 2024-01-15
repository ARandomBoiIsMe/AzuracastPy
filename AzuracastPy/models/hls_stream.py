from AzuracastPy.constants import API_ENDPOINTS, HLS_FORMATS, BITRATES
from AzuracastPy.exceptions import ClientException
from AzuracastPy.util.general_util import generate_repr_string
from .util.station_resource_operations import edit_resource, delete_resource

from typing import Optional

class Links:
    def __init__(self_, self):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class HLSStream:
    def __init__(self, name: str, format: str, bitrate: int, listeners: int, id: int, links: Links, _station):
        self.name = name
        self.format = format
        self.bitrate = bitrate
        self.listeners = listeners
        self.id = id
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(self, name: Optional[str] = None, format: Optional[str] = None, bitrate: Optional[int] = None):
        if format is not None:
            if format not in HLS_FORMATS:
                message = f"format param must be one of: {', '.join(HLS_FORMATS)}"
                raise ClientException(message)
        
        if bitrate is not None:
            if bitrate not in BITRATES:
                message = f"bitrate param must be one of: {', '.join(BITRATES)}"
                raise ClientException(message)
            
        return edit_resource(self, "hls_stream", name, format, bitrate)
    
    def delete(self):
        return delete_resource(self, "hls_stream")
    
    def _build_update_body(self, name, format, bitrate):
        return {
            "name": name if name else self.name,
            "format": format if format else self.format,
            "bitrate": bitrate if bitrate else self.bitrate
        }
    
    def _update_properties(self, name, format, bitrate):
        self.name = name if name else self.name
        self.format = format if format else self.format
        self.bitrate = bitrate if bitrate else self.bitrate
    
    def _clear_properties(self):
        self.name = None
        self.format = None
        self.bitrate = None
        self.listeners = None
        self.id = None
        self.links = None
        self._station = None