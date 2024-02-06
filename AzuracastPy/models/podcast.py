"""Class for a station podcast."""

from typing import List, Optional

from ..constants import API_ENDPOINTS
from ..enums import Languages, PodcastCategories
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string, generate_enum_error_text
from ..util.media_util import get_resource_art

from .util.station_resource_operations import edit_station_resource, delete_station_resource

from .podcast_episode import PodcastEpisode

class Links:
    def __init__(
        self_,
        self: str,
        episodes: str,
        public_episodes: str,
        public_feed: str,
        art: str,
        episode_new_art: str,
        episode_new_media: str
    ):
        self_.self = self
        self_.episodes = episodes
        self_.public_episodes = public_episodes
        self_.public_feed = public_feed
        self_.art = art
        self_.episode_new_art = episode_new_art
        self_.episode_new_media = episode_new_media

    def __repr__(self):
        return generate_repr_string(self)

class PodcastEpisodeHelper:
    def __init__(
        self,
        _podcast
    ):
        self._podcast = _podcast

    def __call__(
        self,
        id: str
    ) -> PodcastEpisode:
        """
        Retrieves a specific episode from the podcast.

        :param id: The ID of the episode to be retrieved.

        :returns: A :class:`PodcastEpisode` object.
        """
        if not isinstance(id, str):
            raise ValueError("id param should be of type string.")

        url = API_ENDPOINTS["podcast_episode"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id,
            id=id
        )

        response = self._podcast._station._request_handler.get(url)

        return PodcastEpisode(**response, _podcast=self._podcast)

    # TODO: Media and art require file uploads
    # TODO: Schedule episode release
    def create(
        self,
        title: str,
        description: str,
        explicit: bool = False
    ) -> PodcastEpisode:
        """
        Adds an episode to the podcast.

        :param title: The title of the episode.
        :param description: A description of the episode.
        :param explicit: Is the episode explicit? Swearing? Sexual content?

        :returns: A :class:`PodcastEpisode` object for the newly created episode.
        """
        url = url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id
        )

        body = {
            "title": title,
            "description": description,
            "explicit": explicit
        }

        response = self._podcast._station._request_handler.post(url, body)

        self._podcast.episodes.append(response['id'])

        return PodcastEpisode(**response, _podcast=self._podcast)

    def all(self) -> List[PodcastEpisode]:
        """
        Retrieves the episodes of the podcast.

        :returns: A list of :class:`PodcastEpisode` objects.
        """
        url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id
        )

        response = self._podcast._station._request_handler.get(url)

        return [PodcastEpisode(**pe, _podcast=self._podcast) for pe in response]

class PodcastCategoryHelper:
    def __init__(
        self,
        _podcast
    ):
        self._podcast = _podcast

    def add(
        self,
        category: PodcastCategories
    ):
        """
        Adds a category to the podcast.

        :param category: The category to be added to the podcast.
            It must be from the :class:`PodcastCategories` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            station(1).podcast(1).category.add(
                category=PodcastCategories.SONG_CHANGED
            )
        """
        if any(category == existing_category for existing_category in self._podcast.categories):
            message = f"The '{category}' category is already in the podcast's current category list."
            raise ClientException(message)

        categories = self._podcast.categories.copy()
        categories.append(category)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            id=self._podcast.id
        )

        body = {
            "categories": categories
        }

        response = self._podcast._station._request_handler.put(url, body)

        if response['success']:
            self._podcast.categories = categories

        return response

    def remove(
        self,
        category: PodcastCategories
    ):
        """
        Removes a category from the podcast's current category list.

        :param category: The category to be removed from the podcast's category list.
            It must be from the :class:`PodcastCategories` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            station(1).podcast(1).category.remove(
                category=PodcastCategories.GOVERNMENT
            )
        """
        categories = self._podcast.categories.copy()

        try:
            categories.remove(category)
        except ValueError:
            message = f"The '{category}' category is not in the podcast's current category list."
            raise ClientException(message)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            id=self._podcast.id
        )

        body = {
            "categories": categories
        }

        response = self._podcast._station._request_handler.put(url, body)

        if response['success']:
            self._podcast.categories = categories

        return response

class Podcast:
    def __init__(
        self,
        id: str,
        storage_location_id: int,
        title: str,
        link: str,
        description: str,
        language: str,
        author: str,
        email: str,
        has_custom_art: bool,
        art: str,
        art_updated_at: int,
        categories: List[str],
        episodes: List[str],
        links: Links,
        _station
    ):
        self.id = id
        self.storage_location_id = storage_location_id
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.author = author
        self.email = email
        self.has_custom_art = has_custom_art
        self.art = art
        self.art_updated_at = art_updated_at
        self.categories = categories
        self.episodes = episodes
        self.links = links
        self._station = _station

        self.episode = PodcastEpisodeHelper(_podcast=self)
        self.category = PodcastCategoryHelper(_podcast=self)

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        language: Optional[Languages] = None,
        categories: Optional[List[PodcastCategories]] = None,
        author: Optional[str] = None,
        email: Optional[str] = None,
        website: Optional[str] = None
    ):
        """
        Edits the podcast's properties.

        Updates all edited attributes of the current :class:`Podcast` object.

        :param title: (Optional) The new title of the podcast. Default: ``None``.
        :param description: (Optional) The new description of the podcast. Default: ``None``.
        :param language: (Optional) The new language of the podcast. Default: ``None``.
        :param categories: (Optional) A list of the categories that the podcast falls under.
            Each element of the list must be from the ``PodcastCategories`` class.
            Default: ``None``.
        :param author: (Optional) The new author of the podcast. Default: ``None``.
        :param email: (Optional) The new email of the podcast. Default: ``None``.
        :param website: (Optional) The new website url of the podcast. Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import Languages, PodcastCategories

            station.podcast(1).edit(
                title="New title",
                language=Languages.BULGARIAN,
                categories=[
                    PodcastCategories.GOVERNMENT,
                    PodcastCategories.HISTORY
                ]
            )
        """
        if language:
            if not isinstance(language, Languages):
                raise ClientException(generate_enum_error_text("language", Languages))

            language = language.value

        return edit_station_resource(
            self, "station_podcast", title, description, language, author, email, website,
            categories
        )

    def delete(self):
        """
        Deletes the podcast from the station.

        Sets all attributes of the current :class:`Podcast` object to ``None``.

        Usage:
        .. code-block:: python

            station.podcast(1).delete()
        """
        return delete_station_resource(self, "station_podcast")

    def _build_update_body(
        self,
        title,
        description,
        language,
        author,
        email,
        website,
        categories
    ):
        return {
            "title": title or self.title,
            "description": description or self.description,
            "language": language or self.language,
            "author": author or self.author,
            "email": email or self.email,
            "link": website or self.link,
            "categories": categories or self.categories
        }

    def _update_properties(
        self,
        title,
        description,
        language,
        author,
        email,
        website,
        categories
    ):
        self.title = title or self.title
        self.description = description or self.description
        self.language = language or self.language
        self.author = author or self.author
        self.email = email or self.email
        self.link = website or self.link
        self.categories = categories or self.categories

    def _clear_properties(self):
        self.id = None
        self.storage_location_id = None
        self.title = None
        self.link = None
        self.description = None
        self.language = None
        self.author = None
        self.email = None
        self.has_custom_art = None
        self.art = None
        self.art_updated_at = None
        self.categories = None
        self.episodes = None
        self.links = None
        self._station = None

    def get_art(self) -> bytes:
        return get_resource_art(self)
