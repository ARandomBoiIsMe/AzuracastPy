import unittest
from unittest import TestCase, mock
from requests import Response

from AzuracastPy.enums import (
    PlaylistSources
)

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.playlist = fake_data_generator.return_fake_playlist_instance()
        self.playlist._station = mock.MagicMock()
        self.response = Response()

    def test_successful_playlist_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.playlist._station._request_handler.put.return_value = self.response.json()

        self.playlist.edit(
            name="New name lol",
            allow_requests=False,
            avoid_duplicates=False,
            source=PlaylistSources.REMOTE_URL
        )

        self.assertEqual(self.playlist.name, "New name lol")
        self.assertEqual(self.playlist.include_in_requests, False)
        self.assertEqual(self.playlist.avoid_duplicates, False)
        self.assertEqual(self.playlist.source, "remote_url")

    def test_failed_playlist_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.playlist._station._request_handler.put.return_value = self.response.json()

        self.playlist.edit(
            name="New name lol",
            allow_requests=False,
            avoid_duplicates=False,
            source=PlaylistSources.REMOTE_URL
        )

        self.assertNotEqual(self.playlist.name, "New name lol")
        self.assertNotEqual(self.playlist.include_in_requests, False)
        self.assertNotEqual(self.playlist.avoid_duplicates, False)
        self.assertNotEqual(self.playlist.source, "remote_url")

    def test_successful_playlist_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.playlist._station._request_handler.delete.return_value = self.response.json()

        self.playlist.delete()

        self.assertIsNone(self.playlist.name)
        self.assertIsNone(self.playlist.type)
        self.assertIsNone(self.playlist.source)
        self.assertIsNone(self.playlist.order)
        self.assertIsNone(self.playlist.remote_url)
        self.assertIsNone(self.playlist.remote_type)
        self.assertIsNone(self.playlist.remote_buffer)
        self.assertIsNone(self.playlist.is_enabled)
        self.assertIsNone(self.playlist.is_jingle)
        self.assertIsNone(self.playlist.play_per_songs)
        self.assertIsNone(self.playlist.play_per_minutes)
        self.assertIsNone(self.playlist.play_per_hour_minute)
        self.assertIsNone(self.playlist.weight)
        self.assertIsNone(self.playlist.include_in_requests)
        self.assertIsNone(self.playlist.include_in_on_demand)
        self.assertIsNone(self.playlist.backend_options)
        self.assertIsNone(self.playlist.avoid_duplicates)
        self.assertIsNone(self.playlist.played_at)
        self.assertIsNone(self.playlist.queue_reset_at)
        self.assertIsNone(self.playlist.schedule_items)
        self.assertIsNone(self.playlist.id)
        self.assertIsNone(self.playlist.short_name)
        self.assertIsNone(self.playlist.num_songs)
        self.assertIsNone(self.playlist.total_length)
        self.assertIsNone(self.playlist.links)
        self.assertIsNone(self.playlist._station)

    def test_failed_playlist_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.playlist._station._request_handler.delete.return_value = self.response.json()

        self.playlist.delete()

        self.assertIsNotNone(self.playlist.name)
        self.assertIsNotNone(self.playlist.type)
        self.assertIsNotNone(self.playlist.source)
        self.assertIsNotNone(self.playlist.order)
        self.assertIsNotNone(self.playlist.remote_url)
        self.assertIsNotNone(self.playlist.remote_type)
        self.assertIsNotNone(self.playlist.remote_buffer)
        self.assertIsNotNone(self.playlist.is_enabled)
        self.assertIsNotNone(self.playlist.is_jingle)
        self.assertIsNotNone(self.playlist.play_per_songs)
        self.assertIsNotNone(self.playlist.play_per_minutes)
        self.assertIsNotNone(self.playlist.play_per_hour_minute)
        self.assertIsNotNone(self.playlist.weight)
        self.assertIsNotNone(self.playlist.include_in_requests)
        self.assertIsNotNone(self.playlist.include_in_on_demand)
        self.assertIsNotNone(self.playlist.backend_options)
        self.assertIsNotNone(self.playlist.avoid_duplicates)
        self.assertIsNotNone(self.playlist.played_at)
        self.assertIsNotNone(self.playlist.queue_reset_at)
        self.assertIsNotNone(self.playlist.schedule_items)
        self.assertIsNotNone(self.playlist.id)
        self.assertIsNotNone(self.playlist.short_name)
        self.assertIsNotNone(self.playlist.num_songs)
        self.assertIsNotNone(self.playlist.total_length)
        self.assertIsNotNone(self.playlist.links)
        self.assertIsNotNone(self.playlist._station)

if __name__ == '__main__':
    unittest.main()