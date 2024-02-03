"""Class for an SFTP user of a station."""

from typing import Optional, List

from ..constants import API_ENDPOINTS
from ..util.general_util import generate_repr_string

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_,
        self
    ):
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class SFTPUser:
    def __init__(
        self,
        id: int,
        username: str,
        password: str,
        publicKeys: str,
        links: Links,
        _station
    ):
        self.id = id
        self.username = username
        self.password = password
        self.public_keys = publicKeys.split()
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        username: Optional[str] = None,
        public_keys: Optional[List[str]] = None
    ):
        """
        Edits the SFTP user's properties.

        Updates all edited attributes of the current :class:`SFTPUser` object.

        :param username: (Optional) The new username of the SFTP user. Default: ``None``.
        :param public_keys: (Optional) The new list of public keys to be assigned to the user.
            Note: This will override the user's existing public keys.
                  Use the :meth:`.add_public_key` if you want to add a key item to
                  the user's existing keys.
            Default: ``None``.

        Usage:
        .. code-block:: python

            station.sftp_user(1).edit(
                username="New username",
                public_keys=["alicia", "keys"]
            )
        """
        return edit_station_resource(self, "station_sftp_user", username, public_keys)

    def update_password(
        self,
        password: str
    ):
        """
        Updates the SFTP user's password.

        :param password: The SFTP user's new password.

        Usage:
        .. code-block:: python

            station.sftp_user(1).update_password(
                password="new password"
            )
        """
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

    def add_public_key(
        self,
        public_key: str
    ):
        """
        Assigns a new public key to the SFTP user.

        :param public_key: The key to be added to the SFTP user.

        Usage:
        .. code-block:: python

            station.sftp_user(1).add_public_key(
                public_key="new_key"
            )
        """
        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        public_keys = self.public_keys
        public_keys.append(public_key)
        body = {
            "publicKeys": '\n'.join(public_keys)
        }

        response = self._station._request_handler.put(url, body)

        if response['success']:
            # Updates the SFTP user's properties on the object.
            self.public_keys = public_keys

        return response

    def delete(self):
        """
        Deletes the SFTP user from the station.

        Sets all attributes of the current :class:`SFTPUser` object to ``None``.

        Usage:
        .. code-block:: python

            station.sftp_user(1).delete()
        """
        return delete_station_resource(self, "station_sftp_user")

    def _build_update_body(
        self,
        username,
        public_keys
    ):
        return {
            "username": username or self.username,
            "publicKeys": '\n'.join(public_keys) if public_keys else '\n'.join(self.public_keys)
        }

    def _update_properties(
        self,
        username,
        public_keys
    ):
        self.username = username or self.username
        self.public_keys = public_keys or self.public_keys

    def _clear_properties(self):
        self.id = None
        self.username = None
        self.password = None
        self.public_keys = None
        self.links = None
        self._station = None
