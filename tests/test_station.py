from AzuracastPy.models.station_file import StationFile
from AzuracastPy.models.mount_point import MountPoint
from AzuracastPy.models.playlist import Playlist
from AzuracastPy.models.requestable_song import RequestableSong
from AzuracastPy.models.song_history import SongHistory
from AzuracastPy.models.schedule_time import ScheduleTime
from AzuracastPy.models.listener import Listener
from AzuracastPy.models.station_status import StationStatus

import unittest
from unittest import TestCase, mock

from .util import fake_data_generator

from requests import Response

class TestStation(TestCase):
    def setUp(self) -> None:
        self.station = fake_data_generator.return_fake_station_instance(1)
        self.station._request_handler = mock.MagicMock()

    # This indirectly tests all functions that return a single instance of whatever resource,
    # because they all use this function
    # ---------------------------
    def test__request_single_instance_of_incorrect_id_data_type_raises_type_error(self):
        incorrect_ids = ['', True, 2.0]

        for id in incorrect_ids:
            with self.assertRaises(TypeError):
                self.station._request_single_instance_of('', id)

    def test__request_single_instance_of_negative_id_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.station._request_single_instance_of('', -2)
    # ---------------------------
            
    def test_file_returns_file(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_file_json(id)
        
        result = self.station.file(id)

        self.assertIsInstance(result, StationFile)

    def test_files_returns_list_of_file(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_file_json(1),
            fake_data_generator.return_fake_file_json(2),
            fake_data_generator.return_fake_file_json(19)
        ]
        
        result = self.station.files()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, StationFile)

    def test_mount_point_returns_mount_point(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_mount_point_json(id)
        
        result = self.station.mount_point(id)

        self.assertIsInstance(result, MountPoint)

    def test_mount_points_returns_list_of_mount_point(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_mount_point_json(1),
            fake_data_generator.return_fake_mount_point_json(2),
            fake_data_generator.return_fake_mount_point_json(19)
        ]
        
        result = self.station.mount_points()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, MountPoint)

    def test_playlist_returns_playlist(self):
        id = 1
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_playlist_json(id)

        result = self.station.playlist(id)

        self.assertIsInstance(result, Playlist)

    def test_playlists_returns_list_of_playlist(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_playlist_json(1),
            fake_data_generator.return_fake_playlist_json(2),
            fake_data_generator.return_fake_playlist_json(19)
        ]

        result = self.station.playlists()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Playlist)

    def test_requestable_songs_returns_list_of_requestable_song(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_requestable_song_json(),
            fake_data_generator.return_fake_requestable_song_json(),
            fake_data_generator.return_fake_requestable_song_json()
        ]

        result = self.station.requestable_songs()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, RequestableSong)

    def test_history_returns_list_of_song_history(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_song_history_json(),
            fake_data_generator.return_fake_song_history_json(),
            fake_data_generator.return_fake_song_history_json()
        ]

        result = self.station.history()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, SongHistory)

    def test_schedule_returns_list_of_schedule_time(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_schedule_time_json(),
            fake_data_generator.return_fake_schedule_time_json(),
            fake_data_generator.return_fake_schedule_time_json()
        ]

        result = self.station.schedule()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, ScheduleTime)

    def test_listeners_returns_list_of_listener(self):
        self.station._request_handler.get.return_value = [
            fake_data_generator.return_fake_listener_json(),
            fake_data_generator.return_fake_listener_json(),
            fake_data_generator.return_fake_listener_json()
        ]

        result = self.station.listeners()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Listener)

    def test_station_status_returns_station_status(self):
        self.station._request_handler.get.return_value = fake_data_generator.return_fake_station_status_json()

        result = self.station.status()

        self.assertIsInstance(result, StationStatus)

    def test__perform_service_action_invalid_action_raises_value_error_exception(self):
        invalid_actions = ['RESTART', 'StOp', 'stArt']

        for action in invalid_actions:
            with self.assertRaises(ValueError):
                self.station._perform_service_action(action=action, service_type='')

    def test_perform_frontend_action_restart(self):
        response = Response()
        response._content = '{"message": "Service restarted"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_frontend_action()

        self.assertEqual(result, "Service restarted")

    def test_perform_frontend_action_start(self):
        response = Response()
        response._content = '{"message": "Service started"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_frontend_action('start')

        self.assertEqual(result, "Service started")

    def test_perform_frontend_action_stop(self):
        response = Response()
        response._content = '{"message": "Service stopped"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_frontend_action('stop')

        self.assertEqual(result, "Service stopped")

    def test_perform_backend_action_restart(self):
        response = Response()
        response._content = '{"message": "Service restarted"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_backend_action()

        self.assertEqual(result, "Service restarted")

    def test_perform_backend_action_start(self):
        response = Response()
        response._content = '{"message": "Service started"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_backend_action('start')

        self.assertEqual(result, "Service started")

    def test_perform_frontend_action_stop(self):
        response = Response()
        response._content = '{"message": "Service stopped"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.perform_backend_action('stop')

        self.assertEqual(result, "Service stopped")

    def test_station_restart(self):
        response = Response()
        response._content = '{"message": "Station restarted"}'.encode()

        self.station._request_handler.post.return_value = response.json()

        result = self.station.restart()

        self.assertEqual(result, "Station restarted")

if __name__ == '__main__':
    unittest.main()