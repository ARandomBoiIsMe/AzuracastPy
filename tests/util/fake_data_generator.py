from AzuracastPy.models import Station
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
from AzuracastPy.models.queue_item import QueueItem
from AzuracastPy.models.remote_relay import RemoteRelay
from AzuracastPy.models.sftp_user import SFTPUser
from AzuracastPy.models.streamer import Streamer
from AzuracastPy.models.webhook import Webhook

def return_fake_station_json(id: int):
    return {
        "id": id,
        "name": "Yet Another Radio",
        "shortcode": "yet_another_radio",
        "description": "",
        "frontend": "icecast",
        "backend": "liquidsoap",
        "listen_url": "http://localhost:8000/kiki",
        "url": "",
        "public_player_url": "http://localhost/public/yet_another_radio",
        "playlist_pls_url": "http://localhost/public/yet_another_radio/playlist.pls",
        "playlist_m3u_url": "http://localhost/public/yet_another_radio/playlist.m3u",
        "is_public": True,
        "mounts": [
            {
                "id": 4,
                "name": "/hi (128kbps MP3)",
                "url": "http://localhost:8000/kiki",
                "bitrate": 128,
                "format": "mp3",
                "listeners": {
                    "total": 0,
                    "unique": 0,
                    "current": 0
                },
                "path": "/kiki",
                "is_default": True
            },
            {
                "id": 5,
                "name": "hohoho",
                "url": "https://z",
                "bitrate": None,
                "format": None,
                "listeners": {
                    "total": 0,
                    "unique": 0,
                    "current": 0
                },
                "path": "/bleh",
                "is_default": False
            }
        ],
        "remotes": [
            {
                "id": 7,
                "name": "yohppppohpeo",
                "url": "https://yuh",
                "bitrate": None,
                "format": None,
                "listeners": {
                    "total": 0,
                    "unique": 0,
                    "current": 0
                }
            },
            {
                "id": 8,
                "name": "another name who dis",
                "url": "https://yuh",
                "bitrate": 128,
                "format": "ogg",
                "listeners": {
                    "total": 0,
                    "unique": 0,
                    "current": 0
                }
            }
        ],
        "hls_enabled": True,
        "hls_is_default": False,
        "hls_url": "http://localhost/hls/yet_another_radio/live.m3u8",
        "hls_listeners": 0
    }

def return_fake_station_instance(id: int):
    return Station(**return_fake_station_json(id), _request_handler=None)

def return_fake_file_json(id: int):
    return {
        "unique_id": "53bff3de9429ad36ad9bd533",
        "album": "THE INSPECTION",
        "genre": None,
        "lyrics": None,
        "isrc": None,
        "length": 127.37,
        "length_text": "2:07",
        "path": "songs/y2mate.com_-_cochise__megaman_official_audio.mp3",
        "mtime": 1707328093,
        "amplify": None,
        "fade_overlap": None,
        "fade_in": None,
        "fade_out": None,
        "cue_in": None,
        "cue_out": None,
        "art_updated_at": 1703965646,
        "playlists": [
            {
                "id": 7,
                "name": "IM HERE",
                "weight": 2
            }
        ],
        "id": id,
        "song_id": "937b60a479ee80c96db217721afca1fb",
        "text": "Cochise - MEGAMAN",
        "artist": "Cochise",
        "title": "MEGAMAN",
        "custom_fields": {
            "bro_thinks_hes_funny": None,
            "new_name_who_dis": None,
            "lol_if_i_dont_wanna_8_lel": None,
            "lolpleasework": None,
            "i thought this wouldn't work     sff s ';-;": None,
            "whats_up": None
        },
        "links": {
            "self": "http://localhost/api/station/1/file/4"
        }
    }

def return_fake_file_instance(id: int):
    return StationFile(**return_fake_file_json(id), _station=None)

def return_fake_mount_point_json(id: int):
    return {
        "name": "/hey",
        "display_name": "/hey (128kbps MP3)",
        "is_visible_on_public_pages": True,
        "is_default": False,
        "is_public": True,
        "fallback_mount": "/error.mp3",
        "relay_url": "",
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
            "self": "http://localhost/api/station/1/mount/6",
            "intro": "http://localhost/api/station/1/mount/6/intro",
            "listen": "http://localhost:8000/hey"
        }
    }

def return_fake_mount_point_instance(id: int):
    return MountPoint(**return_fake_mount_point_json(id), _station=None)

def return_fake_playlist_json(id: int):
    return {
        "name": "Haha",
        "type": "default",
        "source": "songs",
        "order": "shuffle",
        "remote_url": None,
        "remote_type": "stream",
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
        "played_at": 1707329223,
        "queue_reset_at": 1707327991,
        "schedule_items": [],
        "id": id,
        "short_name": "haha",
        "num_songs": 0,
        "total_length": 0,
        "links": {
            "self": "http://localhost/api/station/1/playlist/5",
            "toggle": "http://localhost/api/station/1/playlist/5/toggle",
            "clone": "http://localhost/api/station/1/playlist/5/clone",
            "queue": "http://localhost/api/station/1/playlist/5/queue",
            "import": "http://localhost/api/station/1/playlist/5/import",
            "reshuffle": "http://localhost/api/station/1/playlist/5/reshuffle",
            "applyto": "http://localhost/api/station/1/playlist/5/apply-to",
            "empty": "http://localhost/api/station/1/playlist/5/empty",
            "export": {
                "pls": "http://localhost/api/station/1/playlist/5/export/pls",
                "m3u": "http://localhost/api/station/1/playlist/5/export/m3u"
            }
        }
    }

def return_fake_playlist_instance(id: int):
    return Playlist(**return_fake_playlist_json(id), _station=None)

def return_fake_requestable_song_json():
    return {
        "request_id": "36c1d6cda4e7d71b97b237bb",
        "request_url": "/api/station/1/request/36c1d6cda4e7d71b97b237bb",
        "song": {
            "id": "773d3766a9cacf261e6c8b9c542b36f9",
            "text": "Cochise - GRIND",
            "artist": "Cochise",
            "title": "GRIND",
            "album": "THE INSPECTION",
            "genre": "",
            "isrc": "",
            "lyrics": "",
            "art": "http://localhost/api/station/yet_another_radio/art/36c1d6cda4e7d71b97b237bb-1705365756.jpg",
            "custom_fields": {
                "bro_thinks_hes_funny": None,
                "i thought this wouldn't work     sff s ';-;": None,
                "lol_if_i_dont_wanna_8_lel": None,
                "lolpleasework": None,
                "new_name_who_dis": None,
                "whats_up": None
            }
        }
    }

def return_fake_requestable_song_instance():
    return RequestableSong(**return_fake_playlist_json())

def return_fake_song_history_json():
    return {
        "sh_id": 1347,
        "played_at": 1707520094,
        "duration": 175,
        "playlist": "IM HERE",
        "streamer": "",
        "is_request": False,
        "song": {
            "id": "773d3766a9cacf261e6c8b9c542b36f9",
            "text": "Cochise - GRIND",
            "artist": "Cochise",
            "title": "GRIND",
            "album": "THE INSPECTION",
            "genre": "",
            "isrc": "",
            "lyrics": "",
            "art": "http://localhost/api/station/yet_another_radio/art/36c1d6cda4e7d71b97b237bb-1705365756.jpg",
            "custom_fields": {
                "bro_thinks_hes_funny": None,
                "i thought this wouldn't work     sff s ';-;": None,
                "lol_if_i_dont_wanna_8_lel": None,
                "lolpleasework": None,
                "new_name_who_dis": None,
                "whats_up": None
            }
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
        "id": "1eeb3f87-c013-6c90-b123-9ba650b804a0",
        "storage_location_id": 4,
        "title": "Title",
        "link": "Website",
        "description": "Description",
        "language": "en",
        "author": "Author",
        "email": "Email@gmail.com",
        "has_custom_art": False,
        "art": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/art",
        "art_updated_at": 0,
        "categories": [
            "Arts|Performing Arts",
            "Business|Non-Profit",
            "Arts|Fashion & Beauty"
        ],
        "episodes": [
            "1eeb3f88-f3a4-6a22-b189-8d7240fd53e1",
            "1eeb3f97-f14e-6d54-9d30-131fe97e1a45",
            "1eec486c-7007-60aa-a71b-9d325f29a184"
        ],
        "links": {
            "self": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0",
            "episodes": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episodes",
            "public_episodes": "http://localhost/public/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episodes",
            "public_feed": "http://localhost/public/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/feed",
            "art": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/art",
            "episode_new_art": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episodes/art",
            "episode_new_media": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episodes/media"
        }
    }

def return_fake_podcast_instance():
    return Podcast(**return_fake_podcast_json(), _station=None)

def return_fake_podcast_episode_json():
    return {
        "id": "1eec486c-7007-60aa-a71b-9d325f29a184",
        "title": "lol hey",
        "description": "fuck off",
        "explicit": False,
        "publish_at": None,
        "has_media": False,
        "media": {
            "id": None,
            "original_name": None,
            "length": 0,
            "length_text": None,
            "path": None
        },
        "has_custom_art": False,
        "art": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184/art",
        "art_updated_at": 0,
        "links": {
            "self": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184",
            "public": "http://localhost/public/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184",
            "download": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184/download",
            "art": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184/art",
            "media": "http://localhost/api/station/1/podcast/1eeb3f87-c013-6c90-b123-9ba650b804a0/episode/1eec486c-7007-60aa-a71b-9d325f29a184/media"
        }
    }

def return_fake_podcast_episode_instance():
    return PodcastEpisode(**return_fake_podcast_episode_json(), _podcast=None)

def return_fake_queue_item_json():
    return {
        "cued_at": 1707406815,
        "played_at": 1707520368,
        "duration": 127,
        "playlist": "IM HERE",
        "is_request": False,
        "song": {
            "id": "937b60a479ee80c96db217721afca1fb",
            "text": "Cochise - MEGAMAN",
            "artist": "Cochise",
            "title": "MEGAMAN",
            "album": "THE INSPECTION",
            "genre": "",
            "isrc": "",
            "lyrics": "",
            "art": "http://localhost/api/station/yet_another_radio/art/53bff3de9429ad36ad9bd533-1703965646.jpg",
            "custom_fields": {
                "bro_thinks_hes_funny": None,
                "i thought this wouldn't work     sff s ';-;": None,
                "lol_if_i_dont_wanna_8_lel": None,
                "lolpleasework": None,
                "new_name_who_dis": None,
                "whats_up": None
            }
        },
        "sent_to_autodj": True,
        "is_played": False,
        "autodj_custom_uri": None,
        "log": None,
        "links": {
            "self": "http://localhost/api/station/1/queue/1308"
        }
    }

def return_fake_queue_item_instance():
    return QueueItem(**return_fake_queue_item_json(), _station=None)

def return_fake_remote_relay_json(id: int):
    return {
        "id": id,
        "display_name": "another name who dis",
        "is_visible_on_public_pages": True,
        "type": "icecast",
        "is_editable": True,
        "enable_autodj": True,
        "autodj_format": "ogg",
        "autodj_bitrate": 128,
        "custom_listen_url": None,
        "url": "https://yuh",
        "mount": "",
        "admin_password": "",
        "source_port": None,
        "source_mount": "",
        "source_username": "",
        "source_password": "",
        "is_public": False,
        "listeners_unique": 0,
        "listeners_total": 0,
        "links": {
            "self": "http://localhost/api/station/1/remote/8"
        }
    }

def return_fake_remote_relay_instance():
    return RemoteRelay(**return_fake_remote_relay_json(), _station=None)

def return_fake_sftp_user_json(id: int):
    return {
        "username": "lil_tee",
        "password": "",
        "publicKeys": "hi\nho\nhate",
        "id": id,
        "links": {
            "self": "http://localhost/api/station/1/sftp-user/5"
        }
    }

def return_fake_sftp_user_instance():
    return SFTPUser(**return_fake_sftp_user_json(), _station=None)

def return_fake_streamer_json(id: int):
    return {
        "streamer_username": "hi",
        "streamer_password": "",
        "display_name": "ISSBROKIE",
        "comments": "Im so fucking tired someone help me please I feel like I'm drowning-",
        "is_active": True,
        "enforce_schedule": True,
        "reactivate_at": None,
        "art_updated_at": 0,
        "schedule_items": [],
        "id": id,
        "links": {
            "self": "http://localhost/api/station/1/streamer/4",
            "broadcasts": "http://localhost/api/station/1/streamer/4/broadcasts",
            "art": "http://localhost/api/station/1/streamer/4/art"
        },
        "has_custom_art": False,
        "art": "http://localhost/api/station/1/streamer/4/art"
    }

def return_fake_streamer_instance():
    return Streamer(**return_fake_streamer_json(), _station=None)

def return_fake_webhook_json(id: int):
    return {
        "name": "from library",
        "type": "email",
        "is_enabled": True,
        "triggers": [
            "live_connect",
            "song_changed"
        ],
        "config": [
            "gabeyiscool43@gmail.com",
            "BRO",
            "THIS WORKS"
        ],
        "id": id,
        "links": {
            "self": "http://localhost/api/station/1/webhook/18",
            "toggle": "http://localhost/api/station/1/webhook/18/toggle",
            "test": "http://localhost/api/station/1/webhook/18/test"
        }
    }

def return_fake_webhook_instance():
    return Webhook(**return_fake_webhook_json(), _station=None)