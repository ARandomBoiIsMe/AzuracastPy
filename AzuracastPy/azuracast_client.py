from typing import Optional, List, Union

from .models import Station

from .request_handler import RequestHandler
from .constants import API_ENDPOINTS

class AzuracastClient:
    # Docstring here

    def __init__(self, radio_url: str, x_api_key: Optional[str] = None):
        """
        Constructs an Azuracast API client.

        :param radio_url: Your radio's URL, which was set upon its creation.
        :param x_api_key: An optional authorization key, which can be created from your Azuracast account's profile. Include this key to gain access to specific endpoints.
        """
        # TODO: Handle lack of url and x_api_key here. Soon.
        self._request_handler = RequestHandler(radio_url=radio_url, x_api_key=x_api_key)

    def stations(self) -> List[Station]:
        """
        Retrieves list of stations on the radio.
        Constructs and returns a list of :class:`Station` instances.
        """
        url = API_ENDPOINTS["stations"].format(
            radio_url=self._request_handler.radio_url
        )

        response = self._request_handler.get(url)

        return [Station(**station, _request_handler=self._request_handler) for station in response]

    def station(self, id: int) -> Station:
        """
        Retrieves a specified station on the radio.
        Constructs and returns a single instance of :class:`Station`.

        :param id: The numerical ID of the station to be retrieved.
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