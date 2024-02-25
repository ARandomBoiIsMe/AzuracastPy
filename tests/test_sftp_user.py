from AzuracastPy.exceptions import ClientException

import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.sftp_user = fake_data_generator.return_fake_sftp_user_instance()
        self.sftp_user._station = mock.MagicMock()
        self.response = Response()

    def test_successful_sftp_user_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.edit(
            username="New username",
            public_keys=["alicia", "keys"]
        )

        self.assertEqual(self.sftp_user.username, "New username")
        self.assertEqual(self.sftp_user.public_keys, ["alicia", "keys"])

    def test_failed_sftp_user_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.edit(
            username="New username",
            public_keys=["alicia", "keys"]
        )

        self.assertNotEqual(self.sftp_user.username, "New username")
        self.assertNotEqual(self.sftp_user.public_keys, ["alicia", "keys"])

    def test_successful_sftp_user_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.sftp_user._station._request_handler.delete.return_value = self.response.json()

        self.sftp_user.delete()

        self.assertIsNone(self.sftp_user.username)
        self.assertIsNone(self.sftp_user.password)
        self.assertIsNone(self.sftp_user.public_keys)
        self.assertIsNone(self.sftp_user.id)
        self.assertIsNone(self.sftp_user.links)
        self.assertIsNone(self.sftp_user._station)

    def test_failed_sftp_user_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.sftp_user._station._request_handler.delete.return_value = self.response.json()

        self.sftp_user.delete()

        self.assertIsNotNone(self.sftp_user.username)
        self.assertIsNotNone(self.sftp_user.password)
        self.assertIsNotNone(self.sftp_user.public_keys)
        self.assertIsNotNone(self.sftp_user.id)
        self.assertIsNotNone(self.sftp_user.links)
        self.assertIsNotNone(self.sftp_user._station)

    def test_successful_sftp_user_key_addition(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        self.response._content = '{"success": true}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.key.add(
            "alicia!",
            "keys!"
        )

        self.assertIn("alicia!", self.sftp_user.public_keys)
        self.assertIn("keys!", self.sftp_user.public_keys)

    def test_failed_sftp_user_key_addition(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        self.response._content = '{"success": false}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.key.add(
            "alicia!",
            "keys!"
        )

        self.assertNotIn("alicia!", self.sftp_user.public_keys)
        self.assertNotIn("keys!", self.sftp_user.public_keys)

    def test_sftp_user_key_addition_raises_error_if_key_is_already_in_the_sftp_user(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        with self.assertRaises(ClientException):
            self.sftp_user.key.add(
                "key1"
            )

    def test_sftp_user_key_addition_raises_error_if_key_is_invalid(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        with self.assertRaises(ClientException):
            self.sftp_user.key.add(1)

    def test_successful_sftp_user_key_removal(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        self.response._content = '{"success": true}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.key.remove(
            "key1"
        )

        self.assertNotIn("key1", self.sftp_user.public_keys)

    def test_failed_sftp_user_key_removal(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        self.response._content = '{"success": false}'.encode()

        self.sftp_user._station._request_handler.put.return_value = self.response.json()

        self.sftp_user.key.remove(
            "key1"
        )

        self.assertIn("key1", self.sftp_user.public_keys)

    def test_sftp_user_key_removal_raises_error_if_key_not_in_the_sftp_user(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        with self.assertRaises(ClientException):
            self.sftp_user.key.remove(
                "alicia"
            )

    def test_sftp_user_key_removal_raises_error_if_key_is_invalid(self):
        self.sftp_user.public_keys = [
            "key1",
            "key2"
        ]

        with self.assertRaises(ClientException):
            self.sftp_user.key.remove(True)

if __name__ == '__main__':
    unittest.main()