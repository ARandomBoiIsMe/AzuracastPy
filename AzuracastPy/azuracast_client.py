from typing import Optional, List, Union

from .models import Station, NowPlaying
from .models.administration.admin import Admin

from .request_handler import RequestHandler
from .constants import API_ENDPOINTS

class AzuracastClient:
    """
    The Azuracast API client.

    This will be used to access the data and actions provided by an Azuracast web radio.
    """
    def __init__(
        self, 
        radio_url: str, 
        x_api_key: Optional[str] = None
    ):
        """
        Constructs an Azuracast API client.

        :param radio_url: Your radio's URL, which was set upon its creation.
        :param x_api_key: An optional authorization key, which can be created from your Azuracast account's profile. Include this key to gain access to specific functionality.
        """
        # TODO: Handle lack of url and x_api_key here. Soon.
        self._request_handler = RequestHandler(radio_url=radio_url, x_api_key=x_api_key)

    def _build_now_playing_url(
        self,
        station_id: Optional[int] = None
    ):
        if station_id is None:
            return API_ENDPOINTS["all_now_playing"].format(
                radio_url=self._request_handler.radio_url
            )

        if type(station_id) is not int:
            raise TypeError("station_id must be an integer.")
        
        if station_id < 0:
            raise ValueError("station_id must be a non-negative number.")
        
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

        :param station_id: (Optional) The ID of the station to retrieve data for. If None, retrieves data for all stations. Default: ``None``.

        :returns: A list of :class:`NowPlaying` objects, or a single :class:`NowPlaying` object, depending on whether or not a ``station_id`` was provided. 
        """
        url = self._build_now_playing_url(station_id)

        response = self._request_handler.get(url)

        if station_id is not None:
            # The entire now_playing list is returned when an invalid station ID is passed.
            if isinstance(response, list):
                return [NowPlaying(**data) for data in response]
            
            return NowPlaying(**response)
        
        return [NowPlaying(**data) for data in response]

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
        if type(id) is not int:
            raise TypeError("id param should be of type int.")
        
        if id < 0:
            raise ValueError("id must be a non-negative number.")

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
    
    def cpu_stats(self):
        """
        :returns: The statistics of the system running the web radio.
        """
        url = API_ENDPOINTS["cpu_stats"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return response