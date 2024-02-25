import unittest
from unittest import TestCase, mock
from requests import Response

from AzuracastPy.enums import (
    Formats,
    Bitrates
)

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.mount_point = fake_data_generator.return_fake_mount_point_instance(1)
        self.mount_point._station = mock.MagicMock()
        self.response = Response()

    def test_successful_mount_point_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.mount_point._station._request_handler.put.return_value = self.response.json()

        self.mount_point.edit(
            display_name="New display name",
            enable_autodj=False,
            autodj_format=Formats.OPUS,
            autodj_bitrate=Bitrates.BITRATE_32
        )

        self.assertEqual(self.mount_point.display_name, "New display name")
        self.assertEqual(self.mount_point.enable_autodj, False)
        self.assertEqual(self.mount_point.autodj_format, "opus")
        self.assertEqual(self.mount_point.autodj_bitrate, 32)

    def test_failed_mount_point_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.mount_point._station._request_handler.put.return_value = self.response.json()

        self.mount_point.edit(
            display_name="New display name",
            enable_autodj=False,
            autodj_format=Formats.OPUS,
            autodj_bitrate=Bitrates.BITRATE_32
        )

        self.assertNotEqual(self.mount_point.display_name, "New display name")
        self.assertNotEqual(self.mount_point.enable_autodj, False)
        self.assertNotEqual(self.mount_point.autodj_format, "opus")
        self.assertNotEqual(self.mount_point.autodj_bitrate, 32)

    def test_successful_mount_point_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.mount_point._station._request_handler.delete.return_value = self.response.json()

        self.mount_point.delete()

        self.assertIsNone(self.mount_point.name)
        self.assertIsNone(self.mount_point.display_name)
        self.assertIsNone(self.mount_point.is_visible_on_public_pages)
        self.assertIsNone(self.mount_point.is_default)
        self.assertIsNone(self.mount_point.is_public)
        self.assertIsNone(self.mount_point.fallback_mount)
        self.assertIsNone(self.mount_point.relay_url)
        self.assertIsNone(self.mount_point.authhash)
        self.assertIsNone(self.mount_point.max_listener_duration)
        self.assertIsNone(self.mount_point.enable_autodj)
        self.assertIsNone(self.mount_point.autodj_format)
        self.assertIsNone(self.mount_point.autodj_bitrate)
        self.assertIsNone(self.mount_point.custom_listen_url)
        self.assertIsNone(self.mount_point.intro_path)
        self.assertIsNone(self.mount_point.frontend_config)
        self.assertIsNone(self.mount_point.listeners_unique)
        self.assertIsNone(self.mount_point.listeners_total)
        self.assertIsNone(self.mount_point.id)
        self.assertIsNone(self.mount_point.links)
        self.assertIsNone(self.mount_point._station)

    def test_failed_mount_point_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.mount_point._station._request_handler.delete.return_value = self.response.json()

        self.mount_point.delete()

        self.assertIsNotNone(self.mount_point.name)
        self.assertIsNotNone(self.mount_point.display_name)
        self.assertIsNotNone(self.mount_point.is_visible_on_public_pages)
        self.assertIsNotNone(self.mount_point.is_default)
        self.assertIsNotNone(self.mount_point.is_public)
        self.assertIsNotNone(self.mount_point.fallback_mount)
        self.assertIsNotNone(self.mount_point.relay_url)
        self.assertIsNotNone(self.mount_point.authhash)
        self.assertIsNotNone(self.mount_point.max_listener_duration)
        self.assertIsNotNone(self.mount_point.enable_autodj)
        self.assertIsNotNone(self.mount_point.autodj_format)
        self.assertIsNotNone(self.mount_point.autodj_bitrate)
        self.assertIsNotNone(self.mount_point.custom_listen_url)
        self.assertIsNotNone(self.mount_point.intro_path)
        self.assertIsNotNone(self.mount_point.frontend_config)
        self.assertIsNotNone(self.mount_point.listeners_unique)
        self.assertIsNotNone(self.mount_point.listeners_total)
        self.assertIsNotNone(self.mount_point.id)
        self.assertIsNotNone(self.mount_point.links)
        self.assertIsNotNone(self.mount_point._station)

if __name__ == '__main__':
    unittest.main()