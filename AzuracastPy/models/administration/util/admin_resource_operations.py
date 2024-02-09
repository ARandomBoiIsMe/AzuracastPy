from AzuracastPy.constants import API_ENDPOINTS

def edit_admin_resource(self, resource_type: str, *args):
    url = API_ENDPOINTS[resource_type].format(
        radio_url=self._admin._request_handler.radio_url,
        id=self.id
    )

    body = self._build_update_body(*args)

    response = self._admin._request_handler.put(url, body)

    if response['success']:
        self._update_properties(*args)

    return response

def delete_admin_resource(self, resource_type: str):
    url = API_ENDPOINTS[resource_type].format(
        radio_url=self._admin._request_handler.radio_url,
        id=self.id
    )

    response = self._admin._request_handler.delete(url)

    if response['success']:
        self._clear_properties()

    return response