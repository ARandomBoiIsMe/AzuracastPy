from AzuracastPy.exceptions import ClientException
from AzuracastPy.enums import (
    WebhookTriggers
)

import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.webhook = fake_data_generator.return_fake_webhook_instance()
        self.webhook._station = mock.MagicMock()
        self.response = Response()

    def test_successful_webhook_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.edit(
            name="New name lol",
            triggers=[
                WebhookTriggers.LIVE_DISCONNECT,
                WebhookTriggers.SONG_CHANGED
            ]
        )

        self.assertEqual(self.webhook.name, "New name lol")
        self.assertEqual(self.webhook.triggers, [
            WebhookTriggers.LIVE_DISCONNECT.value,
            WebhookTriggers.SONG_CHANGED.value
            ]
        )

    def test_failed_webhook_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.edit(
            name="New name lol",
            triggers=[
                WebhookTriggers.LIVE_DISCONNECT,
                WebhookTriggers.SONG_CHANGED
            ]
        )

        self.assertNotEqual(self.webhook.name, "New name lol")
        self.assertNotEqual(self.webhook.triggers, [
            WebhookTriggers.LIVE_DISCONNECT.value,
            WebhookTriggers.SONG_CHANGED.value
            ]
        )

    def test_successful_webhook_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.webhook._station._request_handler.delete.return_value = self.response.json()

        self.webhook.delete()

        self.assertIsNone(self.webhook.name)
        self.assertIsNone(self.webhook.type)
        self.assertIsNone(self.webhook.is_enabled)
        self.assertIsNone(self.webhook.triggers)
        self.assertIsNone(self.webhook.config)
        self.assertIsNone(self.webhook.id)
        self.assertIsNone(self.webhook.links)
        self.assertIsNone(self.webhook._station)

    def test_failed_webhook_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.webhook._station._request_handler.delete.return_value = self.response.json()

        self.webhook.delete()

        self.assertIsNotNone(self.webhook.name)
        self.assertIsNotNone(self.webhook.type)
        self.assertIsNotNone(self.webhook.is_enabled)
        self.assertIsNotNone(self.webhook.triggers)
        self.assertIsNotNone(self.webhook.config)
        self.assertIsNotNone(self.webhook.id)
        self.assertIsNotNone(self.webhook.links)
        self.assertIsNotNone(self.webhook._station)

    def test_successful_webhook_trigger_addition(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        self.response._content = '{"success": true}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.trigger.add(
            WebhookTriggers.SONG_CHANGED,
            WebhookTriggers.LIVE_CONNECT
        )

        self.assertIn(WebhookTriggers.SONG_CHANGED.value, self.webhook.triggers)
        self.assertIn(WebhookTriggers.LIVE_CONNECT.value, self.webhook.triggers)

    def test_failed_webhook_trigger_addition(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        self.response._content = '{"success": false}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.trigger.add(
            WebhookTriggers.SONG_CHANGED,
            WebhookTriggers.LIVE_CONNECT
        )

        self.assertNotIn(WebhookTriggers.SONG_CHANGED.value, self.webhook.triggers)
        self.assertNotIn(WebhookTriggers.LIVE_CONNECT.value, self.webhook.triggers)

    def test_webhook_trigger_addition_raises_error_if_trigger_is_already_in_the_webhook(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        with self.assertRaises(ClientException):
            self.webhook.trigger.add(
                WebhookTriggers.LISTENER_LOST
            )

    def test_webhook_trigger_addition_raises_error_if_trigger_is_invalid(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        with self.assertRaises(ClientException):
            self.webhook.trigger.add("lol")

    def test_successful_webhook_trigger_removal(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        self.response._content = '{"success": true}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.trigger.remove(
            WebhookTriggers.LISTENER_LOST
        )

        self.assertNotIn(WebhookTriggers.LISTENER_LOST.value, self.webhook.triggers)

    def test_failed_webhook_trigger_removal(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        self.response._content = '{"success": false}'.encode()

        self.webhook._station._request_handler.put.return_value = self.response.json()

        self.webhook.trigger.remove(
             WebhookTriggers.LISTENER_LOST
        )

        self.assertIn( WebhookTriggers.LISTENER_LOST.value, self.webhook.triggers)

    def test_webhook_trigger_removal_raises_error_if_trigger_not_in_the_webhook(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        with self.assertRaises(ClientException):
            self.webhook.trigger.remove(
                WebhookTriggers.SONG_CHANGED
            )

    def test_webhook_trigger_removal_raises_error_if_trigger_is_invalid(self):
        self.webhook.triggers = [
            "listener_lost"
        ]

        with self.assertRaises(ClientException):
            self.webhook.trigger.remove("hi again")

if __name__ == '__main__':
    unittest.main()