from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.constants import API_ENDPOINTS

class Admin:
    def __init__(self, _request_handler: RequestHandler) -> None:
        self._request_handler = _request_handler
    
    def _request_multiple_instances_of(self, resource_name: str):
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id
        )

        return self._request_handler.get(url)
    
    def _request_single_instance_of(self, resource_name: str, resource_id: int):
        if type(resource_id) is not int:
            raise TypeError("id param should be of type int.")
        
        if resource_id < 0:
            raise ValueError("id must be a non-negative number.")
        
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url,
            station_id=self.id,
            id=resource_id
        )

        return self._request_handler.get(url)

    # def custom_fields(self) -> List[StationFile]:
    #     response = self._request_multiple_instances_of("station_files")

    #     return [StationFile(**sf, _station=self) for sf in response]
    
    # def file(self, id: int) -> StationFile:
    #     response = self._request_single_instance_of("station_file", id)

    #     return StationFile(**response, _station=self)