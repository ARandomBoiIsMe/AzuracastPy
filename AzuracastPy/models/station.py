from typing import List, Optional, Dict, Any

from .mount import Mount
from .remote import Remote
from .requestable_song import RequestableSong
from .station_status import StationStatus
from .song_history import SongHistory

from endpoints import API_ENDPOINTS
from request_handler import RequestHandler

class Station:
    def __init__(
            self, id: str, name: str, shortcode: str, description: str, frontend: str, backend: str,
            listen_url: str, url: str, public_player_url: str, playlist_pls_url: str, playlist_m3u_url: str,
            is_public: bool, hls_enabled: bool, hls_url: Optional[str], hls_listeners: int,
            mounts: List[Mount], remotes: List[Remote], hls_is_default: bool = None,
            _request_handler: RequestHandler = None
        ):
        self.id = id
        self.name = name
        self.shortcode = shortcode
        self.description = description
        self.frontend = frontend
        self.backend = backend
        self.listen_url = listen_url
        self.url = url
        self.public_player_url = public_player_url
        self.playlist_pls_url = playlist_pls_url
        self.playlist_m3u_url = playlist_m3u_url
        self.is_public = is_public
        self.mounts = mounts
        self.remotes = remotes
        self.hls_enabled = hls_enabled
        self.hls_is_default = hls_is_default
        self.hls_url = hls_url
        self.hls_listeners = hls_listeners
        self._request_handler = _request_handler

    def __repr__(self):
        return (
            f"Station(id={self.id!r}, name={self.name!r}, shortcode={self.shortcode!r}, "
            f"description={self.description!r}, frontend={self.frontend!r}, backend={self.backend!r}, "
            f"listen_url={self.listen_url!r}, url={self.url!r}, public_player_url={self.public_player_url!r}, "
            f"is_public={self.is_public}, hls_enabled={self.hls_enabled}, hls_listeners={self.hls_listeners}, "
            f"mounts={self.mounts!r}, remotes={self.remotes!r})"
        )
    
    def requestable_songs(self) -> List[RequestableSong]:
        url = API_ENDPOINTS["requestable_songs"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.get(url)

        return [RequestableSong(**rs) for rs in response]
    
    def request_song(self, request_id: str):
        url = API_ENDPOINTS["song_request"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            request_id=request_id
        )

        self._request_handler.post(url)

    def status(self) -> StationStatus:
        url = API_ENDPOINTS["station_status"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.get(url)

        return StationStatus(**response)
    
    def restart(self):
        url = API_ENDPOINTS["restart_station"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.post(url)

        return response['message']
    
    def perform_frontend_action(self, action: str = 'restart'):
        response = self._perform_service_action(action=action, service_type="frontend")

        return response['message']
    
    def perform_backend_action(self, action: str = 'restart'):
        response = self._perform_service_action(action=action, service_type="backend")

        return response['message']
    
    def _perform_service_action(self, action: str, service_type: str):
        if action not in ['start', 'stop', 'restart']:
            raise ValueError("action must be one of 'start', 'stop' or 'restart'")
        
        url = API_ENDPOINTS[f"{service_type}_action"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            action=action
        )

        response = self._request_handler.post(url)

        return response
    
    def history(self) -> List[SongHistory]:
        url = API_ENDPOINTS["station_history"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.get(url)

        return [SongHistory(**sh) for sh in response]