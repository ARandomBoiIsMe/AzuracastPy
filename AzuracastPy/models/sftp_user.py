"""Class for an SFTP user of a station."""

from typing import Optional, List

from ..constants import API_ENDPOINTS
from ..exceptions import ClientException
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

class PublicKeysHelper:
    def __init__(
        self,
        _sftp_user
    ):
        self._sftp_user = _sftp_user

    def add(
        self,
        public_key: str
    ):
        """
        Assigns a new public key to the SFTP user.

        :param public_key: The key to be added to the SFTP user.

        Usage:
        .. code-block:: python

            station.sftp_user(1).key.add(
                public_key="new_key"
            )
        """
        if any(public_key == key for key in self._sftp_user.public_keys):
            message = f"The '{public_key}' key is already in the user's current public key list."
            raise ClientException(message)

        public_keys = self._sftp_user.public_keys.copy()
        public_keys.append(public_key)

        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._sftp_user._station._request_handler.radio_url,
            station_id=self._sftp_user._station.id,
            id=self._sftp_user.id
        )

        body = {
            "publicKeys": '\n'.join(public_keys)
        }

        response = self._sftp_user._station._request_handler.put(url, body)

        if response['success']:
            self._sftp_user.public_keys = public_keys

        return response

    def remove(
        self,
        public_key: str
    ):
        """
        Removes a public key from the SFTP user's current keys.

        :param public_key: The key to be removed from the SFTP user.

        Usage:
        .. code-block:: python

            station.sftp_user(1).key.remove(
                public_key="key"
            )
        """
        public_keys = self._sftp_user.public_keys.copy()

        try:
            public_keys.remove(public_key)
        except ValueError:
            message = f"The '{public_key}' key is not in the user's current public key list."
            raise ClientException(message)

        url = API_ENDPOINTS["station_sftp_user"].format(
            radio_url=self._sftp_user._station._request_handler.radio_url,
            station_id=self._sftp_user._station.id,
            id=self._sftp_user.id
        )

        body = {
            "publicKeys": '\n'.join(public_keys)
        }

        response = self._sftp_user._station._request_handler.put(url, body)

        if response['success']:
            self._sftp_user.public_keys = public_keys

        return response

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

        self.key = PublicKeysHelper(_sftp_user=self)

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
