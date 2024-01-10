from typing import List

from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.constants import API_ENDPOINTS

from .admin_station import AdminStation

class Admin:
    def __init__(self, _request_handler: RequestHandler) -> None:
        self._request_handler = _request_handler
    
    def _request_multiple_instances_of(self, resource_name: str):
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url
        )

        return self._request_handler.get(url)
    
    def _request_single_instance_of(self, resource_name: str, resource_id: int):
        if type(resource_id) is not int:
            raise TypeError("id param should be of type int.")
        
        if resource_id < 0:
            raise ValueError("id must be a non-negative number.")
        
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            id=resource_id
        )

        return self._request_handler.get(url)
    
    def stations(self) -> List[AdminStation]:
        response = self._request_multiple_instances_of("admin_stations")

        return [AdminStation(**a) for a in response]

    def station(self, id: int) -> List[AdminStation]:
        response = self._request_single_instance_of("admin_station", id)

        return AdminStation(**response)