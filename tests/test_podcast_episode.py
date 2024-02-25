import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.podcast_episode = fake_data_generator.return_fake_podcast_episode_instance()
        self.podcast_episode._podcast = mock.MagicMock()
        self.response = Response()

    def test_successful_podcast_episode_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.podcast_episode._podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast_episode.edit(
            title="New episode title",
            description="New episode description",
            explicit=True
        )

        self.assertEqual(self.podcast_episode.title, "New episode title")
        self.assertEqual(self.podcast_episode.description, "New episode description")
        self.assertEqual(self.podcast_episode.explicit, True)

    def test_failed_podcast_episode_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.podcast_episode._podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast_episode.edit(
            title="New episode title",
            description="New episode description",
            explicit=True
        )

        self.assertNotEqual(self.podcast_episode.title, "New episode title")
        self.assertNotEqual(self.podcast_episode.description, "New episode description")
        self.assertNotEqual(self.podcast_episode.explicit, True)

    def test_successful_podcast_episode_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.podcast_episode._podcast._station._request_handler.delete.return_value = self.response.json()

        self.podcast_episode.delete()

        self.assertIsNone(self.podcast_episode.id)
        self.assertIsNone(self.podcast_episode.title)
        self.assertIsNone(self.podcast_episode.description)
        self.assertIsNone(self.podcast_episode.explicit)
        self.assertIsNone(self.podcast_episode.publish_at)
        self.assertIsNone(self.podcast_episode.has_media)
        self.assertIsNone(self.podcast_episode.media)
        self.assertIsNone(self.podcast_episode.has_custom_art)
        self.assertIsNone(self.podcast_episode.art)
        self.assertIsNone(self.podcast_episode.art_updated_at)
        self.assertIsNone(self.podcast_episode.links)
        self.assertIsNone(self.podcast_episode._podcast)

    def test_failed_podcast_episode_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.podcast_episode._podcast._station._request_handler.delete.return_value = self.response.json()

        self.podcast_episode.delete()
        
        self.assertIsNotNone(self.podcast_episode.id)
        self.assertIsNotNone(self.podcast_episode.title)
        self.assertIsNotNone(self.podcast_episode.description)
        self.assertIsNotNone(self.podcast_episode.explicit)
        self.assertIsNotNone(self.podcast_episode.publish_at)
        self.assertIsNotNone(self.podcast_episode.has_media)
        self.assertIsNotNone(self.podcast_episode.media)
        self.assertIsNotNone(self.podcast_episode.has_custom_art)
        self.assertIsNotNone(self.podcast_episode.art)
        self.assertIsNotNone(self.podcast_episode.art_updated_at)
        self.assertIsNotNone(self.podcast_episode.links)
        self.assertIsNotNone(self.podcast_episode._podcast)

if __name__ == '__main__':
    unittest.main()