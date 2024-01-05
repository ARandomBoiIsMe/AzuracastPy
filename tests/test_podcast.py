from AzuracastPy.models.podcast_episode import PodcastEpisode

import unittest
from unittest import TestCase, mock

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.podcast = fake_data_generator.return_fake_podcast_instance()
        self.podcast._request_handler = mock.MagicMock()

    def test_podcast_episode_invalid_type_raises_type_error(self):
        incorrect_ids = [True, 2.0, 1]

        for id in incorrect_ids:
            with self.assertRaises(TypeError):
                self.podcast.podcast_episode(id)

    def test_podcast_returns_podcast(self):
        id = 'string-id'
        self.podcast._request_handler.get.return_value = fake_data_generator.return_fake_podcast_episode_json()
        
        result = self.podcast.podcast_episode(id)

        self.assertIsInstance(result, PodcastEpisode)

    def test_podcasts_returns_list_of_podcast(self):
        self.podcast._request_handler.get.return_value = [
            fake_data_generator.return_fake_podcast_episode_json(),
            fake_data_generator.return_fake_podcast_episode_json(),
            fake_data_generator.return_fake_podcast_episode_json()
        ]
        
        result = self.podcast.podcast_episodes()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, PodcastEpisode)