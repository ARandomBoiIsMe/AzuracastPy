"""The client that provides access to the AzuraCast API."""

from typing import Optional, List, Union

from .models import Station, NowPlaying
from .models.administration.admin import Admin

from .request_handler import RequestHandler
from .constants import API_ENDPOINTS
from .exceptions import ClientException

class AzuracastClient:
    """
    The Azuracast API client.

    This will be used to access the data and actions provided by an Azuracast web radio.
    """
    def __init__(
        self,
        radio_url: Optional[str] = None,
        x_api_key: Optional[str] = None,
        config_file_path: Optional[str] = None
    ):
        """
        Constructs an Azuracast API client.

        :param radio_url: Your radio's URL, which was set upon its creation.
        :param x_api_key: (Optional) Your account's API key,
            which can be generated from your profile. Default: ``None``.
        """
        if not radio_url and not x_api_key and not config_file_path:
            raise ClientException("I need at least one value bro, damn...")

        if config_file_path:
            pass

        if "http://" not in radio_url and "https://" not in radio_url:
            raise ValueError("radio_url param must start with 'http://' or 'https://'")

        self._request_handler = RequestHandler(
            radio_url=radio_url.rstrip('/'),
            x_api_key=x_api_key
        )

    def _build_now_playing_url(
        self,
        station_id: Optional[int] = None
    ):
        if not station_id:
            return API_ENDPOINTS["all_now_playing"].format(
                radio_url=self._request_handler.radio_url
            )

        if type(station_id) is not int or station_id < 0:
            raise ValueError("station_id must be an non-negative integer.")

        return API_ENDPOINTS["station_now_playing"].format(
            radio_url=self._request_handler.radio_url,
            station_id=station_id
        )

    def admin(self) -> Admin:
        """
        Exposes administration actions for a radio.

        :returns: An :class:`Admin` object.
        """
        return Admin(_request_handler=self._request_handler)

    def now_playing(
        self,
        station_id: Optional[int] = None
    ) -> Union[List[NowPlaying], NowPlaying]:
        """
        Retrieves now playing information for a specific station or all stations.

        :param station_id: (Optional) The ID of the station to retrieve data for.
            If None, retrieves data for all stations. Default: ``None``.

        :returns: A list of :class:`NowPlaying` objects, or a single :class:`NowPlaying` object,
            depending on whether or not a ``station_id`` was provided.
        """
        url = self._build_now_playing_url(station_id)

        response = self._request_handler.get(url)

        if station_id:
            # The entire now_playing list is returned when an invalid station ID is passed.
            if isinstance(response, list):
                return [NowPlaying(**np) for np in response]

            return NowPlaying(**response)

        return [NowPlaying(**np) for np in response]

    def stations(self) -> List[Station]:
        """
        Retrieves list of stations on the radio.

        :returns: A list of :class:`Station` objects.
        """
        url = API_ENDPOINTS["stations"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return [Station(**s, _request_handler=self._request_handler) for s in response]

    def station(
        self,
        id: int
    ) -> Station:
        """
        Retrieves a specific station on the radio.

        :param id: The numerical ID of the station to be retrieved.

        :returns: A :class:`Station` object.
        """
        if type(id) is not int or id < 0:
            raise ValueError("id param must be a non-negative integer.")

        url = API_ENDPOINTS["station"].format(
            radio_url=self._request_handler.radio_url,
            station_id=id
        )

        response = self._request_handler.get(url)

        return Station(**response, _request_handler=self._request_handler)

    def status(self):
        """
        :returns: The status of the radio's API.
        """
        url = API_ENDPOINTS["api_status"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return response

    def time(self):
        """
        :returns: The current time.
        """
        url = API_ENDPOINTS["time"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return response
