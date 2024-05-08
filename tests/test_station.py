from AzuracastPy import models

from AzuracastPy.enums import (
    ServiceActions,
    Formats,
    Bitrates,
    PlaylistTypes,
    Languages,
    PodcastCategories,
    WebhookConfigTypes,
    WebhookTriggers
)

import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.station = fake_data_generator.return_fake_station_instance()
        self.station._request_handler = mock.MagicMock()
        self.response = Response()

    def test_file_returns_file(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_file_json()

        result = self.station.file(id)

        self.assertIsInstance(result, models.StationFile)
        self.assertIsInstance(result.links, models.station_file.Links)
        self.assertIsInstance(result.playlists, list)

        for playlist in result.playlists:
            self.assertIsInstance(playlist, models.station_file.Playlist)

    def test_files_returns_list_of_file(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_file_json(),
            fake_data_generator.return_fake_file_json(),
            fake_data_generator.return_fake_file_json()
        ]

        result = self.station.files()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.StationFile)
            self.assertIsInstance(item.links, models.station_file.Links)
            self.assertIsInstance(item.playlists, list)

            for playlist in item.playlists:
                self.assertIsInstance(playlist, models.station_file.Playlist)

    def test_mount_point_creation(self):
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_mount_point_json()
        self.station._request_handler.post.return_value['name'] = "/autodj.mp3"
        self.station._request_handler.post.return_value['display_name'] = "Hehehehe"
        self.station._request_handler.post.return_value['autodj_format'] = "opus"

        result = self.station.mount_point.create(
            url="/autodj.mp3",
            display_name="Hehehehe",
            autodj_format=Formats.OPUS
        )

        self.assertIsInstance(result, models.MountPoint)
        self.assertIsInstance(result.links, models.mount_point.Links)

        self.assertEqual(result.name, "/autodj.mp3")
        self.assertEqual(result.display_name, "Hehehehe")
        self.assertEqual(result.autodj_format, "opus")
        self.assertEqual(result.autodj_bitrate, 128)
        self.assertEqual(result.fallback_mount, "/error.mp3")

    def test_mount_point_returns_mount_point(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_mount_point_json()

        result = self.station.mount_point(id)

        self.assertIsInstance(result, models.MountPoint)
        self.assertIsInstance(result.links, models.mount_point.Links)

    def test_mount_points_returns_list_of_mount_point(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_mount_point_json(),
            fake_data_generator.return_fake_mount_point_json(),
            fake_data_generator.return_fake_mount_point_json()
        ]

        result = self.station.mount_points()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.MountPoint)
            self.assertIsInstance(item.links, models.mount_point.Links)

    def test_playlist_creation(self):
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_playlist_json()
        self.station._request_handler.post.return_value['name'] = "New playlist"
        self.station._request_handler.post.return_value['type'] = "once_per_x_minutes"
        self.station._request_handler.post.return_value['play_per_minutes'] = 5

        self.station._request_handler.get.return_value = fake_data_generator.return_fake_playlist_json()
        self.station._request_handler.get.return_value['name'] = "New playlist"
        self.station._request_handler.get.return_value['type'] = "once_per_x_minutes"
        self.station._request_handler.get.return_value['play_per_minutes'] = 5

        result = self.station.playlist.create(
            name="New playlist",
            type=PlaylistTypes.ONCE_PER_X_MINUTES,
            play_per_value=5
        )

        self.assertIsInstance(result, models.Playlist)
        self.assertIsInstance(result.links, models.playlist.Links)

        self.assertEqual(result.name, "New playlist")
        self.assertEqual(result.type, "once_per_x_minutes")
        self.assertEqual(result.play_per_minutes, 5)
        self.assertEqual(result.order, "shuffle")
        self.assertEqual(result.weight, 3)

    def test_playlist_returns_playlist(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_playlist_json()

        result = self.station.playlist(id)

        self.assertIsInstance(result, models.Playlist)
        self.assertIsInstance(result.links, models.playlist.Links)
        self.assertIsInstance(result.schedule_items, list)

        for schedule_item in result.schedule_items:
            self.assertIsInstance(schedule_item, models.playlist.ScheduleItem)

    def test_playlists_returns_list_of_playlist(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_playlist_json(),
            fake_data_generator.return_fake_playlist_json(),
            fake_data_generator.return_fake_playlist_json()
        ]

        result = self.station.playlists()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.Playlist)
            self.assertIsInstance(item.links, models.playlist.Links)
            self.assertIsInstance(item.schedule_items, list)

            for schedule_item in item.schedule_items:
                self.assertIsInstance(schedule_item, models.playlist.ScheduleItem)

    def test_requestable_songs_returns_list_of_requestable_song(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_requestable_song_json(),
            fake_data_generator.return_fake_requestable_song_json(),
            fake_data_generator.return_fake_requestable_song_json()
        ]

        result = self.station.requestable_songs()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.RequestableSong)
            self.assertIsInstance(item.song, models.Song)

    def test_history_returns_list_of_song_history(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_song_history_json(),
            fake_data_generator.return_fake_song_history_json(),
            fake_data_generator.return_fake_song_history_json()
        ]

        result = self.station.history()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.SongHistory)
            self.assertIsInstance(item.song, models.Song)

    def test_schedule_returns_list_of_schedule_time(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_schedule_time_json(),
            fake_data_generator.return_fake_schedule_time_json(),
            fake_data_generator.return_fake_schedule_time_json()
        ]

        result = self.station.schedule()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.ScheduleItem)

    def test_listeners_returns_list_of_listener(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_listener_json(),
            fake_data_generator.return_fake_listener_json(),
            fake_data_generator.return_fake_listener_json()
        ]

        result = self.station.listeners()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.Listener)
            self.assertIsInstance(item.device, models.listener.Device)
            self.assertIsInstance(item.location, models.listener.Location)

    def test_station_status_returns_station_status(self):
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_station_status_json()

        result = self.station.status()

        self.assertIsInstance(result, models.StationStatus)

    def test_podcast_invalid_type_raises_type_error(self):
        incorrect_ids = [True, 2.0, 1]

        for id in incorrect_ids:
            with self.assertRaises(ValueError):
                self.station.podcast(id)

    def test_podcast_creation(self):
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_podcast_json()
        self.station._request_handler.post.return_value['title'] = "New podcast"
        self.station._request_handler.post.return_value['description'] = "This is a random description"
        self.station._request_handler.post.return_value['language'] = "ar"
        self.station._request_handler.post.return_value['categories'] = ["Arts|Design", "Comedy|Comedy Interviews"]

        self.station._request_handler.get.return_value = fake_data_generator.return_fake_podcast_json()
        self.station._request_handler.get.return_value['title'] = "New podcast"
        self.station._request_handler.get.return_value['description'] = "This is a random description"
        self.station._request_handler.get.return_value['language'] = "ar"
        self.station._request_handler.get.return_value['categories'] = ["Arts|Design", "Comedy|Comedy Interviews"]

        result = self.station.podcast.create(
            title="New podcast",
            description="This is a random description",
            language=Languages.ARABIC,
            categories=[
                PodcastCategories.Arts.DESIGN,
                PodcastCategories.Comedy.COMEDY_INTERVIEWS
            ]
        )

        self.assertIsInstance(result, models.Podcast)
        self.assertIsInstance(result.links, models.podcast.Links)

        self.assertEqual(result.title, "New podcast")
        self.assertEqual(result.description, "This is a random description")
        self.assertEqual(result.language, "ar")
        self.assertEqual(result.categories, ["Arts|Design", "Comedy|Comedy Interviews"])

    def test_podcast_returns_podcast(self):
        id = "meh"
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_podcast_json()

        result = self.station.podcast(id)

        self.assertIsInstance(result, models.Podcast)
        self.assertIsInstance(result.links, models.podcast.Links)

    def test_podcasts_returns_list_of_podcast(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_podcast_json(),
            fake_data_generator.return_fake_podcast_json(),
            fake_data_generator.return_fake_podcast_json()
        ]

        result = self.station.podcasts()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.Podcast)
            self.assertIsInstance(item.links, models.podcast.Links)

    def test_hls_stream_creation(self):
        id = 1
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_hls_stream_json()
        self.station._request_handler.post.return_value['name'] = "New HLS Stream"
        self.station._request_handler.post.return_value['format'] = "mp3"
        self.station._request_handler.post.return_value['bitrate'] = 32

        result = self.station.hls_stream.create(
            name="New HLS Stream",
            format=Formats.MP3,
            bitrate=Bitrates.BITRATE_32
        )

        self.assertIsInstance(result, models.HLSStream)
        self.assertIsInstance(result.links, models.hls_stream.Links)

        self.assertEqual(result.name, "New HLS Stream")
        self.assertEqual(result.format, "mp3")
        self.assertEqual(result.bitrate, 32)

    def test_hls_stream_returns_hls_stream(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_hls_stream_json()

        result = self.station.hls_stream(id)

        self.assertIsInstance(result, models.HLSStream)
        self.assertIsInstance(result.links, models.hls_stream.Links)

    def test_hls_streams_returns_list_of_hls_stream(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_hls_stream_json(),
            fake_data_generator.return_fake_hls_stream_json(),
            fake_data_generator.return_fake_hls_stream_json()
        ]

        result = self.station.hls_streams()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.HLSStream)
            self.assertIsInstance(item.links, models.hls_stream.Links)

    def test_remote_relay_creation(self):
        id = 1
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_remote_relay_json()
        self.station._request_handler.post.return_value['url'] = "http://station.example.com:8000"
        self.station._request_handler.post.return_value['display_name'] = "Display name"
        self.station._request_handler.post.return_value['autodj_format'] = "mp3"

        result = self.station.remote_relay.create(
            station_listening_url="http://station.example.com:8000",
            display_name="Display name",
            autodj_format=Formats.MP3
        )

        self.assertIsInstance(result, models.RemoteRelay)
        self.assertIsInstance(result.links, models.remote_relay.Links)

        self.assertEqual(result.url, "http://station.example.com:8000")
        self.assertEqual(result.display_name, "Display name")
        self.assertEqual(result.autodj_format, "mp3")
        self.assertEqual(result.autodj_bitrate, 128)

    def test_remote_relay_returns_remote_relay(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_remote_relay_json()

        result = self.station.remote_relay(id)

        self.assertIsInstance(result, models.RemoteRelay)
        self.assertIsInstance(result.links, models.remote_relay.Links)

    def test_remote_relays_returns_list_of_remote_relay(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_remote_relay_json(),
            fake_data_generator.return_fake_remote_relay_json(),
            fake_data_generator.return_fake_remote_relay_json()
        ]

        result = self.station.remote_relays()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.RemoteRelay)
            self.assertIsInstance(item.links, models.remote_relay.Links)

    def test_sftp_user_creation(self):
        id = 1
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_sftp_user_json()
        self.station._request_handler.post.return_value['username'] = "Username"
        self.station._request_handler.post.return_value['password'] = "Password"
        self.station._request_handler.post.return_value['publicKeys'] = "key1\nkey2"

        result = self.station.sftp_user.create(
            username="Username",
            password="Password",
            public_keys=['key1', 'key2']
        )

        self.assertIsInstance(result, models.SFTPUser)
        self.assertIsInstance(result.links, models.sftp_user.Links)

        self.assertEqual(result.username, "Username")
        self.assertEqual(result.password, "Password")
        self.assertEqual(result.public_keys, ["key1", "key2"])

    def test_sftp_user_returns_sftp_user(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_sftp_user_json()

        result = self.station.sftp_user(id)

        self.assertIsInstance(result, models.SFTPUser)
        self.assertIsInstance(result.links, models.sftp_user.Links)

    def test_sftp_users_returns_list_of_sftp_user(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_sftp_user_json(),
            fake_data_generator.return_fake_sftp_user_json(),
            fake_data_generator.return_fake_sftp_user_json()
        ]

        result = self.station.sftp_users()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.SFTPUser)
            self.assertIsInstance(item.links, models.sftp_user.Links)

    def test_streamer_creation(self):
        id = 1
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_streamer_json()
        self.station._request_handler.post.return_value['username'] = "Username"
        self.station._request_handler.post.return_value['password'] = "Password"
        self.station._request_handler.post.return_value['comments'] = "Never gonna give you up."

        self.station._request_handler.get.return_value = fake_data_generator.return_fake_streamer_json()
        self.station._request_handler.get.return_value['streamer_username'] = "Username"
        self.station._request_handler.get.return_value['streamer_password'] = "Password"
        self.station._request_handler.get.return_value['comments'] = "Never gonna give you up."

        result = self.station.streamer.create(
            username="Username",
            password="Password",
            comments="Never gonna give you up."
        )

        self.assertIsInstance(result, models.Streamer)
        self.assertIsInstance(result.links, models.streamer.Links)

        self.assertEqual(result.streamer_username, "Username")
        self.assertEqual(result.streamer_password, "Password")
        self.assertEqual(result.comments, "Never gonna give you up.")

    def test_streamer_returns_streamer(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_streamer_json()

        result = self.station.streamer(id)

        self.assertIsInstance(result, models.Streamer)
        self.assertIsInstance(result.links, models.streamer.Links)
        self.assertIsInstance(result.schedule_items, list)

        for schedule_item in result.schedule_items:
            self.assertIsInstance(schedule_item, models.streamer.ScheduleItem)

    def test_streamers_returns_list_of_streamer(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_streamer_json(),
            fake_data_generator.return_fake_streamer_json(),
            fake_data_generator.return_fake_streamer_json()
        ]

        result = self.station.streamers()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.Streamer)
            self.assertIsInstance(item.links, models.streamer.Links)
            self.assertIsInstance(item.schedule_items, list)

            for schedule_item in item.schedule_items:
                self.assertIsInstance(schedule_item, models.streamer.ScheduleItem)

    def test_webhook_creation(self):
        id = 1
        self.station._request_handler.post.return_value = fake_data_generator.return_fake_webhook_json()
        self.station._request_handler.post.return_value['name'] = "New email webhook"
        self.station._request_handler.post.return_value['type'] = "email"
        self.station._request_handler.post.return_value['config'] = [
            "gabeyiscool43@gmail.com",
            "BRO",
            "THIS WORKS"
        ]
        self.station._request_handler.post.return_value['triggers'] = [
            "live_connect",
            "station_online"
        ]

        self.station._request_handler.get.return_value = fake_data_generator.return_fake_webhook_json()
        self.station._request_handler.get.return_value['name'] = "New email webhook"
        self.station._request_handler.get.return_value['type'] = "email"
        self.station._request_handler.get.return_value['config'] = [
            "gabeyiscool43@gmail.com",
            "BRO",
            "THIS WORKS"
        ]
        self.station._request_handler.get.return_value['triggers'] = [
            "live_connect",
            "station_online"
        ]

        config = self.station.webhook.generate_webhook_config(
            subject="subject",
            message="message",
            to="to"
        )

        result = self.station.webhook.create(
            name="New email webhook",
            type=WebhookConfigTypes.EMAIL,
            webhook_config=config,
            triggers=[WebhookTriggers.STATION_ONLINE, WebhookTriggers.LIVE_CONNECT]
        )

        self.assertIsInstance(result, models.Webhook)
        self.assertIsInstance(result.links, models.webhook.Links)

        self.assertEqual(result.name, "New email webhook")
        self.assertEqual(result.type, "email")
        self.assertEqual(result.config, [
            "gabeyiscool43@gmail.com",
            "BRO",
            "THIS WORKS"
        ])
        self.assertEqual(result.triggers, [
            "live_connect",
            "station_online"
        ])

    def test_webhook_returns_webhook(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_webhook_json()

        result = self.station.webhook(id)

        self.assertIsInstance(result, models.Webhook)
        self.assertIsInstance(result.links, models.webhook.Links)

    def test_webhooks_returns_list_of_webhook(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_webhook_json(),
            fake_data_generator.return_fake_webhook_json(),
            fake_data_generator.return_fake_webhook_json()
        ]

        result = self.station.webhooks()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.Webhook)
            self.assertIsInstance(item.links, models.webhook.Links)

    def test_perform_frontend_action_restart(self):
        self.response._content = '{"message": "Service restarted"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_frontend_action()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service restarted")

    def test_perform_frontend_action_start(self):
        self.response._content = '{"message": "Service started"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_frontend_action(ServiceActions.START)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service started")

    def test_perform_frontend_action_stop(self):
        self.response._content = '{"message": "Service stopped"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_frontend_action(ServiceActions.STOP)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service stopped")

    def test_perform_backend_action_restart(self):
        self.response._content = '{"message": "Service restarted"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_backend_action()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service restarted")

    def test_perform_backend_action_start(self):
        self.response._content = '{"message": "Service started"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_backend_action(ServiceActions.START)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service started")

    def test_perform_frontend_action_stop(self):
        self.response._content = '{"message": "Service stopped"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.perform_backend_action(ServiceActions.STOP)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Service stopped")

    def test_station_restart(self):
        self.response._content = '{"message": "Station restarted"}'.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.restart()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Station restarted")

    def test_successful_song_request(self):
        self.response._content = """
        {
            "success": true,
            "message": "Your request has been submitted and will be played soon.",
            "formatted_message": "Your request has been submitted and will be played soon."
        }
        """.encode()

        self.station._request_handler.post.return_value = self.response.json()

        result = self.station.request_song("bleh")

        self.assertIsInstance(result, dict)
        self.assertEqual(result['message'], "Your request has been submitted and will be played soon.")

if __name__ == '__main__':
    unittest.main()