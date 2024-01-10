from typing import Optional

from AzuracastPy.constants import API_ENDPOINTS
from AzuracastPy.util.general_util import generate_repr_string

class Links:
    def __init__(self_, self):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class SFTPUser:
    def __init__(self, id: int, username: str, password: str, publicKeys: str, links: Links, _station):
        self.id = id
        self.username = username
        self.password = password
        self.public_keys = publicKeys
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(self, username: Optional[str] = None, public_keys: Optional[str] = None):
        old_sftp_user = self._station.sftp_user(self.id)

        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(
            old_sftp_user, username, public_keys
        )

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                old_sftp_user, username, public_keys
            )
            
        return response
    
    def update_password(self, password: str):
        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = {
            "password": password
        }

        response = self._station._request_handler.put(url, body)

        return response
    
    def delete(self):
        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _build_update_body(self, old_sftp_user: "SFTPUser", username, public_keys):
        return {
            "username": username if username else old_sftp_user.username,
            "publicKeys": public_keys if public_keys else old_sftp_user.public_keys
        }
    
    def _update_properties(self, old_sftp_user: "SFTPUser", username, public_keys):
        self.username = username if username else old_sftp_user.username
        self.public_keys = public_keys if public_keys else old_sftp_user.public_keys

    def _clear_properties(self):
        self.id = None
        self.username = None
        self.password = None
        self.public_keys = None
        self.links = None
        self._station = None