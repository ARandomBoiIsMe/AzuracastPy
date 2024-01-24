from typing import List, Optional

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
from .hls_stream import HLSStream

from .helpers import (
    MountPointHelper,
    FileHelper,
    PlaylistHelper,
    PodcastHelper,
    SFTPUserHelper,
    HLSStreamHelper,
    StreamerHelper,
    WebhookHelper,
    RemoteRelayHelper
)

from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.util.media_util import generate_file_upload_structure
from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.constants import API_ENDPOINTS

class Station:
    """
    This class represents a station in an Azuracast web radio.

    It provides data and actions that can be performed on stations of a hosted radio.
    """
    def __init__(
        self, 
        id: str, 
        name: str, 
        shortcode: str, 
        description: str, 
        frontend: str, 
        backend: str,
        listen_url: str, 
        url: str, 
        public_player_url: str, 
        is_public: bool, 
        hls_enabled: bool,
        hls_listeners: int, 
        mounts: List[Mount], 
        remotes: List[Remote], 
        hls_is_default: bool = None,
        playlist_pls_url: Optional[str] = None, 
        playlist_m3u_url: Optional[str] = None,
        hls_url: Optional[str] = None, 
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

        self.mount_point = MountPointHelper(_station=self)
        self.file = FileHelper(_station=self)
        self.playlist = PlaylistHelper(_station=self)
        self.podcast = PodcastHelper(_station=self)
        self.streamer = StreamerHelper(_station=self)
        self.webhook = WebhookHelper(_station=self)
        self.remote_relay = RemoteRelayHelper(_station=self)
        self.sftp_user = SFTPUserHelper(_station=self)
        self.hls_stream = HLSStreamHelper(_station=self)

    def __repr__(self):
        return generate_repr_string(self)
    
    def _perform_service_action(
        self, 
        action: str, 
        service_type: str
    ):
        if action not in ['start', 'stop', 'restart']:
            raise ValueError("action must be one of: 'start', 'stop' or 'restart'")
        
        url = API_ENDPOINTS[f"{service_type}_action"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            action=action
        )

        response = self._request_handler.post(url)

        return response
    
    def _request_multiple_instances_of(
        self, 
        resource_name: str
    ):
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        return self._request_handler.get(url)

    def requestable_songs(self) -> List[RequestableSong]:
        """
        Retrieves songs that are available for requests on the station.

        :returns: A list of :class:`RequestableSong` objects.
        """
        response = self._request_multiple_instances_of("requestable_songs")

        return [RequestableSong(**rs) for rs in response]
    
    def request_song(
        self, 
        request_id: str
    ):
        """
        Makes a song request to the station.

        :param request_id: The ID of the song to be requested.
        """
        url = API_ENDPOINTS["song_request"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            request_id=request_id
        )

        response = self._request_handler.post(url)

        return response

    def status(self) -> StationStatus:
        """
        Displays the current status of the station.

        :returns: A :class:`StationStatus` object.
        """
        # Had to make an exception here cuz it doesn't need an ID despite being a single instance
        response = self._request_multiple_instances_of("station_status")

        return StationStatus(**response)
    
    def restart(self):
        """
        Restarts the station.
        """
        url = API_ENDPOINTS["restart_station"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.post(url)

        return response
    
    def perform_frontend_action(
        self, 
        action: str = 'restart'
    ):
        """
        Performs an action on the station's frontend. Available actions are 'start', 'stop' and 'restart'

        :param action: (Optional) The action to be performed. Default: ``"restart"``.
        """
        response = self._perform_service_action(action=action, service_type="frontend")

        return response
    
    def perform_backend_action(
        self, 
        action: str = 'restart'
    ):
        """
        Performs an action on the station's backend. Available actions are 'start', 'stop' and 'restart'

        :param action: (Optional) The action to be performed. Default: ``"restart"``.
        """
        response = self._perform_service_action(action=action, service_type="backend")

        return response
    
    def history(self) -> List[SongHistory]:
        """
        Retrieves the history of played songs on the station.  

        :returns: A list of :class:`SongHistory` objects.
        """
        response = self._request_multiple_instances_of("station_history")

        return [SongHistory(**sh) for sh in response]
    
    def listeners(self) -> List[Listener]:
        """
        Retrieves the current listeners of the station.  

        :returns: A list of :class:`Listener` objects.
        """
        response = self._request_multiple_instances_of("station_listeners")

        return [Listener(**l) for l in response]
    
    def schedule(self) -> List[ScheduleTime]:
        """
        Retrieves the schedule of the station.  

        :returns: A list of :class:`ScheduleTime` objects.
        """
        response = self._request_multiple_instances_of("station_schedule")

        return [ScheduleTime(**st) for st in response]
    
    def update_fallback(
        self, 
        path: str, 
        file: str
    ):
        url = API_ENDPOINTS["station_fallback"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        upload_body = generate_file_upload_structure(path, file)

        response = self._request_handler.post(url, upload_body)

        return response

    def fallback(self):
        # Request requires no ID, so I shall use this function
        response = self._request_multiple_instances_of("station_fallback")

        return response
    
    def files(self) -> List[StationFile]:
        """
        Retrieves the station's uploaded music files.

        :returns: A list of :class:`StationFile` objects.
        """
        response = self._request_multiple_instances_of("station_files")

        return [StationFile(**sf, _station=self) for sf in response]
       
    def mount_points(self) -> List[MountPoint]:
        """
        Retrieves the station's mount points.  

        :returns: A list of :class:`MountPoint` objects.
        """
        response = self._request_multiple_instances_of("station_mount_points")

        return [MountPoint(**mp, _station=self) for mp in response]
    
    def playlists(self) -> List[Playlist]:
        """
        Retrieves the station's playlists.  

        :returns: A list of :class:`Playlist` objects.
        """
        response = self._request_multiple_instances_of("station_playlists")

        return [Playlist(**p, _station=self) for p in response]
    
    def podcasts(self) -> List[Podcast]:
        """
        Retrieves the station's podcasts.  

        :returns: A list of :class:`Podcast` objects.
        """
        response = self._request_multiple_instances_of("station_podcasts")

        return [Podcast(**p, _station=self) for p in response]

    def queue(self) -> List[QueueItem]:
        response = self._request_multiple_instances_of("station_queue")

        return [QueueItem(**qi, _station=self) for qi in response]
    
    # Had to do this cuz, at the time of development, the API doesn't support a GET request for a 
    # single queue item. Throws a 405 error instead.
    def queue_item(self, 
    id: int) -> QueueItem:
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
        """
        Retrieves the station's remote relays.  

        :returns: A list of :class:`RemoteRelay` objects.
        """
        response = self._request_multiple_instances_of("station_remote_relays")

        return [RemoteRelay(**rr, _station=self) for rr in response]
    
    def sftp_users(self) -> List[SFTPUser]:
        """
        Retrieves the station's SFTP users.

        :returns: A list of :class:`SFTPUser` objects.
        """
        response = self._request_multiple_instances_of("station_sftp_users")

        return [SFTPUser(**su, _station=self) for su in response]
    
    def hls_streams(self) -> List[HLSStream]:
        """
        Retrieves the station's HTTP Live Streaming (HLS) streams.  

        :returns: A list of :class:`HLSStream` objects.
        """
        response = self._request_multiple_instances_of("hls_streams")

        return [HLSStream(**hs, _station=self) for hs in response]
    
    def streamers(self) -> List[Streamer]:
        """
        Retrieves the station's streamers.  

        :returns: A list of :class:`Streamer` objects.
        """
        response = self._request_multiple_instances_of("station_streamers")

        return [Streamer(**s, _station=self) for s in response]

    def webhooks(self) -> List[Webhook]:
        """
        Retrieves the station's webhooks.  

        :returns: A list of :class:`Webhook` objects.
        """
        response = self._request_multiple_instances_of("station_webhooks")

        return [Webhook(**wh, _station=self) for wh in response]