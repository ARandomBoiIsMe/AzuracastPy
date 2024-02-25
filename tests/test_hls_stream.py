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
        self.hls_stream = fake_data_generator.return_fake_hls_stream_instance()
        self.hls_stream._station = mock.MagicMock()
        self.response = Response()

    def test_successful_hls_stream_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.hls_stream._station._request_handler.put.return_value = self.response.json()

        self.hls_stream.edit(
            name="New name",
            format=Formats.OPUS,
            bitrate=Bitrates.BITRATE_128
        )

        self.assertEqual(self.hls_stream.name, "New name")
        self.assertEqual(self.hls_stream.format, "opus")
        self.assertEqual(self.hls_stream.bitrate, 128)

    def test_failed_hls_stream_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.hls_stream._station._request_handler.put.return_value = self.response.json()

        self.hls_stream.edit(
            name="New name",
            format=Formats.OPUS,
            bitrate=Bitrates.BITRATE_128
        )

        self.assertNotEqual(self.hls_stream.name, "New name")
        self.assertNotEqual(self.hls_stream.format, "opus")
        self.assertNotEqual(self.hls_stream.bitrate, 128)

    def test_successful_hls_stream_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.hls_stream._station._request_handler.delete.return_value = self.response.json()

        self.hls_stream.delete()

        self.assertIsNone(self.hls_stream.name)
        self.assertIsNone(self.hls_stream.format)
        self.assertIsNone(self.hls_stream.bitrate)
        self.assertIsNone(self.hls_stream.listeners)
        self.assertIsNone(self.hls_stream.id)
        self.assertIsNone(self.hls_stream.links)
        self.assertIsNone(self.hls_stream._station)

    def test_failed_hls_stream_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.hls_stream._station._request_handler.delete.return_value = self.response.json()

        self.hls_stream.delete()

        self.assertIsNotNone(self.hls_stream.name)
        self.assertIsNotNone(self.hls_stream.format)
        self.assertIsNotNone(self.hls_stream.bitrate)
        self.assertIsNotNone(self.hls_stream.listeners)
        self.assertIsNotNone(self.hls_stream.id)
        self.assertIsNotNone(self.hls_stream.links)
        self.assertIsNotNone(self.hls_stream._station)

if __name__ == '__main__':
    unittest.main()