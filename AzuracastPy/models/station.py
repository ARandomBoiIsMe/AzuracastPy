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
from .queue_item import QueueItem
from .remote_relay import RemoteRelay
from .sftp_user import SFTPUser
from .streamer import Streamer
from .webhook import Webhook, WebhookConfig
from .hls_stream import HLSStream

from AzuracastPy.constants import (
    API_ENDPOINTS,
    WEBHOOK_CONFIG_TEMPLATES,
    WEBHOOK_TRIGGERS,
    HLS_FORMATS
)
from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.util import file_upload_util, general_util
from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.exceptions import ClientException

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
        return generate_repr_string(self)
    
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
    
    def update_fallback(self, path: str, file: str):
        url = API_ENDPOINTS["station_fallback"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        upload_body = file_upload_util.generate_file_upload_structure(path, file)

        response = self._request_handler.post(url, upload_body)

        return response

    def fallback(self):
        # Request requires no ID, so I shall use this function
        response = self._request_multiple_instances_of("station_fallback")

        return response
    
    def upload_file(self, path: str, file: str) -> StationFile:
        url = API_ENDPOINTS["station_files"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        upload_body = file_upload_util.generate_file_upload_structure(path, file)

        response = self._request_handler.post(url, upload_body)

        return StationFile(**response, _station=self)
    
    def files(self) -> List[StationFile]:
        response = self._request_multiple_instances_of("station_files")

        return [StationFile(**sf, _station=self) for sf in response]
    
    def file(self, id: int) -> StationFile:
        response = self._request_single_instance_of("station_file", id)

        return StationFile(**response, _station=self)
    
    def mount_points(self) -> List[MountPoint]:
        response = self._request_multiple_instances_of("station_mount_points")

        return [MountPoint(**mp) for mp in response]
    
    def mount_point(self, id: int) -> MountPoint:
        response = self._request_single_instance_of("station_mount_point", id)

        return MountPoint(**response)
    
    def add_playlist(
        self, name: str, type: str = "default", source: str = "songs", order: str = "shuffle",
        remote_url: Optional[str] = None, remote_type: str = "stream", remote_buffer: int = 0,
        play_per_value: int = 0, weight: int = 3, include_in_requests: bool = True, 
        include_in_on_demand: bool = False, avoid_duplicates: bool = True, is_jingle: bool = False
    ):
        url = API_ENDPOINTS["station_playlists"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        body = {
            "name": name,
            "type": type,
            "source": source,
            "order": order,
            "remote_url": remote_url,
            "remote_type": remote_type,
            "remote_buffer": remote_buffer,
            "is_jingle": is_jingle,
            "play_per_songs": play_per_value if type == "once_per_x_songs" else 0,
            "play_per_minutes": play_per_value if type == "once_per_x_minutes" else 0,
            "play_per_hour_minute": play_per_value if type == "once_per_hour" else 0,
            "weight": weight,
            "include_in_requests": include_in_requests,
            "include_in_on_demand": include_in_on_demand,
            "avoid_duplicates": avoid_duplicates
        }

        response = self._request_handler.post(url, body)

        return Playlist(**response, _station=self)
    
    def playlists(self) -> List[Playlist]:
        response = self._request_multiple_instances_of("station_playlists")

        return [Playlist(**p, _station=self) for p in response]
    
    def playlist(self, id: int) -> Playlist:
        response = self._request_single_instance_of("station_playlist", id)

        return Playlist(**response, _station=self)
    
    def add_podcast(
        self, title: str, description: str, language: str, categories: Optional[List[str]] = None,
        author: Optional[str] = None, email: Optional[str] = None, website: Optional[str] = None
    ) -> Podcast:
        url = API_ENDPOINTS["station_podcasts"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        if len(language) > 2:
            language = language.lower().replace(' ', '_')
            language = general_util.get_language_code(language)

        body = {
            "title": title,
            "description": description,
            "language": language,
            "author": author if author else "",
            "email": email if email else "",
            "link": website if website else "",
            "categories": categories if categories else []
        }

        response = self._request_handler.post(url, body)

        return Podcast(**response, _station=self)
    
    def podcasts(self) -> List[Podcast]:
        response = self._request_multiple_instances_of("station_podcasts")

        return [Podcast(**p, _station=self) for p in response]

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

        return Podcast(**response, _station=self)
    
    def queue(self) -> List[QueueItem]:
        response = self._request_multiple_instances_of("station_queue")

        return [QueueItem(**qi, _station=self) for qi in response]
    
    # Had to do this cuz the API doesn't support a GET request for a 
    # single queue item. Throws a 405 error instead.
    def queue_item(self, id: int) -> QueueItem:
        queue_response = self._request_multiple_instances_of("station_queue")

        queue = [QueueItem(**qi, _station=self) for qi in queue_response]

        id = id - 1
        if id < 0:
            raise IndexError("Requested resource not found.")
        
        try:
            return queue[id]
        except IndexError:
            raise IndexError("Requested resource not found.")
    
    def remote_relays(self) -> List[RemoteRelay]:
        response = self._request_multiple_instances_of("station_remote_relays")

        return [RemoteRelay(**rr) for rr in response]
    
    def remote_relay(self, id: int) -> RemoteRelay:
        response = self._request_single_instance_of("station_remote_relay_item", id)

        return RemoteRelay(**response)
    
    def add_sftp_user(self, username: str, password: str, public_keys: Optional[str] = None):
        url = API_ENDPOINTS["station_sftp_users"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        body = {
            "username": username,
            "password": password,
            "publicKeys": public_keys if public_keys else ""
        }

        response = self._request_handler.post(url, body)

        return SFTPUser(**response, _station=self)

    def sftp_users(self) -> List[SFTPUser]:
        response = self._request_multiple_instances_of("station_sftp_users")

        return [SFTPUser(**su, _station=self) for su in response]
    
    def sftp_user(self, id: int) -> SFTPUser:
        response = self._request_single_instance_of("station_sftp_user", id)

        return SFTPUser(**response, _station=self)
    
    def add_hls_stream(self, name: str, format: str = "aac") -> HLSStream:
        if format not in HLS_FORMATS:
            message = f"format param must be one of {', '.join(HLS_FORMATS)}"
            raise ClientException(message)

        url = API_ENDPOINTS['hls_streams'].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        body = {
            "name": name,
            "format": format
        }

        response = self._request_handler.post(url, body)

        return HLSStream(**response, _station=self)

    def hls_streams(self) -> List[HLSStream]:
        response = self._request_multiple_instances_of("hls_streams")

        return [HLSStream(**hs, _station=self) for hs in response]
    
    def hls_stream(self, id: int) -> HLSStream:
        response = self._request_single_instance_of("hls_stream", id)

        return HLSStream(**response, _station=self)
    
    def add_streamer(
        self, streamer_username: str, streamer_password: str, display_name: Optional[str] = None,
        comments: Optional[str] = None, is_active: bool = True, enforce_schedule: bool = False
    ) -> Streamer:
        url = API_ENDPOINTS["station_streamers"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        body = {
            "streamer_username": streamer_username,
            "streamer_password": streamer_password,
            "display_name": display_name if display_name else "",
            "comments": comments if comments else "",
            "is_active": is_active,
            "enforce_schedule": enforce_schedule
        }

        response = self._request_handler.post(url, body)

        return Streamer(**response, _station=self)
    
    def streamers(self) -> List[Streamer]:
        response = self._request_multiple_instances_of("station_streamers")

        return [Streamer(**s, _station=self) for s in response]
    
    def streamer(self, id: int) -> Streamer:
        response = self._request_single_instance_of("station_streamer", id)

        return Streamer(**response, _station=self)
    
    def add_webhook(
        self, name: str, type: str, webhook_config: WebhookConfig, triggers: Optional[List[str]] = None 
    ) -> Webhook:
        valid_types = WEBHOOK_CONFIG_TEMPLATES.keys()
        if type not in valid_types:
            message = f"type param must be one of {', '.join(valid_types)}"
            raise ClientException(message)
        
        if triggers is not None:
            if not all(trigger in WEBHOOK_TRIGGERS for trigger in set(triggers)):
                message = f"Invalid trigger found in triggers list. Elements in trigger list must be one of {', '.join(WEBHOOK_TRIGGERS)}."
                raise ClientException(message)
        
        config = webhook_config.to_dict()
        if not all(key in config for key in WEBHOOK_CONFIG_TEMPLATES['email']):
            message = f"The provided 'webhook_config' is either incomplete or contains unneeded keys for the '{type}' webhook. The '{type}' webhook's config must only contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[type])}. Refer to the documentation for the config structure of each webhook type."
            raise ClientException(message)
        
        url = API_ENDPOINTS["station_webhooks"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )
        
        body = {
            "name": name,
            "type": type,
            "triggers": triggers if triggers else [],
            "config": config
        }

        response = self._request_handler.post(url=url, body=body)

        return Webhook(**response, _station=self)

    def webhooks(self) -> List[Webhook]:
        response = self._request_multiple_instances_of("station_webhooks")

        return [Webhook(**wh, _station=self) for wh in response]
    
    def webhook(self, id: int) -> Webhook:
        response = self._request_single_instance_of("station_webhook", id)

        return Webhook(**response, _station=self)