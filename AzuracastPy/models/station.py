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
from .webhook import Webhook

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.util import file_upload_util, general_util

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
    
    def _delete_single_instance_of(self, resource_name: str, resource_id: int):
        if type(resource_id) is not int:
            raise TypeError("id param should be of type int.")
        
        if resource_id < 0:
            raise ValueError("id must be a non-negative number.")
        
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=resource_id
        )

        return self._request_handler.delete(url)

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
    
    def upload_file(self, path: str, file: str) -> StationFile:
        url = API_ENDPOINTS["station_files"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        upload_body = file_upload_util.generate_file_upload_structure(path, file)

        response = self._request_handler.post(url, upload_body)

        return StationFile(**response, station=self)
    
    def files(self) -> List[StationFile]:
        response = self._request_multiple_instances_of("station_files")

        return [StationFile(**sf, station=self) for sf in response]
    
    def file(self, id: int) -> StationFile:
        response = self._request_single_instance_of("station_file", id)

        return StationFile(**response, station=self)

    def edit_file(
            self, id: int, title: Optional[str] = None, artist: Optional[str] = None, path: Optional[str] = None,
            genre: Optional[str] = None, album: Optional[str] = None, lyrics: Optional[str] = None,
            isrc: Optional[str] = None, playlists: Optional[List[str]] = None, amplify: Optional[int] = None,
            fade_overlap: Optional[int] = None, fade_in: Optional[int] = None, fade_out: Optional[int] = None,
            cue_in: Optional[int] = None, cue_out: Optional[int] = None
        ):
        old_file = self.file(id)

        url = API_ENDPOINTS["station_file"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=id
        )

        body = {
            "artist": artist if artist else old_file.artist,
            "title": title if title else old_file.title,
            "album": album if album else old_file.album,
            "genre": genre if genre else old_file.genre,
            "lyrics": lyrics if lyrics else old_file.lyrics,
            "path": path if path else old_file.path,
            "isrc": isrc if isrc else old_file.isrc,
            "amplify": amplify if amplify else old_file.amplify,
            "fade_overlap": fade_overlap if fade_overlap else old_file.fade_overlap,
            "fade_in": fade_in if fade_in else old_file.fade_in,
            "fade_out": fade_out if fade_out else old_file.fade_out,
            "cue_in": cue_in if cue_in else old_file.cue_in,
            "cue_out": cue_out if cue_out else old_file.cue_out,
            "playlists": playlists if playlists else old_file.playlists
        }

        response = self._request_handler.put(url, body)

        return response['message']
    
    def delete_file(self, id: int):
        response = self._delete_single_instance_of("station_file", id)

        return response
    
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

        return Playlist(**response)
    
    def playlists(self) -> List[Playlist]:
        response = self._request_multiple_instances_of("station_playlists")

        return [Playlist(**p) for p in response]
    
    def playlist(self, id: int) -> Playlist:
        response = self._request_single_instance_of("station_playlist", id)

        return Playlist(**response)
    
    def edit_playlist(
            self, id: int, name: Optional[str] = None, type: Optional[str] = None, source: Optional[str] = None,
            order: Optional[str] = None, remote_url: Optional[str] = None, remote_type: Optional[str] = None,
            remote_buffer: Optional[int] = None, play_per_value: Optional[int] = None, weight: Optional[int] = None,
            include_in_requests: Optional[bool] = None, include_in_on_demand: Optional[bool] = None,
            avoid_duplicates: Optional[bool] = None, is_jingle: Optional[bool] = None
        ):
        old_playlist = self.playlist(id)

        url = API_ENDPOINTS["station_playlist"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=id
        )

        body = {
            "name": name if name else old_playlist.name,
            "type": type if type else old_playlist.type,
            "source": source if source else old_playlist.source,
            "order": order if order else old_playlist.order,
            "remote_url": remote_url if remote_url else old_playlist.remote_url,
            "remote_type": remote_type if remote_type else old_playlist.remote_type,
            "remote_buffer": remote_buffer if remote_buffer else old_playlist.remote_buffer,
            "is_jingle": is_jingle if is_jingle is not None else old_playlist.is_jingle,
            "play_per_songs": play_per_value if type == "once_per_x_songs" else old_playlist.play_per_songs,
            "play_per_minutes": play_per_value if type == "once_per_x_minutes" else old_playlist.play_per_minutes,
            "play_per_hour_minute": play_per_value if type == "once_per_hour" else old_playlist.play_per_hour_minute,
            "weight": weight if weight is not None else old_playlist.weight,
            "include_in_requests": include_in_requests if include_in_requests is not None else old_playlist.include_in_requests,
            "include_in_on_demand": include_in_on_demand if include_in_on_demand is not None else old_playlist.include_in_on_demand,
            "avoid_duplicates": avoid_duplicates if avoid_duplicates is not None else old_playlist.avoid_duplicates
        }

        response = self._request_handler.put(url, body)

        return response['message']
    
    def delete_playlist(self, id: int):
        response = self._delete_single_instance_of("station_playlist", id)

        return response['message']
    
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

        return Podcast(**response)
    
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
    
    def edit_podcast(
        self, id: str, title: Optional[str] = None, description: Optional[str] = None, language: Optional[str] = None,
        categories: Optional[List[str]] = None, author: Optional[str] = None, email: Optional[str] = None,
        website: Optional[str] = None
    ):
        old_podcast = self.podcast(id)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=id
        )

        if language is not None and len(language) > 2:
            language = language.lower().replace(' ', '_')
            language = general_util.get_language_code(language)

        body = {
            "title": title if title else old_podcast.title,
            "description": description if description else old_podcast.description,
            "language": language if language else old_podcast.language,
            "author": author if author else old_podcast.author,
            "email": email if email else old_podcast.email,
            "link": website if website else old_podcast.link,
            "categories": categories if categories else old_podcast.categories
        }

        response = self._request_handler.put(url, body)

        return response['message']

    def delete_podcast(self, id: str) -> str:
        if type(id) is not str:
            raise TypeError("id param should be of type string.")
        
        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=id
        )

        response = self._request_handler.delete(url)

        return response['message']
    
    def queue(self) -> List[QueueItem]:
        response = self._request_multiple_instances_of("station_queue")

        return [QueueItem(**qi) for qi in response]
    
    # Had to do this cuz the API doesn't support a GET request for a 
    # single queue item. Throws a 405 error instead.
    def queue_item(self, id: int) -> QueueItem:
        queue_response = self._request_multiple_instances_of("station_queue")

        queue = [QueueItem(**qi) for qi in queue_response]

        id = id - 1
        if id < 0:
            raise IndexError("Requested resource not found.")
        
        try:
            return queue[id]
        except IndexError:
            raise IndexError("Requested resource not found.")

    def delete_queue_item(self, id: int):
        response = self._delete_single_instance_of("station_queue_item", id)

        return response['message']
    
    def remote_relays(self) -> List[RemoteRelay]:
        response = self._request_multiple_instances_of("station_remote_relays")

        return [RemoteRelay(**rr) for rr in response]
    
    def remote_relay(self, id: int) -> RemoteRelay:
        response = self._request_single_instance_of("station_remote_relay_item", id)

        return RemoteRelay(**response)
    
    def sftp_users(self) -> List[SFTPUser]:
        response = self._request_multiple_instances_of("station_sftp_users")

        return [SFTPUser(**su) for su in response]
    
    def sftp_user(self, id: int) -> SFTPUser:
        response = self._request_single_instance_of("station_sftp_user", id)

        return SFTPUser(**response)
    
    def streamers(self) -> List[Streamer]:
        response = self._request_multiple_instances_of("station_streamers")

        return [Streamer(**s) for s in response]
    
    def streamer(self, id: int) -> Streamer:
        response = self._request_single_instance_of("station_streamer", id)

        return Streamer(**response)
    
    def webhooks(self) -> List[Webhook]:
        response = self._request_multiple_instances_of("station_webhooks")

        return [Webhook(**s) for s in response]
    
    def webhook(self, id: int) -> Webhook:
        response = self._request_single_instance_of("station_webhook", id)

        return Webhook(**response)
    
    def delete_webhook(self, id: int):
        response = self._delete_single_instance_of("station_webhook", id)

        return response['message']