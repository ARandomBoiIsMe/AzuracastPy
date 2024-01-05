from typing import List, Optional, Dict, Any

from .mount import Mount
from .remote import Remote
from .requestable_song import RequestableSong
from .station_status import StationStatus
from .song_history import SongHistory
from .listener import Listener
from .schedule_time import ScheduleTime
from .station_file import StationFile
from .mount_point import MountPoint
from .playlist import Playlist
from .podcast import Podcast

from AzuracastPy.endpoints import API_ENDPOINTS
from AzuracastPy.request_handler import RequestHandler

class Station:
    def __init__(
            self, id: str, name: str, shortcode: str, description: str, frontend: str, backend: str,
            listen_url: str, url: str, public_player_url: str, is_public: bool, hls_enabled: bool,
            hls_listeners: int, mounts: List[Mount], remotes: List[Remote], hls_is_default: bool = None,
            playlist_pls_url: Optional[str] = None, playlist_m3u_url: Optional[str] = None,
            hls_url: Optional[str] = None, _request_handler: RequestHandler = None
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
    
    def _request_multiple_instances_of(self, resource_name: str):
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        return self._request_handler.get(url)
    
    def _request_single_instance_of(self, resource_name: str, resource_id: int):
        if type(resource_id) is not int:
            raise TypeError("id param should be of type int.")
        
        if resource_id < 0:
            raise ValueError("id must be a non-negative number.")
        
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=resource_id
        )

        return self._request_handler.get(url)

    def requestable_songs(self) -> List[RequestableSong]:
        response = self._request_multiple_instances_of("requestable_songs")

        return [RequestableSong(**rs) for rs in response]
    
    def request_song(self, request_id: str):
        url = API_ENDPOINTS["song_request"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            request_id=request_id
        )

        self._request_handler.post(url)

    def status(self) -> StationStatus:
        # Had to make an exception here cuz it doesn't need an ID despite being a single instance
        response = self._request_multiple_instances_of("station_status")

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
    
    def history(self) -> List[SongHistory]:
        response = self._request_multiple_instances_of("station_history")

        return [SongHistory(**sh) for sh in response]
    
    def listeners(self) -> List[Listener]:
        response = self._request_multiple_instances_of("station_listeners")

        return [Listener(**l) for l in response]
    
    def schedule(self) -> List[ScheduleTime]:
        response = self._request_multiple_instances_of("station_schedule")

        return [ScheduleTime(**st) for st in response]
    
    def files(self) -> List[StationFile]:
        response = self._request_multiple_instances_of("station_files")

        return [StationFile(**sf) for sf in response]
    
    def file(self, id: int) -> StationFile:
        response = self._request_single_instance_of("station_file", id)

        return StationFile(**response)
    
    def mount_points(self) -> List[MountPoint]:
        response = self._request_multiple_instances_of("station_mount_points")

        return [MountPoint(**mp) for mp in response]
    
    def mount_point(self, id) -> MountPoint:
        response = self._request_single_instance_of("station_mount_point", id)

        return MountPoint(**response)
    
    def playlists(self) -> List[Playlist]:
        response = self._request_multiple_instances_of("station_playlists")

        return [Playlist(**p) for p in response]
    
    def playlist(self, id) -> Playlist:
        response = self._request_single_instance_of("station_playlist", id)

        return Playlist(**response)
    
    def podcasts(self) -> List[Podcast]:
        response = self._request_multiple_instances_of("station_podcasts")

        return [Podcast(**p, station_id=self.id, _request_handler=self._request_handler) for p in response]

    # Can't use the _request_single_instance_of method here, cuz the ID is a string.
    # The function only works with integers.
    # Bummer.
    def podcast(self, id: str) -> Podcast:
        if type(id) is not str:
            raise TypeError("id param should be of type string.")
        
        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=id
        )

        response = self._request_handler.get(url)

        return Podcast(**response, station_id=self.id, _request_handler=self._request_handler)