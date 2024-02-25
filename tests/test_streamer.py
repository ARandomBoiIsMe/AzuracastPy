import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.streamer = fake_data_generator.return_fake_streamer_instance()
        self.streamer._station = mock.MagicMock()
        self.response = Response()

    def test_successful_streamer_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.streamer._station._request_handler.put.return_value = self.response.json()

        self.streamer.edit(
            username="New username",
            display_name="The name which is displayed",
            comments="Lol hi hi hi",
            enforce_schedule=False
        )

        self.assertEqual(self.streamer.streamer_username, "New username")
        self.assertEqual(self.streamer.display_name, "The name which is displayed")
        self.assertEqual(self.streamer.comments, "Lol hi hi hi")
        self.assertEqual(self.streamer.enforce_schedule, False)


    def test_failed_streamer_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.streamer._station._request_handler.put.return_value = self.response.json()

        self.streamer.edit(
            username="New username",
            display_name="The name which is displayed",
            comments="Lol hi hi hi",
            enforce_schedule=False
        )

        self.assertNotEqual(self.streamer.streamer_username, "New username")
        self.assertNotEqual(self.streamer.display_name, "The name which is displayed")
        self.assertNotEqual(self.streamer.comments, "Lol hi hi hi")
        self.assertNotEqual(self.streamer.enforce_schedule, False)

    def test_successful_streamer_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.streamer._station._request_handler.delete.return_value = self.response.json()

        self.streamer.delete()

        self.assertIsNone(self.streamer.streamer_username)
        self.assertIsNone(self.streamer.streamer_password)
        self.assertIsNone(self.streamer.display_name)
        self.assertIsNone(self.streamer.comments)
        self.assertIsNone(self.streamer.is_active)
        self.assertIsNone(self.streamer.enforce_schedule)
        self.assertIsNone(self.streamer.reactivate_at)
        self.assertIsNone(self.streamer.art_updated_at)
        self.assertIsNone(self.streamer.schedule_items)
        self.assertIsNone(self.streamer.id)
        self.assertIsNone(self.streamer.links)
        self.assertIsNone(self.streamer.has_custom_art)
        self.assertIsNone(self.streamer.art)
        self.assertIsNone(self.streamer._station)

    def test_failed_streamer_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.streamer._station._request_handler.delete.return_value = self.response.json()

        self.streamer.delete()

        self.assertIsNotNone(self.streamer.streamer_username)
        self.assertIsNotNone(self.streamer.streamer_password)
        self.assertIsNotNone(self.streamer.display_name)
        self.assertIsNotNone(self.streamer.comments)
        self.assertIsNotNone(self.streamer.is_active)
        self.assertIsNotNone(self.streamer.enforce_schedule)
        self.assertIsNotNone(self.streamer.reactivate_at)
        self.assertIsNotNone(self.streamer.art_updated_at)
        self.assertIsNotNone(self.streamer.schedule_items)
        self.assertIsNotNone(self.streamer.id)
        self.assertIsNotNone(self.streamer.links)
        self.assertIsNotNone(self.streamer.has_custom_art)
        self.assertIsNotNone(self.streamer.art)
        self.assertIsNotNone(self.streamer._station)

if __name__ == '__main__':
    unittest.main()