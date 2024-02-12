"""Class for an SFTP user of a station."""

from typing import Optional, List, Union

from ..constants import API_ENDPOINTS
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    """Represents the links associated with an SFTP user."""
    def __init__(
        self_,
        self
    ):
        """
        Initializes a :class:`Links` instance for an SFTP user.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``sftp_user.links``.
        """
        self_.self = self

    def __repr__(self):
        return generate_repr_string(self)

class PublicKeysHelper:
    """Provides functions for working with the public keys of an SFTP user."""
    def __init__(
        self,
        _sftp_user
    ):
        """
        Initializes a :class:`PublicKeysHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``sftp_user.key``.
        """
        self._sftp_user = _sftp_user

    def add(
        self,
        *args: str
    ):
        """
        Adds one or more keys to the SFTP user.

        :param args: The key(s) to be added to the user.
            All arguments must be strings.

        Usage:
        .. code-block:: python

            sftp_user.key.add("key")

            sftp_user.key.add("key1", "key2")
        """
        public_keys = self._sftp_user.public_keys.copy()

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be a string."
                raise ClientException(message)

            if arg in public_keys:
                message = f"'{arg}' is already in the user's keys."
                raise ClientException(message)

            public_keys.append(arg)

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
        *args: str
    ):
        """
        Removes one or more keys from the SFTP user.

        :param args: The keys(s) to be removed from the user.
            All arguments must be strings.

        Usage:
        .. code-block:: python

            sftp_user.key.remove("key")

            sftp_user.key.remove("key1", "key2")
        """
        public_keys = self._sftp_user.public_keys.copy()

        for arg in args:
            if not isinstance(arg, str):
                message = "Each argument must be a string."
                raise ClientException(message)

            if arg not in public_keys:
                message = f"'{arg}' is not in the user's keys."
                raise ClientException(message)

            public_keys.remove(arg)

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
    """Represents an SFTP User on a station."""
    def __init__(
        self,
        id: int,
        username: str,
        password: str,
        publicKeys: str,
        links: Links,
        _station
    ):
        """
        Initializes a :class:`SFTPUser` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.sftp_user(id)`` or ``station.sftp_users()``.
        """
        self.id = id
        self.username = username
        self.password = password
        self.public_keys = publicKeys.split()
        self.links = Links(**links)
        self._station = _station

        self.key = PublicKeysHelper(_sftp_user=self)
        """
        An instance of :class:`.PublicKeysHelper`.

        Provides the interface for working with this SFTP user's public keys.

        For example, to assign one or more public keys to this user:

        .. code-block:: python

            sftp_user.key.add("key")

            sftp_user.key.add("key1", "key2")

        To remove one or more keys from this user:

        .. code-block:: python

            sftp_user.key.remove("key")

            sftp_user.key.remove("key1", "key2")
        """

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
            Note: This will overwrite the user's existing keys.
                  Use the :meth:`.key.add` and :meth:`.key.remove` methods to
                  interact with the user's existing keys.
            Default: ``None``.

        Usage:
        .. code-block:: python

            sftp_user.edit(
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

            sftp_user.update_password(
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

            sftp_user.delete()
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
