"""The client that provides access to the AzuraCast API."""

import configparser
import os
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

    This is how to obtain an instance of this class, with explicit parameters:

    .. code-block:: python

        from AzuracastPy import AzuracastClient

        client = AzuracastClient(
            radio_url="Your radio's public URL.",
            x_api_key="Your account's API key. This can be created from your profile on the site."
        )

    To achieve the same thing, but with a config file:

    .. code-block:: python

        from AzuracastPy import AzuracastClient

        client = AzuracastClient(
            config="Path to the '*.ini' configuration file containing the values."
        )
    """
    def __init__(
        self,
        radio_url: Optional[str] = None,
        x_api_key: Optional[str] = None,
        config: Optional[str] = None
    ):
        """
        Constructs an Azuracast API client.

        :param radio_url: (Optional) Your radio's URL, which was set upon its creation.
            Provide this or the 'config' param value.
            Default: ``None``.
        :param x_api_key: (Optional) Your account's API key,
            which can be generated from your profile.
            Provide this or the 'config' param value.
            Default: ``None``.
        :param config: (Optional) Path to the config file with the needed details.
            Provide this or the 'radio_url' and 'x_api_key' param values.
            Default: ``None``.

        If a 'config' param is provided, the values in the specified config file
        will overwrite the values of the 'radio_url' and 'x_api_key' params.
        """
        if not radio_url and not config:
            message = "Either the 'config' param or the 'radio_url' param "\
                      "must be provided."
            raise ClientException(message)

        if config:
            if not os.path.isfile(config):
                raise ValueError(f"File does not exist: {config}")

            if not config.endswith('.ini'):
                raise ValueError(f"Config file must be a '.ini' file: {config}")

            config_ = configparser.ConfigParser()
            config_.read(config)

            try:
                radio_url = config_['PARAM']['RADIO_URL']
                x_api_key = config_['PARAM']['X_API_KEY']
            except KeyError:
                raise ClientException("Please see the format for a valid config file here: # bleh")

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

        Usage:

        .. code-block:: python

            admin = client.admin()
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

        To get the now-playing details of a single station whose id is ``1``:

        .. code-block:: python

            station_now_playing = client.now_playing(1)

        To get the now-playing details of all stations on the radio:

        .. code-block:: python

            all_now_playing = client.now_playing()
        """
        url = self._build_now_playing_url(station_id)

        response = self._request_handler.get(url)

        if station_id:
            # The entire now_playing list is returned when an invalid station ID is passed.
            # API's rules, not mine.
            if isinstance(response, list):
                return [NowPlaying(**np) for np in response]

            return NowPlaying(**response)

        return [NowPlaying(**np) for np in response]

    def stations(self) -> List[Station]:
        """
        Retrieves list of stations on the radio.

        :returns: A list of :class:`Station` objects.

        Usage:

        .. code-block:: python

            stations = client.stations()
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

        Usage:

        .. code-block:: python

            station = client.station(1)
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

        Usage:

        .. code-block:: python

            status = client.status()
        """
        url = API_ENDPOINTS["api_status"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return response

    def time(self):
        """
        :returns: The current time.

        Usage:

        .. code-block:: python

            time = client.time()
        """
        url = API_ENDPOINTS["time"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return response
