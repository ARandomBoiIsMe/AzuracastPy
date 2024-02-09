from AzuracastPy.models import PodcastEpisode

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
            with self.assertRaises(ValueError):
                self.podcast.episode(id)