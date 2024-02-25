from AzuracastPy import models

from AzuracastPy.exceptions import ClientException
from AzuracastPy.enums import (
    Languages,
    PodcastCategories
)

import unittest
from unittest import TestCase, mock
from requests import Response

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.podcast = fake_data_generator.return_fake_podcast_instance()
        self.podcast._station = mock.MagicMock()
        self.response = Response()

    def test_successful_podcast_edit(self):
        self.response._content = '{"success": true}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.edit(
            title="Brand new title",
            language=Languages.LATIN,
            categories=[
                PodcastCategories.Music.MUSIC_HISTORY,
                PodcastCategories.Education.LANGUAGE_LEARNING
            ],
            author='I AM not AN AUTHOR :('
        )

        self.assertEqual(self.podcast.title, "Brand new title")
        self.assertEqual(self.podcast.language, "la")
        self.assertEqual(self.podcast.categories, [
            PodcastCategories.Music.MUSIC_HISTORY,
            PodcastCategories.Education.LANGUAGE_LEARNING
            ]
        )
        self.assertEqual(self.podcast.author, "I AM not AN AUTHOR :(")

    def test_failed_podcast_edit(self):
        self.response._content = '{"success": false}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.edit(
            title="Brand new title",
            language=Languages.LATIN,
            categories=[
                PodcastCategories.Music.MUSIC_HISTORY,
                PodcastCategories.Education.LANGUAGE_LEARNING
            ],
            author='I AM not AN AUTHOR :('
        )

        self.assertNotEqual(self.podcast.title, "Brand new title")
        self.assertNotEqual(self.podcast.language, "la")
        self.assertNotEqual(self.podcast.categories, [
            PodcastCategories.Music.MUSIC_HISTORY,
            PodcastCategories.Education.LANGUAGE_LEARNING
            ]
        )
        self.assertNotEqual(self.podcast.author, "I AM not AN AUTHOR :(")

    def test_successful_podcast_delete(self):
        self.response._content = '{"success": true}'.encode()

        self.podcast._station._request_handler.delete.return_value = self.response.json()

        self.podcast.delete()

        self.assertIsNone(self.podcast.id)
        self.assertIsNone(self.podcast.storage_location_id)
        self.assertIsNone(self.podcast.title)
        self.assertIsNone(self.podcast.link)
        self.assertIsNone(self.podcast.description)
        self.assertIsNone(self.podcast.language)
        self.assertIsNone(self.podcast.author)
        self.assertIsNone(self.podcast.email)
        self.assertIsNone(self.podcast.has_custom_art)
        self.assertIsNone(self.podcast.art)
        self.assertIsNone(self.podcast.art_updated_at)
        self.assertIsNone(self.podcast.categories)
        self.assertIsNone(self.podcast.episodes)
        self.assertIsNone(self.podcast.links)
        self.assertIsNone(self.podcast._station)

    def test_failed_podcast_delete(self):
        self.response._content = '{"success": false}'.encode()

        self.podcast._station._request_handler.delete.return_value = self.response.json()

        self.podcast.delete()

        self.assertIsNotNone(self.podcast.id)
        self.assertIsNotNone(self.podcast.storage_location_id)
        self.assertIsNotNone(self.podcast.title)
        self.assertIsNotNone(self.podcast.link)
        self.assertIsNotNone(self.podcast.description)
        self.assertIsNotNone(self.podcast.language)
        self.assertIsNotNone(self.podcast.author)
        self.assertIsNotNone(self.podcast.email)
        self.assertIsNotNone(self.podcast.has_custom_art)
        self.assertIsNotNone(self.podcast.art)
        self.assertIsNotNone(self.podcast.art_updated_at)
        self.assertIsNotNone(self.podcast.categories)
        self.assertIsNotNone(self.podcast.episodes)
        self.assertIsNotNone(self.podcast.links)
        self.assertIsNotNone(self.podcast._station)

    def test_successful_podcast_category_addition(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        self.response._content = '{"success": true}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.category.add(
            PodcastCategories.Arts.DESIGN,
            PodcastCategories.Comedy.COMEDY_INTERVIEWS,
            PodcastCategories.Leisure.AVIATION
        )

        self.assertIn(PodcastCategories.Arts.DESIGN, self.podcast.categories)
        self.assertIn(PodcastCategories.Comedy.COMEDY_INTERVIEWS, self.podcast.categories)
        self.assertIn(PodcastCategories.Leisure.AVIATION, self.podcast.categories)

    def test_failed_podcast_category_addition(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        self.response._content = '{"success": false}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.category.add(
            PodcastCategories.Arts.DESIGN,
            PodcastCategories.Comedy.COMEDY_INTERVIEWS,
            PodcastCategories.Leisure.AVIATION
        )

        self.assertNotIn(PodcastCategories.Arts.DESIGN, self.podcast.categories)
        self.assertNotIn(PodcastCategories.Comedy.COMEDY_INTERVIEWS, self.podcast.categories)
        self.assertNotIn(PodcastCategories.Leisure.AVIATION, self.podcast.categories)

    def test_podcast_category_addition_raises_error_if_category_is_already_in_the_podcast(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        with self.assertRaises(ClientException):
            self.podcast.category.add(
                PodcastCategories.Arts.PERFORMING_ARTS,
                PodcastCategories.Comedy.COMEDY_INTERVIEWS,
                PodcastCategories.Leisure.AVIATION
            )

    def test_podcast_category_addition_raises_error_if_category_is_invalid(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        with self.assertRaises(ClientException):
            self.podcast.category.add(2)

    def test_successful_podcast_category_removal(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        self.response._content = '{"success": true}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.category.remove(
            PodcastCategories.Arts.PERFORMING_ARTS
        )

        self.assertNotIn(PodcastCategories.Arts.PERFORMING_ARTS, self.podcast.categories)

    def test_failed_podcast_category_removal(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        self.response._content = '{"success": false}'.encode()

        self.podcast._station._request_handler.put.return_value = self.response.json()

        self.podcast.category.remove(
            PodcastCategories.Arts.PERFORMING_ARTS
        )

        self.assertIn(PodcastCategories.Arts.PERFORMING_ARTS, self.podcast.categories)

    def test_podcast_category_removal_raises_error_if_category_not_in_the_podcast(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        with self.assertRaises(ClientException):
            self.podcast.category.remove(
                PodcastCategories.Comedy.COMEDY_INTERVIEWS,
                PodcastCategories.Leisure.AVIATION
            )

    def test_podcast_category_removal_raises_error_if_category_is_invalid(self):
        self.podcast.categories = [
            "Arts|Performing Arts",
            "Arts|Fashion & Beauty"
        ]

        with self.assertRaises(ClientException):
            self.podcast.category.remove(2)

    def test_podcast_episode_creation(self):
        self.podcast.episodes = []

        self.podcast._station._request_handler.post.return_value = fake_data_generator.return_fake_podcast_episode_json()
        self.podcast._station._request_handler.post.return_value['title'] = "Tis a podcast"
        self.podcast._station._request_handler.post.return_value['description'] = "I'm not sure, but this might be a podcast"
        self.podcast._station._request_handler.post.return_value['explicit'] = True

        result = self.podcast.episode.create(
            title="Tis a podcast",
            description="I'm not sure, but this might be a podcast",
            explicit=True
        )

        self.assertIsInstance(result, models.PodcastEpisode)
        self.assertIsInstance(result.links, models.podcast_episode.Links)

        self.assertEqual(result.title, "Tis a podcast")
        self.assertEqual(result.description, "I'm not sure, but this might be a podcast")
        self.assertEqual(result.explicit, True)

        self.assertIn(result.id, self.podcast.episodes)

    def test_episode_returns_podcast_episode(self):
        id = "meh"
        self.podcast._station._request_handler.get.return_value = fake_data_generator.return_fake_podcast_episode_json()

        result = self.podcast.episode(id)

        self.assertIsInstance(result, models.PodcastEpisode)
        self.assertIsInstance(result.links, models.podcast_episode.Links)

    def test_episode_returns_podcast_episode(self):
        id = "meh"
        self.podcast._station._request_handler.get.return_value = [
            fake_data_generator.return_fake_podcast_episode_json(),
            fake_data_generator.return_fake_podcast_episode_json()
        ]

        result = self.podcast.episode.all()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.PodcastEpisode)
            self.assertIsInstance(item.links, models.podcast_episode.Links)

if __name__ == '__main__':
    unittest.main()