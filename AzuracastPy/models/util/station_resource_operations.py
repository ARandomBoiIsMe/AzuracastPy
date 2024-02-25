from AzuracastPy.constants import API_ENDPOINTS

def edit_station_resource(self, resource_type: str, *args):
    url = API_ENDPOINTS[resource_type].format(
        radio_url=self._station._request_handler.radio_url,
        station_id=self._station.id,
        id=self.id
    )

    body = self._build_update_body(*args)

    response = self._station._request_handler.put(url, body)

    if response['success'] is True:
        self._update_properties(*args)

    return response

def delete_station_resource(self, resource_type: str):
    url = API_ENDPOINTS[resource_type].format(
        radio_url=self._station._request_handler.radio_url,
        station_id=self._station.id,
        id=self.id
    )

    response = self._station._request_handler.delete(url)

    if response['success'] is True:
        self._clear_properties()

    return response