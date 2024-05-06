import json

from AzuracastPy import models

FAKE_JSON_DIR = 'tests/util/json'

def return_fake_station_json():
    with open(f'{FAKE_JSON_DIR}/station.json', 'r') as file:
        return json.loads(file.read())

def return_fake_station_instance():
    return models.Station(**return_fake_station_json(), _request_handler=None)

def return_fake_file_json():
    with open(f'{FAKE_JSON_DIR}/file.json', 'r') as file:
        return json.loads(file.read())

def return_fake_mount_point_json():
    with open(f'{FAKE_JSON_DIR}/mount_point.json', 'r') as file:
        return json.loads(file.read())

def return_fake_mount_point_instance():
    return models.MountPoint(**return_fake_mount_point_json(), _station=None)

def return_fake_now_playing_json():
    with open(f'{FAKE_JSON_DIR}/now_playing.json', 'r') as file:
        return json.loads(file.read())

def return_fake_playlist_json():
    with open(f'{FAKE_JSON_DIR}/playlist.json', 'r') as file:
        return json.loads(file.read())

def return_fake_playlist_instance():
    return models.Playlist(**return_fake_playlist_json(), _station=None)

def return_fake_requestable_song_json():
    with open(f'{FAKE_JSON_DIR}/requestable_song.json', 'r') as file:
        return json.loads(file.read())

def return_fake_song_history_json():
    with open(f'{FAKE_JSON_DIR}/song_history.json', 'r') as file:
        return json.loads(file.read())

def return_fake_schedule_time_json():
    with open(f'{FAKE_JSON_DIR}/schedule_time.json', 'r') as file:
        return json.loads(file.read())

def return_fake_listener_json():
    with open(f'{FAKE_JSON_DIR}/listener.json', 'r') as file:
        return json.loads(file.read())

def return_fake_station_status_json():
    with open(f'{FAKE_JSON_DIR}/station_status.json', 'r') as file:
        return json.loads(file.read())

def return_fake_podcast_json():
    with open(f'{FAKE_JSON_DIR}/podcast.json', 'r') as file:
        return json.loads(file.read())

def return_fake_podcast_instance():
    return models.Podcast(**return_fake_podcast_json(), _station=None)

def return_fake_podcast_episode_json():
    with open(f'{FAKE_JSON_DIR}/podcast_episode.json', 'r') as file:
        return json.loads(file.read())

def return_fake_podcast_episode_instance():
    return models.PodcastEpisode(**return_fake_podcast_episode_json(), _podcast=None)

def return_fake_queue_item_json():
    with open(f'{FAKE_JSON_DIR}/queue_item.json', 'r') as file:
        return json.loads(file.read())

def return_fake_hls_stream_json():
    with open(f'{FAKE_JSON_DIR}/hls_stream.json', 'r') as file:
        return json.loads(file.read())

def return_fake_hls_stream_instance():
    return models.HLSStream(**return_fake_hls_stream_json(), _station=None)

def return_fake_remote_relay_json():
    with open(f'{FAKE_JSON_DIR}/remote_relay.json', 'r') as file:
        return json.loads(file.read())

def return_fake_remote_relay_instance():
    return models.RemoteRelay(**return_fake_remote_relay_json(), _station=None)

def return_fake_sftp_user_json():
    with open(f'{FAKE_JSON_DIR}/sftp_user.json', 'r') as file:
        return json.loads(file.read())

def return_fake_sftp_user_instance():
    return models.SFTPUser(**return_fake_sftp_user_json(), _station=None)

def return_fake_streamer_json():
    with open(f'{FAKE_JSON_DIR}/streamer.json', 'r') as file:
        return json.loads(file.read())

def return_fake_streamer_instance():
    return models.Streamer(**return_fake_streamer_json(), _station=None)

def return_fake_webhook_json():
    with open(f'{FAKE_JSON_DIR}/webhook.json', 'r') as file:
        return json.loads(file.read())

def return_fake_webhook_instance():
    return models.Webhook(**return_fake_webhook_json(), _station=None)

def return_fake_admin_instance():
    return models.administration.Admin(_request_handler=None)

def return_fake_admin_station_json():
    with open(f'{FAKE_JSON_DIR}/admin_station.json', 'r') as file:
        return json.loads(file.read())

def return_fake_role_json():
    with open(f'{FAKE_JSON_DIR}/role.json', 'r') as file:
        return json.loads(file.read())

def return_fake_custom_field_json():
    with open(f'{FAKE_JSON_DIR}/custom_field.json', 'r') as file:
        return json.loads(file.read())

def return_fake_storage_location_json():
    with open(f'{FAKE_JSON_DIR}/storage_location.json', 'r') as file:
        return json.loads(file.read())

def return_fake_permissions_json():
    with open(f'{FAKE_JSON_DIR}/permissions.json', 'r') as file:
        return json.loads(file.read())

def return_fake_relay_json():
    with open(f'{FAKE_JSON_DIR}/relay.json', 'r') as file:
        return json.loads(file.read())

def return_fake_settings_json():
    with open(f'{FAKE_JSON_DIR}/settings.json', 'r') as file:
        return json.loads(file.read())

def return_fake_cpu_stats_json():
    with open(f'{FAKE_JSON_DIR}/cpu_stats.json', 'r') as file:
        return json.loads(file.read())