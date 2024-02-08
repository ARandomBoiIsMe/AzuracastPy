"""Helper functions for station resources."""

from typing import Optional, Union, Dict, Any, List

from ..util.media_util import generate_file_upload_structure
from ..util.general_util import get_day_number, generate_enum_error_text
from ..exceptions import ClientException
from ..constants import API_ENDPOINTS, WEBHOOK_CONFIG_TEMPLATES
from ..enums import (
    WebhookConfigTypes,
    WebhookTriggers,
    Formats,
    Bitrates,
    RemoteTypes,
    PlaylistTypes,
    PlaylistSources,
    PlaylistOrders,
    PlaylistRemoteTypes,
    Languages,
    PodcastCategories
)

from .mount_point import MountPoint
from .station_file import StationFile
from .playlist import Playlist
from .podcast import Podcast
from .hls_stream import HLSStream
from .sftp_user import SFTPUser
from .streamer import Streamer
from .remote_relay import RemoteRelay
from .webhook import Webhook
from .queue_item import QueueItem

def _request_single_instance_of_station_resource(
    station,
    resource_name,
    resource_id
):
    if type(resource_id) is not int or resource_id < 0:
        raise ValueError("id param must be a non-negative integer.")

    url = API_ENDPOINTS[resource_name].format(
        radio_url=station._request_handler.radio_url,
        station_id=station.id,
        id=resource_id
    )

    return station._request_handler.get(url)

class MountPointHelper:
    """Provides a set of functions to interact with mount points."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> MountPoint:
        """
        Retrieves a specific mount point from the station.

        :param id: The numerical ID of the mount point to be retrieved.

        :returns: A :class:`MountPoint` object.

        Usage:
        .. code-block:: python

            mount_point = station.mount_point(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_mount_point",
            resource_id=id
        )

        return MountPoint(**response, _station=self._station)

    # TODO: intro_path requires file upload
    def create(
        self,
        url: str,
        display_name: Optional[str] = None,
        show_on_public_pages: bool = True,
        is_default: bool = False,
        is_public: bool = True,
        relay_stream_url: Optional[str] = None,
        max_listener_duration: int = 0,
        fallback_mount: str = "/error.mp3",
        enable_autodj: bool = True,
        autodj_format: Formats = Formats.MP3,
        autodj_bitrate: Bitrates = Bitrates.BITRATE_128,
        custom_url: Optional[str] = None,
        custom_frontend_config: Optional[Union[Dict[str, Any], str]] = None
    ) -> MountPoint:
        """
        Adds a mount point to the station.

        :param url: The URL assigned to the mount point. Must be a valid URL, such as
            ``"/autodj.mp3"``.
        :param display_name: (Optional) The display name assigned to this mount point when viewing
            it on administrative or public pages. Leave as ``None`` to automatically generate one.
            Default: ``None``.
        :param show_on_public_pages: Determines whether listeners are allowed to select this mount
            point on this station's public pages. Default: ``True``.
        :param is_default: Determines whether this mount will be played on the radio preview and
            the public radio page in this system. Default: ``False``.
        :param is_public: Determines whether this mount will be advertised on "Yellow Pages" public
            radio directories. Default: ``True``.
        :param relay_stream_url: (Optional) The full URL of another stream to relay its broadcast
            through this mount point. Default: ``None``.
        :param max_listener_duration: The length of time (seconds) a listener will stay connected
            to the stream. Set to ``0`` to let listeners stay connected infinitely. Default: ``0``.
        :param fallback_mount: The mount point users will be redirected to if this mount point is
            not playing audio. Default: ``"/error.mp3"``, a repeating error message.
        :param enable_autodj: Determines whether the AutoDJ will automatically play music to this
            mount point. Default: ``True``.
        :param autodj_format: The format of the audio AutoDJ will play on this mount point.
            Default: ``Formats.MP3``.
        :param autodj_bitrate: The bitrate of the audio AutoDJ will play on this mount point.
            Default: ``Bitrates.BITRATE_128``.
        :param custom_url: (Optional) A custom URL for this stream that AzuraCast will use when
            referring to it. Leave as ``None`` to use the default value. Default: ``None``.
        :param custom_frontend_config: (Optional) Special mount point settings, in either
            JSON { key: 'value' } format or XML <key>value</key>. Default: ``None``.

        :returns: A :class:`MountPoint` object for the newly created mount point.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import Formats

            mount_point = station.mount_point.create(
                url="/autodj.mp3",
                display_name="Hehehehe",
                autodj_format=Formats.OPUS
            )
        """
        if not isinstance(autodj_format, Formats):
            raise ClientException(generate_enum_error_text("autodj_format", Formats))

        autodj_format = autodj_format.value

        if not isinstance(autodj_bitrate, Bitrates):
            raise ClientException(generate_enum_error_text("autodj_bitrate", Bitrates))

        autodj_bitrate = autodj_bitrate.value

        url = API_ENDPOINTS["station_mount_points"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "name": url,
            "display_name": display_name or "",
            "is_visible_on_public_pages": show_on_public_pages,
            "is_default": is_default,
            "is_public": is_public,
            "fallback_mount": fallback_mount,
            "relay_url": relay_stream_url or "",
            "max_listener_duration": max_listener_duration,
            "enable_autodj": enable_autodj,
            "autodj_format": autodj_format,
            "autodj_bitrate": autodj_bitrate,
            "custom_listen_url": custom_url,
            "frontend_config": custom_frontend_config,
        }

        response = self._station._request_handler.post(url, body)

        return MountPoint(**response, _station=self._station)

class FileHelper:
    """Provides a set of functions to interact with station files."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> StationFile:
        """
        Retrieves a specific uploaded music file from the station.

        :param id: The numerical ID of the file to be retrieved.

        :returns: A :class:`StationFile` object.

        Usage:
        .. code-block:: python

            file = station.file(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_file",
            resource_id=id
        )

        return StationFile(**response, _station=self._station)

    def upload(
        self,
        path: str,
        file: str
    ) -> StationFile:
        """
        Uploads a media file to the station.

        :param path: the/relative/path/to/file.mp3. (Yes follow this format.)
        :param file: The system path of the file to be uploaded.

        :returns: A :class:`StationFile` object for the newly uploaded file.

        Usage:
        .. code-block:: python

            file = station.file.upload(
                path="song/on/station.mp3",
                file="file/path/on/local/system.mp3"
            )
        """
        url = API_ENDPOINTS["station_files"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        upload_body = generate_file_upload_structure(path, file)

        response = self._station._request_handler.post(url, upload_body)

        return StationFile(**response, _station=self._station)

class PlaylistHelper:
    """Provides a set of functions to interact with playlists."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> Playlist:
        """
        Retrieves a specific playlist from the station.

        :param id: The numerical ID of the playlist to be retrieved.

        :returns: A :class:`Playlist` object.

        Usage:
        .. code-block:: python

            playlist = station.playlist(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_playlist",
            resource_id=id
        )

        return Playlist(**response, _station=self._station)

    def generate_schedule_item(
        self,
        start_time: str,
        end_time: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        days: Optional[List[str]] = None,
        loop_once: bool = False
    ) -> Dict[str, Any]:
        """
        Generates a single schedule item for a playlist.

        :param start_time: The starting time of the schedule, in this format: ``"HOUR:MINUTES"``.
        :param end_time: The ending time of the schedule, in this format: ``"HOUR:MINUTES"``.
        :param start_date: (Optional) The starting date of the schedule, in this format:
            ``"YEAR-MONTH-DAY"``. Default: ``None``.
        :param end_date: (Optional) The ending date of the schedule, in this format:
            ``"YEAR-MONTH-DAY"``. Default: ``None``.
        :param days: (Optional) A list of the days that the playlist will play. Default: ``None``.
        :param loop_once: Determines if the playlist will be looped through only once.
            Default: ``False``.

        Usage:
        .. code-block:: python

            item = station.playlist.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"],
                loop_once=False
            )
        """
        if days:
            days = [get_day_number(day.strip().lower()) for day in days]

        return {
            "start_time": int(start_time.replace(':', '')),
            "end_time": int(end_time.replace(':', '')),
            "start_date": start_date, # year-month-day
            "end_date": end_date, # year-month-day
            "days": days if days else [],
            "loop_once": loop_once
        }

    def generate_schedule_items(self, *args) -> List[Dict[str, Any]]:
        """
        Generates a list of schedule items for a playlist by using the
            :meth:``.generate_schedule_item`` function on each argument.

        :param args: Tuples in the format of
            ``(start_time, end_time, start_date, end_date, days, loop_once)``.
            ``start_time`` and ``end_time`` are mandatory values.
            The rest of the tuple's values can be ``None``.

        Usage:
        .. code-block:: python

            items = station.playlist.generate_schedule_items(
                ("12:32", "23:10", "2024-09-08", "2025-07-08", None, False),
                ("12:32", "23:10", "2024-09-18", "2025-07-08", ["monday", "thursday"], True)
            )
        """
        schedule_items = []

        for arg in args:
            if not isinstance(arg, tuple):
                message = "Each argument must be a tuple of values."
                raise ClientException(message)

            if len(arg) != 6:
                message = "Each tuple must have a value for start_time, end_time and loop_once as"\
                          "well as either a value or None for start_date, end_date and days."
                raise ClientException(message)

            if not isinstance(arg[0], str):
                message = "start_time must be a string."
                raise ClientException(message)

            if not isinstance(arg[1], str):
                message = "end_time must be a string."
                raise ClientException(message)

            if arg[2] and not isinstance(arg[2], str):
                message = "start_date must either be a string or None."
                raise ClientException(message)

            if arg[3] and not isinstance(arg[3], str):
                message = "end_date must either be a string or None."
                raise ClientException(message)

            if arg[4] and not isinstance(arg[4], list):
                message = "days must either be a list or None."
                raise ClientException(message)

            if not isinstance(arg[5], bool):
                message = "loop_once must be a boolean (True or False)."
                raise ClientException(message)

            schedule_items.append(self.generate_schedule_item(*arg))

        return schedule_items

    def create(
        self,
        name: str,
        source: PlaylistSources = PlaylistSources.SONGS,
        type: PlaylistTypes = PlaylistTypes.DEFAULT,
        order: PlaylistOrders = PlaylistOrders.SHUFFLE,
        avoid_duplicates: bool = True,
        allow_requests: bool = True,
        play_per_value: int = 0,
        weight: int = 3,
        include_in_on_demand: bool = False,
        is_jingle: bool = False,
        remote_url: Optional[str] = None,
        remote_type: PlaylistRemoteTypes = PlaylistRemoteTypes.STREAM,
        remote_buffer: int = 0,
        schedule: Optional[List[Dict[str, Any]]] = None
    ) -> Playlist:
        """
        Adds a new playlist to the station.

        :param name: The name of the playlist.
        :param source: Specify where the playlist gets its contents from.
            Default: ``PlaylistSources.SONGS``.
        :param type: The internal play-type of the playlist. Not needed if ``source`` is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``PlaylistTypes.DEFAULT``.
        :param order: Determines the playback order of the songs in the playlist. Not needed
            if ``source`` is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``PlaylistOrders.SHUFFLE``.
        :param avoid_duplicates: Determines whether duplicate artists and track titles will be
            avoided when playing media from this playlist. Not needed if ``source`` is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``True``.
        :param allow_requests: Determines whether users will be able to request media that is on
            this playlist. Not needed if ``source`` is set to ``PlaylistSources.REMOTE_URL``.
            Default: ``True``.
        :param play_per_value: This value acts as the corresponding value for the
            ``ONCE_PER_X_SONGS``, ``ONCE_PER_HOUR`` and ``ONCE_PER_X_MINUTES`` playlist types.
            Not needed if ``source`` is set to ``PlaylistSources.REMOTE_URL``. Default: ``0``.
        :param weight: The frequency of the playlist to be played when compared to playlists.
            This is the value for the ``DEFAULT`` playlist type. Not needed if ``source`` is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``3``.
        :param include_in_on_demand: Determines whether only songs that are in playlists with this
            setting enabled will be visible. Not needed if ``source`` is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``False``.
        :param is_jingle: Set to ``True`` to prevent metadata from being sent to the AutoDJ for
            files in this playlist. Not needed if ``source`` is set to
            ``PlaylistSources.REMOTE_URL``. Default: ``False``.
        :param remote_url: (Optional) The source URL for the playlist's contents. Not needed if
            ``source`` is set to ``PlaylistSources.SONGS``. Default: ``None``.
        :param remote_type: Specify the type of the ``remote_url``. Not needed if ``source`` is
            set to ``PlaylistSources.SONGS``. Default: ``PlaylistRemoteTypes.STREAM``.
        :param remote_buffer: The length of playback time that Liquidsoap should buffer when
            playing this remote playlist. Not needed if ``source`` is set to
            ``PlaylistSources.SONGS``. Default: ``0``.
        :param schedule: The structure representing the schedule list of the playlist. This can be
            generated using the :meth:`.generate_schedule_items` function. Default: ``None``.

        :returns: A :class:`Playlist` object for the newly created playlist.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import PlaylistTypes

            playlist = station.playlist.create(
                name="New playlist",
                type=PlaylistTypes.ONCE_PER_X_MINUTES,
                play_per_value=5
            )
        """
        if weight < 0 or weight > 25:
            message = "weight param must be between 1 and 25."
            raise ClientException(message)

        if not isinstance(type, PlaylistTypes):
            raise ClientException(generate_enum_error_text("type", PlaylistTypes))

        type = type.value

        if not isinstance(source, PlaylistSources):
            raise ClientException(generate_enum_error_text("source", PlaylistSources))

        source = source.value

        if not isinstance(order, PlaylistOrders):
            raise ClientException(generate_enum_error_text("order", PlaylistOrders))

        order = order.value

        if not isinstance(remote_type, PlaylistRemoteTypes):
            raise ClientException(generate_enum_error_text("remote_type", PlaylistRemoteTypes))

        remote_type = remote_type.value

        url = API_ENDPOINTS["station_playlists"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
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
            "include_in_requests": allow_requests,
            "include_in_on_demand": include_in_on_demand,
            "avoid_duplicates": avoid_duplicates,
            "schedule_items": schedule or []
        }

        response = self._station._request_handler.post(url, body)

        # This is probably inefficient, but the schedule_items attribute of the new Playlist won't
        # be returned otherwise. I'll find a better way soon.
        playlist_id = response['id']
        return self.__call__(playlist_id)

class PodcastHelper:
    """Provides a set of functions to interact with podcasts."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: str
    ) -> Podcast:
        """
        Retrieves a specific podcast from the station.

        :param id: The string ID of the podcast to be retrieved.

        :returns: A :class:`Podcast` object.

        Usage:
        .. code-block:: python

            podcast = station.podcast("string-id")
        """
        if not isinstance(id, str):
            raise ValueError("id param should be of type string.")

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=id
        )

        response = self._station._request_handler.get(url)

        return Podcast(**response, _station=self._station)

    # TODO: Art requires file upload
    def create(
        self,
        title: str,
        description: str,
        language: Languages,
        categories: Optional[List[PodcastCategories]] = None,
        author: Optional[str] = None,
        email: Optional[str] = None,
        website: Optional[str] = None
    ) -> Podcast:
        """
        Adds a podcast to the station.

        :param title: The title of the podcast.
        :param description: The description of the podcast.
        :param language: The language spoken in the podcast. Use the :class:`Languages` enum to
            select the language.
        :param categories: (Optional) A list of the categories that the podcast falls under.
            Each element of the list must be from the ``PodcastCategories`` class.
            Default: ``None``.
        :param author: (Optional) The name of the author of the podcast. Default: ``None``.
        :param email: (Optional) The email of the author of the podcast. Default: ``None``.
        :param website: (Optional) The link to the website that hosts the podcast.
            Default: ``None``.

        :returns: A :class:`Podcast` object for the newly created podcast.

        Usage:
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
        if not isinstance(language, Languages):
            raise ClientException(generate_enum_error_text("language", Languages))

        language = language.value

        url = API_ENDPOINTS["station_podcasts"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "title": title,
            "description": description,
            "language": language,
            "author": author or "",
            "email": email or "",
            "link": website or "",
            "categories": categories or []
        }

        response = self._station._request_handler.post(url, body)

        return Podcast(**response, _station=self._station)

class HLSStreamHelper:
    """Provides a set of functions to interact with hls streams."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> HLSStream:
        """
        Retrieves a specific HTTP Live Streaming (HLS) stream from the station.

        :param id: The numerical ID of the HLS stream to be retrieved.

        :returns: A :class:`HLSStream` object.

        Usage:
        .. code-block:: python

            hls_stream = station.hls_stream(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="hls_stream",
            resource_id=id
        )

        return HLSStream(**response, _station=self._station)

    def create(
        self,
        name: str,
        format: Formats = Formats.AAC,
        bitrate: Bitrates = Bitrates.BITRATE_128
    ) -> HLSStream:
        """
        Adds an HTTP Live Streaming (HLS) stream to the station.

        .. note::

            You need to provide a valid X-API-Key to use this function.

        :param name: The name of the HLS stream.
        :param format: The format of the HLS stream. Default: ``Formats.AAC``.
        :param bitrate: The bitrate of the HLS stream. Default: ``Bitrates.BITRATE_128``.

        :returns: A :class:`HLSStream` object for the newly created HLS stream.

       Usage:
        .. code-block:: python

            from AzuracastPy.enums import Formats, Bitrates

            hls_stream = station.hls_stream.create(
                name="New HLS Stream",
                format=Formats.MP3,
                bitrate=Bitrates.BITRATE_32
            )
        """
        if not isinstance(format, Formats):
            raise ClientException(generate_enum_error_text("format", Formats))

        format = format.value

        if not isinstance(bitrate, Bitrates):
            raise ClientException(generate_enum_error_text("bitrate", Bitrates))

        bitrate = bitrate.value

        url = API_ENDPOINTS['hls_streams'].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "name": name,
            "format": format,
            "bitrate": bitrate
        }

        response = self._station._request_handler.post(url, body)

        return HLSStream(**response, _station=self._station)

class SFTPUserHelper:
    """Provides a set of functions to interact with SFTP users."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> SFTPUser:
        """
        Retrieves a specific SFTP user from the station.

        :param id: The numerical ID of the SFTP user to be retrieved.

        :returns: A :class:`SFTPUser` object.

        Usage:
        .. code-block:: python

            sftp_user = station.sftp_user(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_sftp_user",
            resource_id=id
        )

        return SFTPUser(**response, _station=self)

    def create(
        self,
        username: str,
        password: str,
        public_keys: Optional[List[str]] = None
    ) -> SFTPUser:
        """
        Adds an SFTP user to the station.

        :param username: The username of the user.
        :param password: The password of the user.
        :param public_keys: (Optional) A list of public keys to be assigned to the user.
            Default: ``None``.

        :returns: A :class:`SFTPUser` object for the newly created SFTP user.

        Usage:
        .. code-block:: python

            sftp_user = station.sftp_user.create(
                username="Username",
                password="Password",
                public_keys=['key1', 'key2']
            )
        """
        url = API_ENDPOINTS["station_sftp_users"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "username": username,
            "password": password,
            "publicKeys": '\n'.join(public_keys) or ""
        }

        response = self._station._request_handler.post(url, body)

        return SFTPUser(**response, _station=self._station)

class WebhookHelper:
    """Provides a set of functions to interact with webhooks."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> Webhook:
        """
        Retrieves a specific SFTP user from the station.

        :param id: The numerical ID of the SFTP user to be retrieved.

        :returns: A :class:`SFTPUser` object.

        Usage:
        .. code-block:: python

            webhook = station.webhook(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_webhook",
            resource_id=id
        )

        return Webhook(**response, _station=self._station)

    def generate_webhook_config(
        self,
        webhook_url: Optional[str] = None,
        basic_auth_username: Optional[str] = None,
        basic_auth_password: Optional[str] = None,
        timeout: Optional[int] = None,
        to: Optional[str] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
        content: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        author: Optional[str] = None,
        thumbnail: Optional[str] = None,
        footer: Optional[str] = None,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        api: Optional[str] = None,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        instance_url: Optional[str] = None,
        access_token: Optional[str] = None,
        visibility: Optional[str] = None,
        rate_limit: Optional[str] = None,
        message_song_changed_live: Optional[str] = None,
        message_live_connect: Optional[str] = None,
        message_live_disconnect: Optional[str] = None,
        message_station_offline: Optional[str] = None,
        message_station_online: Optional[str] = None,
        station_id: Optional[str] = None,
        partner_id: Optional[str] = None,
        partner_key: Optional[str] = None,
        broadcastsubdomain: Optional[str] = None,
        apikey: Optional[str] = None,
        token: Optional[str] = None,
        measurement_id: Optional[str] = None,
        matomo_url: Optional[str] = None,
        site_id: Optional[str] = None
    ):
        """
        Generates a config object for a webhook.

        :returns: A dictionary of the not-``None`` attributes and their values.

        Usage:
        .. code-block:: python

            webhook_config = station.webhook.generate_webhook_config(
                subject="subject",
                message="message",
                to="to"
            )
        """
        return {
            key: value
            for key, value in locals().items()
            if value is not None and key != "self"
        }

    def create(
        self,
        name: str,
        type: WebhookConfigTypes,
        webhook_config: Dict[str, Any],
        triggers: Optional[List[WebhookTriggers]] = None
    ) -> Webhook:
        """
        Adds a webhook to the station.

        :param name: The name of the webhook.
        :param type: The type of the webhook. Use the :class:`WebhookConfigTypes` enum to select a
            type.
        :param webhook_config: The config object for the selected type. This can be generated using
            the :meth:`.generate_webhook_config` function.
        :param triggers: (Optional) A list of triggers for the webhook. Each element of the list
            must be from the :class:`WebhookTriggers` enum.

        :returns: A :class:`Webhook` object for the newly created webhook.

        Usage:
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
                triggers=[WebhookTriggers.STATION_ONLINE, WebhookTriggers.LIVE_CONNECT]
            )
        """
        if not isinstance(type, WebhookConfigTypes):
            message = "type param must be an attribute from the WebhookConfigTypes enum class."
            raise ClientException(message)

        type = type.value

        if triggers and not all(isinstance(trigger, WebhookTriggers) for trigger in triggers):
            message = "triggers param must be an attribute from the WebhookTriggers enum class."
            raise ClientException(message)

        triggers = [trigger.value for trigger in triggers]

        if not all(key in webhook_config for key in WEBHOOK_CONFIG_TEMPLATES[type]):
            message = "The provided 'webhook_config' is either incomplete or contains unneeded"\
                     f"keys for the '{type}' webhook. The '{type}' webhook's config must only"\
                     f"contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[type])}. Refer to the"\
                      "documentation for the config structure of each webhook type."
            raise ClientException(message)

        url = API_ENDPOINTS["station_webhooks"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "name": name,
            "type": type,
            "triggers": triggers or [],
            "config": webhook_config
        }

        response = self._station._request_handler.post(url=url, body=body)

        return Webhook(**response, _station=self._station)

class StreamerHelper:
    """Provides a set of functions to interact with streamers."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> Streamer:
        """
        Retrieves a specific streamer from the station.

        :returns: A :class:`Streamer` object.

        :param id: The numerical ID of the streamer to be retrieved.

        Usage:
        .. code-block:: python

            streamer = station.streamer(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_streamer",
            resource_id=id
        )

        return Streamer(**response, _station=self._station)

    def generate_schedule_item(
        self,
        start_time: str,
        end_time: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        days: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Generates a single schedule item for a streamer.

        :param start_time: The starting time of the schedule, in this format: ``"HOUR:MINUTES"``.
        :param end_time: The ending time of the schedule, in this format: ``"HOUR:MINUTES"``.
        :param start_date: (Optional) The starting date of the schedule, in this format:
            ``"YEAR-MONTH-DAY"``. Default: ``None``.
        :param end_date: (Optional) The ending date of the schedule, in this format:
            ``"YEAR-MONTH-DAY"``. Default: ``None``.
        :param days: (Optional) A list of the days that the playlist will play. Default: ``None``.

        Usage:
        .. code-block:: python

            item = station.streamer.generate_schedule_item(
                start_time="12:32",
                end_time="23:10",
                start_date="2024-09-08",
                end_date="2025-07-08",
                days=["monday", "thursday"]
            )
        """
        if days:
            days = [get_day_number(day.strip().lower()) for day in days]

        return {
            "start_time": int(start_time.replace(':', '')),
            "end_time": int(end_time.replace(':', '')),
            "start_date": start_date, # year-month-day
            "end_date": end_date, # year-month-day
            "days": days if days else []
        }

    def generate_schedule_items(self, *args):
        """
        Generates a list of schedule items for a streamer by using the
            :meth:`.generate_schedule_item` function on each argument.

        :param args: Tuples in the format of
            ``(start_time, end_time, start_date, end_date, days)``.
            Any of the tuple's values can be ``None``.

        Usage:
        .. code-block:: python

            items = station.streamer.generate_schedule_items(
                ("12:32", "23:10", "2024-09-08", "2025-07-08", None),
                ("12:32", "23:10", "2024-09-18", "2025-07-08", ["monday", "thursday"])
            )
        """
        schedule_items = []

        for arg in args:
            if not isinstance(arg, tuple):
                message = "Each argument must be a tuple of values."
                raise ClientException(message)

            if len(arg) != 5:
                message = "Each tuple must have a value or None for start_time, end_time, "\
                          "start_date, end_date and days."
                raise ClientException(message)

            if not isinstance(arg[0], str):
                message = "start_time must be a string."
                raise ClientException(message)

            if not isinstance(arg[1], str):
                message = "end_time must be a string."
                raise ClientException(message)

            if arg[2] and not isinstance(arg[2], str):
                message = "start_date must either be a string or None."
                raise ClientException(message)

            if arg[3] and not isinstance(arg[3], str):
                message = "end_date must either be a string or None."
                raise ClientException(message)

            if arg[4] and not isinstance(arg[4], list):
                message = "days must either be a list or None."
                raise ClientException(message)

            schedule_items.append(self.generate_schedule_item(*arg))

        return schedule_items

    def create(
        self,
        username: str,
        password: str,
        display_name: Optional[str] = None,
        comments: Optional[str] = None,
        is_active: bool = True,
        enforce_schedule: bool = False,
        schedule: Optional[List[Dict[str, Any]]] = None
    ) -> Streamer:
        """
        Adds a streamer to the station.

        :param username: The streamer's username.
        :param password: The streamer's password.
        :param display_name: (Optional) The streamer's display_name. Leave as ``None`` to use the
            ``username`` as the value. Default: ``None``.
        :param comments: (Optional) Internal notes or comments about the streamer.
            Default: ``None``.
        :param is_active: Determines whether this streamer can log in and stream.
            Default: ``True``.
        :param enforce_schedule: Determines whether this streamer will only be able to connect
            during their scheduled broadcast times. Default: ``False``.
        :param schedule: The structure representing the schedule list of the streamer. This can be
            generated using the :meth:`.generate_schedule_items` function. Default: ``None``.

        :returns: A :class:`Streamer` object for the newly created streamer.

        Usage:
        .. code-block:: python

        streamer = station.streamer.create(
            username="Username",
            password="Password",
            comments="Never gonna give you up."
        )
        """
        url = API_ENDPOINTS["station_streamers"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "streamer_username": username,
            "streamer_password": password,
            "display_name": display_name or username,
            "comments": comments or "",
            "is_active": is_active,
            "enforce_schedule": enforce_schedule,
            "schedule_items": schedule or []
        }

        response = self._station._request_handler.post(url, body)

        # This is probably inefficient, but the schedule_items attribute of the new Streamer won't
        # be returned otherwise. I'll find a better way soon.
        streamer_id = response['id']
        return self.__call__(streamer_id)

class RemoteRelayHelper:
    """Provides a set of functions to interact with remote relays."""
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: int
    ) -> RemoteRelay:
        """
        Retrieves a specific remote relay from the station.

        :param id: The numerical ID of the remote relay to be retrieved.

        :returns: A :class:`RemoteRelay` object.

        Usage:
        .. code-block:: python

            remote_relay = station.remote_relay(1)
        """
        response = _request_single_instance_of_station_resource(
            station=self._station,
            resource_name="station_remote_relay_item",
            resource_id=id
        )

        return RemoteRelay(**response, _station=self._station)

    def create(
        self,
        station_listening_url: str,
        remote_type: RemoteTypes = RemoteTypes.ICECAST,
        display_name: Optional[str] = None,
        station_listening_mount_point: Optional[str] = None,
        station_admin_password: Optional[str] = None,
        show_on_public_pages: bool = True,
        enable_autodj: bool = False,
        autodj_format: Formats = Formats.MP3,
        autodj_bitrate: Bitrates = Bitrates.BITRATE_128,
        station_source_port: Optional[int] = None,
        station_source_mount_point: Optional[str] = None,
        station_source_username: Optional[str] = None,
        station_source_password: Optional[str] = None,
        is_public: bool = False
    ) -> RemoteRelay:
        """
        Adds a remote relay to the station.

        :param station_listening_url: If the remote radio URL is
            "http://station.example.com:8000/radio.mp3", enter "http://station.example.com:8000".
        :param remote_type: The type of the remote station. Default: ``RemoteTypes.ICECAST``.
        :param display_name: The display name of this relay when viewing it on administrative or
            public pages. Leave as ``None`` to automatically generate one. Default: ``None``.
        :param station_listening_mount_point:
        :param station_admin_password: To retrieve detailed unique listeners and client details,
            an administrator password is often required.
        :param show_on_public_pages: Determines whether listeners can select this relay on this
            station's public pages. Default: ``True``.
        :param enable_autodj: Determines whether the AutoDJ on this installation will automatically
            play music to this mount point. Default: ``None``.
        :param autodj_format: The format of the music played by AutoDJ. Default: ``Formats.MP3``.
        :param autodj_bitrate: The bitrate of the music played by AutoDJ.
            Default: ``Bitrates.BITRATE_128``.
        :param station_source_port:
        :param station_source_mount_point:
        :param station_source_username: (Optional) If you are broadcasting using AutoDJ, enter the
            source username here. This may be blank. Default: ``None``.
        :param station_source_password: (Optional) If you are broadcasting using AutoDJ, enter the
            source password here. Default: ``None``.
        :param is_public: Set to ``True`` to advertise this relay on "Yellow Pages" public radio
            directories. Default: ``False``.

        :returns: A :class:`RemoteRelay` object for the newly created remote relay.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import Formats

            remote_relay = station.remote_relay.create(
                station_listening_url="http://station.example.com:8000",
                display_name="Display name",
                autodj_format=Formats.MP3
            )
        """
        if not isinstance(remote_type, RemoteTypes):
            raise ClientException(generate_enum_error_text("remote_type", RemoteTypes))

        remote_type = remote_type.value

        if not isinstance(autodj_format, Formats):
            raise ClientException(generate_enum_error_text("autodj_format", Formats))

        autodj_format = autodj_format.value

        if not isinstance(autodj_bitrate, Bitrates):
            raise ClientException(generate_enum_error_text("autodj_bitrate", Bitrates))

        autodj_bitrate = autodj_bitrate.value

        url = API_ENDPOINTS["station_remote_relays"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "display_name": display_name or "",
            "is_visible_on_public_pages": show_on_public_pages,
            "type": remote_type,
            "enable_autodj": enable_autodj,
            "autodj_format": autodj_format,
            "autodj_bitrate": autodj_bitrate,
            "url": station_listening_url,
            "mount": station_listening_mount_point or "",
            "admin_password": station_admin_password or "",
            "source_port": station_source_port,
            "source_mount": station_source_mount_point or "",
            "source_username": station_source_username or "",
            "source_password": station_source_password or "",
            "is_public": is_public
        }

        response = self._station._request_handler.post(url, body)

        return RemoteRelay(**response, _station=self._station)

class QueueHelper:
    def __init__(
        self,
        _station
    ):
        self._station = _station

    def __call__(
        self,
        id: Optional[int] = None
    ) -> Union[List[QueueItem], QueueItem]:
        """
        Retrieves a specific remote relay from the station.

        :param id: (Optional) The numerical ID of the queue item to be retrieved.
            If None, all items in the queue are retrieved. Default: ``None``.

        :returns: A list of :class:`QueueItem` objects or a single :class:`QueueItem` object.

        Usage:
        .. code-block:: python

            queue = station.queue()
            queue_item = station.queue(1)
        """
        url = API_ENDPOINTS["station_queue"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        response = self._station._request_handler.get(url)

        queue = [QueueItem(**qi, _station=self._station) for qi in response]

        # ---------------------------------------------
        # Had to do this because, at the time of development, the API doesn't support a GET request
        # for a single queue item. Throws a 405 error instead.
        # ---------------------------------------------
        # If a valid id was given, return that element.
        if id:
            if type(id) is not int or id - 1 < 0:
                raise ClientException("id param must be a non-negative integer")

            id = id - 1 # Convert to zero-based index form.

            try:
                return queue[id]
            except IndexError:
                raise ClientException("Requested resource not found.")

        # Else, return the entire queue.
        return queue
