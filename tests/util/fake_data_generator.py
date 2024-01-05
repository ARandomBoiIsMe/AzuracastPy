from AzuracastPy.models.station import Station
from AzuracastPy.models.station_file import StationFile
from AzuracastPy.models.mount_point import MountPoint
from AzuracastPy.models.playlist import Playlist
from AzuracastPy.models.requestable_song import RequestableSong
from AzuracastPy.models.song_history import SongHistory
from AzuracastPy.models.schedule_time import ScheduleTime
from AzuracastPy.models.listener import Listener
from AzuracastPy.models.station_status import StationStatus
from AzuracastPy.models.podcast import Podcast
from AzuracastPy.models.podcast_episode import PodcastEpisode

def return_fake_station_json(id: int):
    return {
        "id":id,
        "name":"XXXX",
        "shortcode":"XXXX",
        "description":"XXXX",
        "frontend":"XXXX",
        "backend":"XXXX",
        "listen_url":"XXXX",
        "url":"XXXX",
        "public_player_url":"XXXX",
        "playlist_pls_url":"XXXX",
        "playlist_m3u_url":"XXXX",
        "is_public":True,
        "mounts":[
            {
                "id":1,
                "name":"XXXX",
                "url":"XXXX",
                "bitrate":128,
                "format":"XXXX",
                "listeners":{
                    "total":0,
                    "unique":0,
                    "current":0
                },
                "path":"XXXX",
                "is_default":True
            }
        ],
        "remotes":[],
        "hls_enabled":False,
        "hls_is_default":False,
        "hls_url":None,
        "hls_listeners":0
    }

def return_fake_station_instance(id: int):
    return Station(**return_fake_station_json(id))

def return_fake_file_json(id: int):
    return {
        "unique_id":"XXXX","album":None,"genre":None,"lyrics":None,"isrc":None,
        "length":408.22,"length_text":"XXXX","path":"XXXX",
        "mtime":1703965645,"amplify":None,"fade_overlap":None,"fade_in":None,"fade_out":None,
        "cue_in":None,"cue_out":None,"art_updated_at":1703965645,
        "playlists":[{"id":1,"name":"XXXX","weight":4}],"id":id,
        "song_id":"XXXX","text":"XXXX",
        "artist":"XXXX","title":"XXXX","custom_fields":[],
        "links":{"self":"XXXX"}
    }

def return_fake_file_instance(id: int):
    return StationFile(**return_fake_file_json(id))

def return_fake_mount_point_json(id: int):
    return {
        "name": "XXXX",
        "display_name": "XXXX",
        "is_visible_on_public_pages": True,
        "is_default": True,
        "is_public": False,
        "fallback_mount": None,
        "relay_url": None,
        "authhash": None,
        "max_listener_duration": 0,
        "enable_autodj": True,
        "autodj_format": "mp3",
        "autodj_bitrate": 128,
        "custom_listen_url": None,
        "intro_path": None,
        "frontend_config": None,
        "listeners_unique": 0,
        "listeners_total": 0,
        "id": id,
        "links": {
            "self": "XXXX",
            "intro": "XXXX",
            "listen": "XXXX"
        }
    }

def return_fake_mount_point_instance(id: int):
    return MountPoint(**return_fake_mount_point_json(id))

def return_fake_playlist_json(id: int):
    return {
        "name": "XXXX",
        "type": "XXXX",
        "source": "XXXX",
        "order": "XXXX",
        "remote_url": None,
        "remote_type": "XXXX",
        "remote_buffer": 0,
        "is_enabled": True,
        "is_jingle": False,
        "play_per_songs": 0,
        "play_per_minutes": 0,
        "play_per_hour_minute": 0,
        "weight": 3,
        "include_in_requests": True,
        "include_in_on_demand": False,
        "backend_options": [
            ""
        ],
        "avoid_duplicates": True,
        "played_at": 1704407702,
        "queue_reset_at": 1704406957,
        "schedule_items": [
            {
                "start_time": 0,
                "end_time": 2300,
                "start_date": "2024-01-19",
                "end_date": None,
                "days": [],
                "loop_once": False,
                "id": 1
            },
            {
                "start_time": 1400,
                "end_time": 2045,
                "start_date": None,
                "end_date": None,
                "days": [
                    3,
                    7
                ],
                "loop_once": False,
                "id": 2
            }
        ],
        "id": id,
        "short_name": "XXXX",
        "num_songs": 8,
        "total_length": 1774,
        "links": {
            "self": "XXXX",
            "toggle": "XXXX",
            "clone": "XXXX",
            "queue": "XXXX",
            "import": "XXXX",
            "reshuffle": "XXXX",
            "applyto": "XXXX",
            "empty": "XXXX",
            "export": {
                "pls": "XXXX",
                "m3u": "XXXX"
            }
        }
    }

def return_fake_playlist_instance(id: int):
    return Playlist(**return_fake_playlist_json(id))

def return_fake_requestable_song_json():
    return {
        "request_id": "XXXX",
        "request_url": "XXXX",
        "song": {
            "id": "XXXX",
            "text": "XXXX",
            "artist": "XXXX",
            "title": "XXXX",
            "album": "XXXX",
            "genre": "XXXX",
            "isrc": "XXXX",
            "lyrics": "XXXX",
            "art": "XXXX",
            "custom_fields": []
        }
    }

def return_fake_requestable_song_instance():
    return RequestableSong(**return_fake_playlist_json())

def return_fake_song_history_json():
    return {
        "sh_id": 536,
        "played_at": 1704485288,
        "duration": 356,
        "playlist": "",
        "streamer": "",
        "is_request": False,
        "song": {
            "id": "XXXX",
            "text": "XXXX",
            "artist": "XXXX",
            "title": "XXXX",
            "album": "",
            "genre": "",
            "isrc": "",
            "lyrics": "",
            "art": "XXXX",
            "custom_fields": []
        },
        "listeners_start": 0,
        "listeners_end": 0,
        "delta_total": 0,
        "is_visible": True
    }

def return_fake_song_history_instance():
    return SongHistory(**return_fake_song_history_json())

def return_fake_schedule_time_json():
    return {
        "id": 12345,
        "type": "XXXX",
        "name": "XXXX",
        "title": "XXXX",
        "description": "XXXX",
        "start_timestamp": 1667545600,
        "start": "2023-11-02T00:00:00",
        "end_timestamp": 1667632000,
        "end": "2023-11-03T00:00:00",
        "is_now": False
    }

def return_fake_schedule_time_instance():
    return ScheduleTime(**return_fake_schedule_time_json())

def return_fake_listener_json():
    return {
        "ip": "XXXX",
        "user_agent": "XXXX",
        "hash": "XXXX",
        "mount_is_local": False,
        "mount_name": "XXXX",
        "connected_on": 1667545600,
        "connected_until": 1667632000,
        "connected_time": 3600,
        "device": {
            "client": "XXXX",
            "is_browser": True,
            "is_mobile": False,
            "is_bot": False,
            "browser_family": "XXXX",
            "os_family": "XXXX"
        },
        "location": {
            "description": "XXXX",
            "region": "XXXX",
            "city": "XXXX",
            "country": "XXXX",
            "lat": 123.456,
            "lon": -78.901
        }
    }

def return_fake_listener_instance():
    return Listener(**return_fake_listener_json())

def return_fake_station_status_json():
    return {
        "backend_running": False,
        "frontend_running": True,
        "station_has_started": True,
        "station_needs_restart": False
    }

def return_fake_station_status_instance():
    return StationStatus(**return_fake_station_status_json())

def return_fake_podcast_json():
    return {
        "id": "XXXX",
        "storage_location_id": 4,
        "title": "XXXX",
        "link": "XXXX",
        "description": "XXXX",
        "language": "XXXX",
        "author": "XXXX",
        "email": "XXXX",
        "has_custom_art": True,
        "art": "XXXX",
        "art_updated_at": 0,
        "categories": [],
        "episodes": [],
        "links": {
            "self": "XXXX",
            "episodes": "XXXX",
            "public_episodes": "XXXX",
            "public_feed": "XXXX",
            "art": "XXXX",
            "episode_new_art": "XXXX",
            "episode_new_media": "XXXX"
        }
    }

def return_fake_podcast_instance():
    return Podcast(**return_fake_podcast_json())

def return_fake_podcast_episode_json():
    return {
        "id": "XXXX",
        "title": "XXXX",
        "description": "XXXX",
        "explicit": False,
        "publish_at": 1704491460,
        "has_media": True,
        "media": {
            "id": "XXXX",
            "original_name": "XXXX",
            "length": 0,
            "length_text": "XXXX",
            "path": "XXXX"
        },
        "has_custom_art": True,
        "art": "XXXX",
        "art_updated_at": 1704491337,
        "links": {
            "self": "XXXX",
            "public": "XXXX",
            "download": "XXXX",
            "art": "XXXX",
            "media": "XXXX"
        }
    }

def return_fake_podcast_episode_instance():
    return PodcastEpisode(**return_fake_podcast_episode_json())