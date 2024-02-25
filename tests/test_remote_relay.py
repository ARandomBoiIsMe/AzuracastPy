import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.remote_relay = fake_data_generator.return_fake_remote_relay_instance()
        self.remote_relay._station = mock.MagicMock()
        self.response = Response()

    def test_successful_remote_relay_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.remote_relay._station._request_handler.put.return_value = self.response.json()

        self.remote_relay.edit(
            display_name="New display name",
            enable_autodj=False
        )

        self.assertEqual(self.remote_relay.display_name, "New display name")
        self.assertEqual(self.remote_relay.enable_autodj, False)

    def test_failed_remote_relay_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.remote_relay._station._request_handler.put.return_value = self.response.json()

        self.remote_relay.edit(
            display_name="New display name",
            enable_autodj=False
        )

        self.assertNotEqual(self.remote_relay.display_name, "New display name")
        self.assertNotEqual(self.remote_relay.enable_autodj, False)

    def test_successful_remote_relay_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.remote_relay._station._request_handler.delete.return_value = self.response.json()

        self.remote_relay.delete()

        self.assertIsNone(self.remote_relay.id)
        self.assertIsNone(self.remote_relay.display_name)
        self.assertIsNone(self.remote_relay.is_visible_on_public_pages)
        self.assertIsNone(self.remote_relay.type)
        self.assertIsNone(self.remote_relay.is_editable)
        self.assertIsNone(self.remote_relay.enable_autodj)
        self.assertIsNone(self.remote_relay.autodj_format)
        self.assertIsNone(self.remote_relay.autodj_bitrate)
        self.assertIsNone(self.remote_relay.custom_listen_url)
        self.assertIsNone(self.remote_relay.url)
        self.assertIsNone(self.remote_relay.mount)
        self.assertIsNone(self.remote_relay.admin_password)
        self.assertIsNone(self.remote_relay.source_port)
        self.assertIsNone(self.remote_relay.source_mount)
        self.assertIsNone(self.remote_relay.source_username)
        self.assertIsNone(self.remote_relay.source_password)
        self.assertIsNone(self.remote_relay.is_public)
        self.assertIsNone(self.remote_relay.listeners_unique)
        self.assertIsNone(self.remote_relay.listeners_total)
        self.assertIsNone(self.remote_relay.links)
        self.assertIsNone(self.remote_relay._station)

    def test_failed_remote_relay_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.remote_relay._station._request_handler.delete.return_value = self.response.json()

        self.remote_relay.delete()

        self.assertIsNotNone(self.remote_relay.id)
        self.assertIsNotNone(self.remote_relay.display_name)
        self.assertIsNotNone(self.remote_relay.is_visible_on_public_pages)
        self.assertIsNotNone(self.remote_relay.type)
        self.assertIsNotNone(self.remote_relay.is_editable)
        self.assertIsNotNone(self.remote_relay.enable_autodj)
        self.assertIsNotNone(self.remote_relay.autodj_format)
        self.assertIsNotNone(self.remote_relay.autodj_bitrate)
        self.assertIsNotNone(self.remote_relay.custom_listen_url)
        self.assertIsNotNone(self.remote_relay.url)
        self.assertIsNotNone(self.remote_relay.mount)
        self.assertIsNotNone(self.remote_relay.admin_password)
        self.assertIsNotNone(self.remote_relay.source_port)
        self.assertIsNotNone(self.remote_relay.source_mount)
        self.assertIsNotNone(self.remote_relay.source_username)
        self.assertIsNotNone(self.remote_relay.source_password)
        self.assertIsNotNone(self.remote_relay.is_public)
        self.assertIsNotNone(self.remote_relay.listeners_unique)
        self.assertIsNotNone(self.remote_relay.listeners_total)
        self.assertIsNotNone(self.remote_relay.links)
        self.assertIsNotNone(self.remote_relay._station)

if __name__ == '__main__':
    unittest.main()