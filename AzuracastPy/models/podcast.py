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
    """Represents the links associated with a podcast."""
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
        """
        Initializes a :class:`Links` object for a podcast.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``podcast.links``.
        """
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
    """Provides functions for working with the episodes of a podcast."""
    def __init__(
        self,
        _podcast
    ):
        """
        Initializes a :class:`PodcastEpisodeHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``podcast.episode``.
        """
        self._podcast = _podcast

    def __call__(
        self,
        id: str
    ) -> PodcastEpisode:
        """
        Retrieves a specific episode from the podcast.

        :param id: The ID of the episode to be retrieved.

        :returns: A :class:`PodcastEpisode` object.

        Usage:

        .. code-block:: python

            episode = podcast.episode("episode-id")
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
        :param explicit: Is the episode explicit? Swearing? Sexual content?. Default: ``False``.

        :returns: A :class:`PodcastEpisode` object for the newly created episode.

        Usage:

        .. code-block:: python

            episode = podcast.episode.create(
                title="Tis a podcast",
                description="I'm not sure, but this might be a podcast",
                explicit=True
            )
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

        # Making a 'redundant' variable here to ensure that any "response does
        # not match PodcastEpisode" errors are raised **before** the ID is added
        # to the podcast's episode list.
        podcast = PodcastEpisode(**response, _podcast=self._podcast)

        self._podcast.episodes.append(response['id'])

        return podcast

    def all(self) -> List[PodcastEpisode]:
        """
        Retrieves the episodes of the podcast.

        :returns: A list of :class:`PodcastEpisode` objects.

        Usage:


        .. code-block:: python

            episodes = podcast.episode.all()
        """
        url = API_ENDPOINTS["podcast_episodes"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            podcast_id=self._podcast.id
        )

        response = self._podcast._station._request_handler.get(url)

        return [PodcastEpisode(**pe, _podcast=self._podcast) for pe in response]

class PodcastCategoryHelper:
    """Provides functions for working with the categories of a podcast."""
    def __init__(
        self,
        _podcast
    ):
        """
        Initializes a :class:`PodcastCategoryHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``podcast.category``.
        """
        self._podcast = _podcast

    def add(
        self,
        *args: PodcastCategories
    ):
        """
        Adds one or more categories to the podcast.

        :param args: The category|categories to be added to the podcast.
            All arguments must be from the :class:`PodcastCategories` enum.

        Usage:

        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            podcast.category.add(PodcastCategories.GOVERNMENT)

            podcast.category.add(
                PodcastCategories.Arts.BOOKS,
                PodcastCategories.HISTORY
            )
        """
        categories = self._podcast.categories.copy()

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be an attribute from the "\
                         f"'PodcastCategories' class."
                raise ClientException(message)

            if arg in categories:
                message = f"'{arg}' is already in the podcast's categories."
                raise ClientException(message)

            categories.append(arg)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            id=self._podcast.id
        )

        body = {
            "categories": categories
        }

        response = self._podcast._station._request_handler.put(url, body)

        if response['success'] is True:
            self._podcast.categories = categories

        return response

    def remove(
        self,
        *args: PodcastCategories
    ):
        """
        Removes one or more categories from the podcast.

        :param args: The category|categories to be removed from the podcast.
            All arguments must be from the :class:`PodcastCategories` enum.

        Usage:

        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            podcast.category.remove(PodcastCategories.GOVERNMENT)

            podcast.category.remove(
                PodcastCategories.Arts.BOOKS,
                PodcastCategories.HISTORY
            )
        """
        categories = self._podcast.categories.copy()

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be an attribute from the "\
                         f"'PodcastCategories' class."
                raise ClientException(message)

            if arg not in categories:
                message = f"'{arg}' is not in the podcast's categories."
                raise ClientException(message)

            categories.remove(arg)

        url = API_ENDPOINTS["station_podcast"].format(
            radio_url=self._podcast._station._request_handler.radio_url,
            station_id=self._podcast._station.id,
            id=self._podcast.id
        )

        body = {
            "categories": categories
        }

        response = self._podcast._station._request_handler.put(url, body)

        if response['success'] is True:
            self._podcast.categories = categories

        return response

class Podcast:
    """Represents a podcast on a station."""
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
        """
        Initializes a :class:`Podcast` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.models.helpers.PodcastHelper.create`,
            :meth:`~.models.helpers.PodcastHelper.__call__` or
            :meth:`~.models.Station.podcasts`.
        """
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
        self.links = Links(**links)
        self._station = _station

        self.episode = PodcastEpisodeHelper(_podcast=self)
        """
        An instance of :class:`.PodcastEpisodeHelper`.

        Provides the interface for working with this podcast's episodes.

        For example, to get all the episodes in this podcast:

        .. code-block:: python

            episodes = podcast.episode.all()

        To get an episode with an ID of ``"episode-id"``:

        .. code-block:: python

            episode = podcast.episode("episode-id")

        To create a new podcast episode:

        .. code-block:: python

            episode = podcast.episode.create(
                title="Tis a podcast",
                description="I'm not sure, but this might be a podcast",
                explicit=True
            )
        """

        self.category = PodcastCategoryHelper(_podcast=self)
        """
        An instance of :class:`.PodcastCategoryHelper`.

        Provides the interface for working with this podcast's categories.

        For example, to add one or more categories to this podcast:

        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            podcast.category.add(PodcastCategories.GOVERNMENT)

            podcast.category.add(
                PodcastCategories.Arts.BOOKS,
                PodcastCategories.HISTORY
            )

        To remove one or more categories from this podcast:

        .. code-block:: python

            from AzuracastPy.enums import PodcastCategories

            podcast.category.remove(PodcastCategories.GOVERNMENT)

            podcast.category.remove(
                PodcastCategories.Arts.BOOKS,
                PodcastCategories.HISTORY
            )
        """

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

            .. warning::

                This will overwrite the podcast's existing categories.
                Use the :meth:`~.models.podcast.PodcastCategoryHelper.add` and
                :meth:`~.models.podcast.PodcastCategoryHelper.remove` methods to
                interact with the podcast's existing categories.

        :param author: (Optional) The new author of the podcast. Default: ``None``.
        :param email: (Optional) The new email of the podcast. Default: ``None``.
        :param website: (Optional) The new website url of the podcast. Default: ``None``.

        Usage:

        .. code-block:: python

            from AzuracastPy.enums import Languages, PodcastCategories

            podcast.edit(
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

            podcast.delete()
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
