"""Class for a station on the radio."""

from typing import List, Optional

from ..request_handler import RequestHandler
from ..util.general_util import generate_repr_string, generate_enum_error_text
from ..constants import API_ENDPOINTS
from ..exceptions import ClientException
from ..enums import ServiceActions

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
    RemoteRelayHelper,
    QueueHelper
)

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
        self.mounts = [Mount(**m) for m in mounts] if mounts else []
        self.remotes = [Remote(**r) for r in remotes] if remotes else []
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
        self.queue = QueueHelper(_station=self)

    def __repr__(self):
        return generate_repr_string(self)

    def _perform_service_action(
        self,
        action: str,
        service_type: str
    ):
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

        Usage:
        .. code-block:: python

            requestable_songs = station.requestable_songs()
        """
        response = self._request_multiple_instances_of("requestable_songs")

        return [RequestableSong(**rs) for rs in response]

    def request_song(
        self,
        request_id: str
    ):
        """
        Makes a song request to the station.

        :param request_id: The request ID of the song to be requested.

        Usage:
        .. code-block:: python

            station.request_song("request_id")
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

        Usage:
        .. code-block:: python

            status = station.status()
        """
        response = self._request_multiple_instances_of("station_status")

        return StationStatus(**response)

    def restart(self):
        """
        Restarts the station.

        Usage:
        .. code-block:: python

            station.restart()
        """
        url = API_ENDPOINTS["restart_station"].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        response = self._request_handler.post(url)

        return response

    def perform_frontend_action(
        self,
        action: ServiceActions = ServiceActions.RESTART
    ):
        """
        Performs an action on the station's frontend.

        :param action: (Optional) The action to be performed. Default: ``ServiceActions.RESTART``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import ServiceActions

            station.perform_frontend_action(ServiceActions.STOP)
        """
        if not isinstance(action, ServiceActions):
            raise ClientException(generate_enum_error_text("action", ServiceActions))

        action = action.value

        return self._perform_service_action(action=action, service_type="frontend")

    def perform_backend_action(
        self,
        action: ServiceActions = ServiceActions.RESTART
    ):
        """
        Performs an action on the station's backend.

        :param action: (Optional) The action to be performed. Default: ``ServiceActions.RESTART``.

        Usage:
        .. code-block:: python

            station.perform_backend_action(ServiceActions.STOP)
        """
        if not isinstance(action, ServiceActions):
            raise ClientException(generate_enum_error_text("action", ServiceActions))

        action = action.value

        return self._perform_service_action(action=action, service_type="backend")

    def history(self) -> List[SongHistory]:
        """
        Retrieves the history of played songs on the station.

        :returns: A list of :class:`SongHistory` objects.

        Usage:
        .. code-block:: python

            song_history = station.history()
        """
        response = self._request_multiple_instances_of("station_history")

        return [SongHistory(**sh) for sh in response]

    def listeners(self) -> List[Listener]:
        """
        Retrieves the current listeners of the station.

        :returns: A list of :class:`Listener` objects.

        Usage:
        .. code-block:: python

            listeners = station.listeners()
        """
        response = self._request_multiple_instances_of("station_listeners")

        return [Listener(**l) for l in response]

    def schedule(self) -> List[ScheduleTime]:
        """
        Retrieves the schedule of the station.

        :returns: A list of :class:`ScheduleTime` objects.

        Usage:
        .. code-block:: python

            schedule = station.schedule()
        """
        response = self._request_multiple_instances_of("station_schedule")

        return [ScheduleTime(**st) for st in response]

    def fallback(self):
        # Request requires no ID, so I shall use this function
        return self._request_multiple_instances_of("station_fallback")

    def files(self) -> List[StationFile]:
        """
        Retrieves the station's uploaded music files.

        :returns: A list of :class:`StationFile` objects.

        Usage:
        .. code-block:: python

            files = station.files()
        """
        response = self._request_multiple_instances_of("station_files")

        return [StationFile(**sf, _station=self) for sf in response]

    def mount_points(self) -> List[MountPoint]:
        """
        Retrieves the station's mount points.

        :returns: A list of :class:`MountPoint` objects.

        Usage:
        .. code-block:: python

            mount_points = station.mount_points()
        """
        response = self._request_multiple_instances_of("station_mount_points")

        return [MountPoint(**mp, _station=self) for mp in response]

    def playlists(self) -> List[Playlist]:
        """
        Retrieves the station's playlists.

        :returns: A list of :class:`Playlist` objects.

        Usage:
        .. code-block:: python

            playlists = station.playlists()
        """
        response = self._request_multiple_instances_of("station_playlists")

        return [Playlist(**p, _station=self) for p in response]

    def podcasts(self) -> List[Podcast]:
        """
        Retrieves the station's podcasts.

        :returns: A list of :class:`Podcast` objects.

        Usage:
        .. code-block:: python

            podcasts = station.podcasts()
        """
        response = self._request_multiple_instances_of("station_podcasts")

        return [Podcast(**p, _station=self) for p in response]

    def remote_relays(self) -> List[RemoteRelay]:
        """
        Retrieves the station's remote relays.

        :returns: A list of :class:`RemoteRelay` objects.

        Usage:
        .. code-block:: python

            remote_relays = station.remote_relays()
        """
        response = self._request_multiple_instances_of("station_remote_relays")

        return [RemoteRelay(**rr, _station=self) for rr in response]

    def sftp_users(self) -> List[SFTPUser]:
        """
        Retrieves the station's SFTP users.

        :returns: A list of :class:`SFTPUser` objects.

        Usage:
        .. code-block:: python

            sftp_users = station.sftp_users()
        """
        response = self._request_multiple_instances_of("station_sftp_users")

        return [SFTPUser(**su, _station=self) for su in response]

    def hls_streams(self) -> List[HLSStream]:
        """
        Retrieves the station's HTTP Live Streaming (HLS) streams.

        :returns: A list of :class:`HLSStream` objects.

        Usage:
        .. code-block:: python

            hls_streams = station.hls_streams()
        """
        response = self._request_multiple_instances_of("hls_streams")

        return [HLSStream(**hs, _station=self) for hs in response]

    def streamers(self) -> List[Streamer]:
        """
        Retrieves the station's streamers.

        :returns: A list of :class:`Streamer` objects.

        Usage:
        .. code-block:: python

            streamers = station.streamers()
        """
        response = self._request_multiple_instances_of("station_streamers")

        return [Streamer(**s, _station=self) for s in response]

    def webhooks(self) -> List[Webhook]:
        """
        Retrieves the station's webhooks.

        :returns: A list of :class:`Webhook` objects.

        Usage:
        .. code-block:: python

            webhooks = station.webhooks()
        """
        response = self._request_multiple_instances_of("station_webhooks")

        return [Webhook(**wh, _station=self) for wh in response]
