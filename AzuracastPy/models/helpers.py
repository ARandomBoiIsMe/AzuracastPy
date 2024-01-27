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

from AzuracastPy.util.media_util import generate_file_upload_structure
from AzuracastPy.util.general_util import get_language_code, get_day_number
from AzuracastPy.exceptions import ClientException
from AzuracastPy.constants import (
    API_ENDPOINTS,
    WEBHOOK_CONFIG_TEMPLATES,
    WEBHOOK_TRIGGERS,
    FORMATS,
    BITRATES,
    PLAYLIST_ORDERS,
    PLAYLIST_TYPES,
    PLAYLIST_SOURCES,
    PLAYLIST_REMOTE_TYPES
)

from typing import Optional, Union, Dict, Any, List

def _request_single_instance_of_station_resource(
    station,
    resource_name,
    resource_id
):
    if type(resource_id) is not int:
        raise TypeError("id param should be of type int.")
        
    if resource_id < 0:
        raise ValueError("id must be a non-negative number.")
    
    url = API_ENDPOINTS[resource_name].format(
        radio_url=station._request_handler.radio_url,
        station_id=station.id,
        id=resource_id
    )

    return station._request_handler.get(url)

class MountPointHelper:
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
        mount_point_url: str, 
        display_name: Optional[str] = None, 
        show_on_public_pages: bool = True,
        is_default: bool = False, 
        is_public: bool = True, 
        relay_stream_url: Optional[str] = None,
        max_listener_duration: int = 0, 
        fallback_mount: str = "/error.mp3", 
        enable_autodj: bool = True,
        autodj_format: str = "mp3", 
        autodj_bitrate: int = 128, 
        custom_url: Optional[str] = None,
        custom_frontend_config: Optional[Union[Dict[str, Any], str]] = None 
    ) -> MountPoint:
        """
        Adds a mount point to the station.

        :param mount_point_url: 
        :param display_name: (Optional) Default: ``None``
        :param show_on_public_pages:
        :param is_default:
        :param is_public:
        :param relay_stream_url: (Optional) Default: ``None``
        :param max_listener_duration:
        :param fallback_mount:
        :param enable_autodj:
        :param autodj_format:
        :param autodj_bitrate:
        :param custom_url: (Optional) Default: ``None``
        :param custom_frontend_config: (Optional) Default: ``None``

        :returns: A :class:`MountPoint` object for the newly created mount point.
        """
        url = API_ENDPOINTS["station_mount_points"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "name": mount_point_url,
            "display_name": display_name if display_name else "",
            "is_visible_on_public_pages": show_on_public_pages,
            "is_default": is_default,
            "is_public": is_public,
            "fallback_mount": fallback_mount,
            "relay_url": relay_stream_url if relay_stream_url else "",
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
        url = API_ENDPOINTS["station_files"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        upload_body = generate_file_upload_structure(path, file)

        response = self._station._request_handler.post(url, upload_body)

        return StationFile(**response, _station=self._station)
    
class PlaylistHelper:
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
        Retrieves a specific uploaded music file from the station.

        :param id: The numerical ID of the file to be retrieved.

        :returns: A :class:`StationFile` object.
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
        days: List[str] = None,
        loop_once: bool = False
    ) -> Dict[str, Any]:
        days = [get_day_number(day.strip().lower()) for day in days]

        return {
            "start_time": int(start_time.replace(':', '')),
            "end_time": int(end_time.replace(':', '')),
            "start_date": start_date, # year-month-day
            "end_date": end_date, # year-month-day
            "days": days if days else [],
            "loop_once": loop_once
        }
    
    def create(
        self, 
        name: str, 
        type: str = "default", 
        source: str = "songs", 
        order: str = "shuffle",
        remote_url: Optional[str] = None, 
        remote_type: str = "stream", 
        remote_buffer: int = 0,
        play_per_value: int = 0, 
        weight: int = 3, 
        include_in_requests: bool = True, 
        include_in_on_demand: bool = False, 
        avoid_duplicates: bool = True, 
        is_jingle: bool = False,
        schedule: Optional[List[Dict[str, Any]]] = None
    ):
        if type not in PLAYLIST_TYPES:
            message = f"type param must be one of: {', '.join(PLAYLIST_TYPES)}"
            raise ClientException(message)
        
        if source not in PLAYLIST_SOURCES:
            message = f"source param must be one of: {', '.join(PLAYLIST_SOURCES)}"
            raise ClientException(message)
        
        if order not in PLAYLIST_ORDERS:
            message = f"order param must be one of: {', '.join(PLAYLIST_ORDERS)}"
            raise ClientException(message)
        
        if remote_type not in PLAYLIST_REMOTE_TYPES:
            message = f"remote_type param must be one of: {', '.join(PLAYLIST_REMOTE_TYPES)}"
            raise ClientException(message)
        
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
            "include_in_requests": include_in_requests,
            "include_in_on_demand": include_in_on_demand,
            "avoid_duplicates": avoid_duplicates,
            "schedule_items": schedule if schedule else []
        }

        response = self._station._request_handler.post(url, body)

        # This is probably inefficient, but the schedule_items attribute of the new Playlist won't be 
        # returned otherwise. I'll find a better way soon.
        playlist_id = response['id']
        return self.__call__(playlist_id)
    
class PodcastHelper:
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
        """
        if type(id) is not str:
            raise TypeError("id param should be of type string.")
        
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
        language: str, 
        categories: Optional[List[str]] = None,
        author: Optional[str] = None, 
        email: Optional[str] = None, 
        website: Optional[str] = None
    ) -> Podcast:
        """
        Adds a podcast to the station.

        :param title: The title of the podcast.
        :param description: The description of the podcast.
        :param language: The language spoken in the podcast. Either the full language name or its equivalent two-letter language code.
        :param categories: (Optional) A list of the categories that the podcast falls under. Default: ``None``.
        :param author: (Optional) The name of the author of the podcast. Default: ``None``.
        :param email: (Optional) The email of the author of the podcast. Default: ``None``.
        :param website: (Optional) The link to the website that hosts the podcast. Default: ``None``.

        :returns: A :class:`Podcast` object for the newly created podcast.
        """
        url = API_ENDPOINTS["station_podcasts"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        language = language.lower()
        if len(language) > 2:
            language = language.lower().replace(' ', '_')
            language = get_language_code(language)

        body = {
            "title": title,
            "description": description,
            "language": language,
            "author": author if author else "",
            "email": email if email else "",
            "link": website if website else "",
            "categories": categories if categories else []
        }

        response = self._station._request_handler.post(url, body)

        return Podcast(**response, _station=self._station)
    
class HLSStreamHelper:
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
        format: str = "aac",
        bitrate: int = 128
    ) -> HLSStream:
        """
        Adds an HTTP Live Streaming (HLS) stream to the station.
        
        .. note::

            You need to provide a valid X-API-Key to use this function.

        :param name: The name of the HLS stream.
        :param format: The format of the HLS stream. Default: ``"aac"``.
        :param bitrate: The bitrate of the HLS stream. Default: ``128``.

        :returns: A :class:`HLSStream` object for the newly created HLS stream.
        """
        if format not in FORMATS:
            message = f"format param must be one of: {', '.join(FORMATS)}"
            raise ClientException(message)
        
        if bitrate not in BITRATES:
            message = f"bitrate param must be one of: {', '.join(BITRATES)}"
            raise ClientException(message)

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

        :param username:
        :param password:
        :param public_keys:

        :returns: A :class:`SFTPUser` object for the newly created SFTP user.
        """
        url = API_ENDPOINTS["station_sftp_users"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "username": username,
            "password": password,
            "publicKeys": '\n'.join(public_keys) if public_keys else ""
        }

        response = self._station._request_handler.post(url, body)

        return SFTPUser(**response, _station=self._station)
    
class WebhookHelper:
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
        return {
            key: value
            for key, value in locals().items()
            if value is not None and key != "self"
        }
    
    def create(
        self, 
        name: str, 
        type: str, 
        webhook_config: Dict[str, Any], 
        triggers: Optional[List[str]] = None 
    ) -> Webhook:
        """
        Adds a webhook to the station.

        :param name:
        :param type:
        :param webhook_config:
        :param triggers:

        :returns: A :class:`Webhook` object for the newly created webhook.
        """
        valid_types = WEBHOOK_CONFIG_TEMPLATES.keys()
        if type not in valid_types:
            message = f"type param must be one of {', '.join(valid_types)}"
            raise ClientException(message)
        
        if triggers is not None:
            if not all(trigger in WEBHOOK_TRIGGERS for trigger in triggers):
                message = f"Invalid trigger found in triggers list. Elements in trigger list must be one of: {', '.join(WEBHOOK_TRIGGERS)}."
                raise ClientException(message)
        
        if not all(key in webhook_config for key in WEBHOOK_CONFIG_TEMPLATES[type]):
            message = f"The provided 'webhook_config' is either incomplete or contains unneeded keys for the '{type}' webhook. The '{type}' webhook's config must only contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[type])}. Refer to the documentation for the config structure of each webhook type."
            raise ClientException(message)
        
        url = API_ENDPOINTS["station_webhooks"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )
        
        body = {
            "name": name,
            "type": type,
            "triggers": triggers if triggers else [],
            "config": webhook_config
        }

        response = self._station._request_handler.post(url=url, body=body)

        return Webhook(**response, _station=self._station)
    
class StreamerHelper:
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
        days: List[str] = None
    ) -> Dict[str, Any]:
        days = [get_day_number(day.strip().lower()) for day in days]

        return {
            "start_time": int(start_time.replace(':', '')),
            "end_time": int(end_time.replace(':', '')),
            "start_date": start_date, # year-month-day
            "end_date": end_date, # year-month-day
            "days": days if days else []
        }
    
    def create(
        self, 
        streamer_username: str, 
        streamer_password: str, 
        display_name: Optional[str] = None,
        comments: Optional[str] = None, 
        is_active: bool = True, 
        enforce_schedule: bool = False,
        schedule: Optional[List[Dict[str, Any]]] = None
    ) -> Streamer:
        """
        Adds a streamer to the station.

        :param streamer_username:
        :param streamer_password:
        :param display_name:
        :param comments:
        :param is_active:
        :param enforce_schedule:
        :param schedule:

        :returns: A :class:`Streamer` object for the newly created streamer.
        """
        url = API_ENDPOINTS["station_streamers"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "streamer_username": streamer_username,
            "streamer_password": streamer_password,
            "display_name": display_name if display_name else "",
            "comments": comments if comments else "",
            "is_active": is_active,
            "enforce_schedule": enforce_schedule,
            "schedule_items": schedule if schedule else []
        }

        response = self._station._request_handler.post(url, body)

        # This is probably inefficient, but the schedule_items attribute of the new Streamer won't be 
        # returned otherwise. I'll find a better way soon.
        streamer_id = response['id']
        return self.__call__(streamer_id)
    
class RemoteRelayHelper:
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
        remote_type: str = "icecast", 
        display_name: Optional[str] = None,
        station_listening_mount_point: Optional[str] = None, 
        station_admin_password: Optional[str] = None,
        show_on_public_pages: bool = True, 
        enable_autodj: bool = False, 
        autodj_format: str = "mp3",
        autodj_bitrate: int = 128, 
        station_source_port: Optional[int] = None,
        station_source_mount_point: Optional[str] = None, 
        station_source_username: Optional[str] = None,
        station_source_password: Optional[str] = None, 
        is_public: bool = False
    ) -> RemoteRelay:
        """
        Adds a remote relay to the station.

        :param station_listening_url:
        :param remote_type:
        :param display_name:
        :param station_listening_mount_point:
        :param station_admin_password:
        :param show_on_public_pages:
        :param enable_autodj:
        :param autodj_format:
        :param autodj_bitrate:
        :param station_source_port:
        :param station_source_mount_point:
        :param station_source_username:
        :param station_source_password:
        :param is_public:

        :returns: A :class:`RemoteRelay` object for the newly created remote relay.
        """
        if remote_type not in ["icecast", "shoutcast1", "shoutcast2"]:
            message = "remote_type param has to be one of: icecast, shoutcast1, shoutcast2"
            raise ClientException(message)
        
        if autodj_format not in FORMATS:
            message = f"autodj_format param must be one of: {', '.join(FORMATS)}"
            raise ClientException(message)
        
        if autodj_bitrate not in BITRATES:
            message = f"autodj_bitrate param must be one of: {', '.join(BITRATES)}"
            raise ClientException(message)

        url = API_ENDPOINTS["station_remote_relays"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        body = {
            "display_name": display_name if display_name else "",
            "is_visible_on_public_pages": show_on_public_pages,
            "type": remote_type,
            "enable_autodj": enable_autodj,
            "autodj_format": autodj_format,
            "autodj_bitrate": autodj_bitrate,
            "url": station_listening_url,
            "mount": station_listening_mount_point if station_listening_mount_point else "",
            "admin_password": station_admin_password if station_admin_password else "",
            "source_port": station_source_port,
            "source_mount": station_source_mount_point if station_source_mount_point else "",
            "source_username": station_source_username if station_source_username else "",
            "source_password": station_source_password if station_source_password else "",
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

        :param id: (Optional) The numerical ID of the queue item to be retrieved. If None, all items in the queue are retrieved. Default: ``None``

        :returns: A list of :class:`QueueItem` objects or a single :class:`QueueItem` object.
        """
        url = API_ENDPOINTS["station_queue"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id
        )

        response = self._station._request_handler.get(url)

        queue = [QueueItem(**qi, _station=self._station) for qi in response]

        # ---------------------------------------------
        # Had to do this because, at the time of development, the API doesn't support a GET request for a 
        # single queue item. Throws a 405 error instead.
        # ---------------------------------------------
        # If a valid id was given, return that element.
        if id is not None:
            if type(id) is not int:
                pass

            id = id - 1 # Convert to zero-based index form.
            if id < 0:
                raise ClientException("Requested resource not found.")
            
            try:
                return queue[id]
            except IndexError:
                raise ClientException("Requested resource not found.")

        # Else, return the entire queue.
        return queue     