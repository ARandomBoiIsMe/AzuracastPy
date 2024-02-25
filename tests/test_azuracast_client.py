import unittest
from unittest.mock import MagicMock

from AzuracastPy import AzuracastClient, models

from .util import fake_data_generator

class TestAzuracastClient(unittest.TestCase):

    def setUp(self):
        radio_url = "http://example.com"
        x_api_key = "your_api_key"

        self.client = AzuracastClient(
            radio_url=radio_url,
            x_api_key=x_api_key
        )

        self.client._request_handler = MagicMock()
        self.client._request_handler.radio_url = radio_url
        self.client._request_handler._x_api_key = x_api_key

    def test_client_initialization(self):
        self.assertEqual(self.client._request_handler.radio_url, "http://example.com")
        self.assertEqual(self.client._request_handler._x_api_key, "your_api_key")

    def test_build_now_playing_url(self):
        url_all_now_playing = self.client._build_now_playing_url()
        url_station_now_playing = self.client._build_now_playing_url(station_id=1)

        self.assertEqual(url_all_now_playing, "http://example.com/api/nowplaying")
        self.assertEqual(url_station_now_playing, "http://example.com/api/nowplaying/1")

    def test_admin_method(self):
        admin_instance = self.client.admin()
        self.assertIsInstance(admin_instance, models.administration.Admin)

    def test_now_playing_method_all_stations(self):
        response_data = [
            fake_data_generator.return_fake_now_playing_json(1),
            fake_data_generator.return_fake_now_playing_json(2)
        ]
        self.client._request_handler.get.return_value = response_data

        all_now_playing = self.client.now_playing()

        self.assertEqual(len(all_now_playing), 2)
        for station_now_playing in all_now_playing:
            self.assertIsInstance(station_now_playing, models.NowPlaying)
            self.assertIsInstance(station_now_playing.station, models.Station)
            self.assertIsInstance(station_now_playing.live, models.now_playing.Live)
            self.assertIsInstance(station_now_playing.playing_next, models.now_playing.PlayingNext)
            self.assertIsInstance(station_now_playing.now_playing, models.now_playing.CurrentSong)
            self.assertIsInstance(station_now_playing.listeners, models.Listeners)
            self.assertIsInstance(station_now_playing.song_history, list)
            for history in station_now_playing.song_history:
                self.assertIsInstance(history, models.now_playing.SongHistory)

    def test_now_playing_method_single_station(self):
        response_data = fake_data_generator.return_fake_now_playing_json(1)
        self.client._request_handler.get.return_value = response_data

        station_now_playing = self.client.now_playing(station_id=1)

        self.assertIsInstance(station_now_playing, models.NowPlaying)
        self.assertIsInstance(station_now_playing.station, models.Station)
        self.assertIsInstance(station_now_playing.live, models.now_playing.Live)
        self.assertIsInstance(station_now_playing.playing_next, models.now_playing.PlayingNext)
        self.assertIsInstance(station_now_playing.now_playing, models.now_playing.CurrentSong)
        self.assertIsInstance(station_now_playing.listeners, models.Listeners)
        self.assertIsInstance(station_now_playing.song_history, list)
        for history in station_now_playing.song_history:
            self.assertIsInstance(history, models.now_playing.SongHistory)

    def test_stations_method(self):
        response_data = [
            fake_data_generator.return_fake_station_json(1),
            fake_data_generator.return_fake_station_json(2)
        ]
        self.client._request_handler.get.return_value = response_data

        stations = self.client.stations()

        self.assertEqual(len(stations), 2)
        for station in stations:
            self.assertIsInstance(station, models.Station)
            self.assertIsInstance(station.mounts, list)
            for mount in station.mounts:
                self.assertIsInstance(mount, models.Mount)

            self.assertIsInstance(station.remotes, list)
            for remote in station.remotes:
                self.assertIsInstance(remote, models.Remote)

    def test_station_method(self):
        response_data = fake_data_generator.return_fake_station_json(1)
        self.client._request_handler.get.return_value = response_data

        station = self.client.station(1)

        self.assertIsInstance(station, models.Station)
        self.assertIsInstance(station.mounts, list)
        for mount in station.mounts:
            self.assertIsInstance(mount, models.Mount)

        self.assertIsInstance(station.remotes, list)
        for remote in station.remotes:
            self.assertIsInstance(remote, models.Remote)

if __name__ == "__main__":
    unittest.main()
