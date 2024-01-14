from AzuracastPy.constants import API_ENDPOINTS, HLS_FORMATS, BITRATES
from AzuracastPy.exceptions import ClientException
from AzuracastPy.util.general_util import generate_repr_string

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
        
        old_hls_stream = self._station.hls_stream(self.id)

        url = API_ENDPOINTS['hls_stream'].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(old_hls_stream, name, format, bitrate)

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(old_hls_stream, name, format, bitrate)

        return response

    def delete(self):
        url = API_ENDPOINTS['hls_stream'].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _build_update_body(self, old_hls_stream: "HLSStream", name, format, bitrate):
        return {
            "name": name if name else old_hls_stream.name,
            "format": format if format else old_hls_stream.format,
            "bitrate": bitrate if bitrate else old_hls_stream.bitrate
        }
    
    def _update_properties(self, old_hls_stream: "HLSStream", name, format, bitrate):
        self.name = name if name else old_hls_stream.name
        self.format = format if format else old_hls_stream.format
        self.bitrate = bitrate if bitrate else old_hls_stream.bitrate
    
    def _clear_properties(self):
        self.name = None
        self.format = None
        self.bitrate = None
        self.listeners = None
        self.id = None
        self.links = None
        self._station = None