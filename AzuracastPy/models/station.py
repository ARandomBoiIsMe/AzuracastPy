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
    """Represents a station on a radio."""
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
        timezone: str = None,
        playlist_pls_url: Optional[str] = None,
        playlist_m3u_url: Optional[str] = None,
        hls_url: Optional[str] = None,
        _request_handler: RequestHandler = None
    ):
        """
        Initializes a :class:`Station` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``client.station(id)`` or ``client.stations()``.
        """
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
        self.timezone = timezone
        self.hls_url = hls_url
        self.hls_listeners = hls_listeners
        self._request_handler = _request_handler

        self.mount_point = MountPointHelper(_station=self)
        """
        An instance of :class:`.MountPointHelper`.

        Provides the interface for working with :class:`.MountPoint` instances.

        For example, to get a mount point with an id of ``1`` from this station:

        .. code-block:: python

            mount_point = station.mount_point(1)

        To create a mount point on this station:

        .. code-block:: python

            from AzuracastPy.enums import Formats

            mount_point = station(1).mount_point.create(
                url="/autodj.mp3",
                display_name="Hehehehe",
                autodj_format=Formats.OPUS
            )
        """

        self.file = FileHelper(_station=self)
        """
        An instance of :class:`.FileHelper`.

        Provides the interface for working with :class:`.StationFile` instances.

        For example, to get an uploaded media file with an id of ``1`` from this station:

        .. code-block:: python

            file = station.file(1)

        To upload a file to this station:

        .. code-block:: python

            file = station.file.upload(
                path="song/on/station.mp3",
                file="file/path/on/local/system.mp3"
            )
        """

        self.playlist = PlaylistHelper(_station=self)
        """
        An instance of :class:`.PlaylistHelper`.

        Provides the interface for working with :class:`.Playlist` instances.

        For example, to get a playlist with an id of ``1`` from this station:

        .. code-block:: python

            playlist = station.playlist(1)

        To create a playlist on this station:

        .. code-block:: python

            from AzuracastPy.enums import PlaylistTypes

            playlist = station.playlist.create(
                name="New",
                type=PlaylistTypes.ONCE_PER_X_MINUTES,
                play_per_value=5
            )
        """

        self.podcast = PodcastHelper(_station=self)
        """
        An instance of :class:`.PodcastHelper`.

        Provides the interface for working with :class:`.Podcast` instances.

        For example, to get a podcast with an id of ``"podcast-id"`` from this station:

        .. code-block:: python

            podcast = station.podcast("podcast-id")

        To create a podcast on this station:

        .. code-block:: python

            from AzuracastPy.enums import Languages, PodcastCategories

            podcast = station.podcast.create(
                title="New podcast",
                description="This is a random description",
                language=Languages.ARABIC,
                categories=[
                    PodcastCategories.Arts.DESIGN,
                    PodcastCategories.Comedy.COMEDY_INTERVIEWS
                ]
            )
        """

        self.streamer = StreamerHelper(_station=self)
        """
        An instance of :class:`.StreamerHelper`.

        Provides the interface for working with :class:`.Streamer` instances.

        For example, to get a streamer with an id of ``1`` from this station:

        .. code-block:: python

            streamer = station.streamer(1)

        To create a streamer on this station:

        .. code-block:: python

            from AzuracastPy.enums import Languages, PodcastCategories

            podcast = station.podcast.create(
                title="New podcast",
                description="This is a random description",
                language=Languages.ARABIC,
                categories=[
                    PodcastCategories.Arts.DESIGN,
                    PodcastCategories.Comedy.COMEDY_INTERVIEWS
                ]
            )
        """

        self.webhook = WebhookHelper(_station=self)
        """
        An instance of :class:`.WebhookHelper`.

        Provides the interface for working with :class:`.Webhook` instances.

        For example, to get a webhook with an id of ``1`` from this station:

        .. code-block:: python

            webhook = station.webhook(1)

        To create a webhook on this station:

        .. code-block:: python

            from AzuracastPy.enums import WebhookConfigTypes, WebhookTriggers

            config = station.webhook.generate_webhook_config(
                subject="subject",
                message="message",
                to="to"
            )

            webhook = station.webhook.create(
                name="New email webhook",
                type=WebhookConfigTypes.EMAIL,
                webhook_config=config,
                triggers=[
                    WebhookTriggers.STATION_ONLINE,
                    WebhookTriggers.LIVE_CONNECT
                ]
            )
        """

        self.remote_relay = RemoteRelayHelper(_station=self)
        """
        An instance of :class:`.RemoteRelayHelper`.

        Provides the interface for working with :class:`.RemoteRelay` instances.

        For example, to get a remote with an id of ``1`` from this station:

        .. code-block:: python

            remote_relay = station.remote_relay(1)

        To create a remote on this station:

        .. code-block:: python

            from AzuracastPy.enums import Formats

            remote_relay = station.remote_relay.create(
                station_listening_url="http://station.example.com:8000",
                display_name="Display name",
                autodj_format=Formats.MP3
            )
        """

        self.sftp_user = SFTPUserHelper(_station=self)
        """
        An instance of :class:`.SFTPUserHelper`.

        Provides the interface for working with :class:`.SFTPUser` instances.

        For example, to get an SFTP user with an id of ``1`` from this station:

        .. code-block:: python

            sftp_user = station.sftp_user(1)

        To create a remote on this station:

        .. code-block:: python

            sftp_user = station.sftp_user.create(
                username="Username",
                password="Password",
                public_keys=['key1', 'key2']
            )
        """

        self.hls_stream = HLSStreamHelper(_station=self)
        """
        An instance of :class:`.HLSStreamHelper`.

        Provides the interface for working with :class:`.HLSStream` instances.

        For example, to get an HLS Stream with an id of ``1`` from this station:

        .. code-block:: python

            hls_stream = station.hls_stream(1)

        To create a remote on this station:

        .. code-block:: python

            from AzuracastPy.enums import Formats, Bitrates

            hls_stream = station.hls_stream.create(
                name="New HLS Stream",
                format=Formats.MP3,
                bitrate=Bitrates.BITRATE_32
            )
        """

        self.queue = QueueHelper(_station=self)
        """
        An instance of :class:`.QueueHelper`.

        Provides the interface for working with :class:`.QueueItem` instances.

        For example, to get a queue item with an id of ``1`` from this station:

        .. code-block:: python

            queue_item = station.queue(1)

        To get all items in the queue on this station:

        .. code-block:: python

            queue = station.queue()
        """

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
        if not isinstance(request_id, str):
            raise ValueError("request_id param must be a string.")

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
