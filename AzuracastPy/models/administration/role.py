from typing import Dict, Any, Optional, List

from ...util.general_util import generate_repr_string, generate_enum_error_text
from ...enums import GlobalPermissions, StationPermissions
from ...constants import API_ENDPOINTS
from ...exceptions import ClientException

from .permissions import Permissions

class Links:
    def __init__(
        self_,
        self: str
    ):
        self_.self = self

    def __repr__(self) -> str:
        return generate_repr_string(self)

class PermissionsHelper:
    def __init__(
        self,
        _role
    ):
        self._role = _role

    def add_global(
        self,
        *args: GlobalPermissions
    ):
        """
        Adds one or more global permissions to the role.

        :param args: The permission(s) to be added to the role.
            All arguments must be from the :class:`GlobalPermissions` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions

            admin.permission.add_global(GlobalPermissions.ADMINISTER_ALL)

            admin.permission.add_global(
                GlobalPermissions.ADMINISTER_ALL,
                GlobalPermissions.ADMINISTER_BACKUPS
            )
        """
        permissions = self._role.permissions.global_permissions.copy()

        for arg in args:
            if not isinstance(arg, GlobalPermissions):
                message = "Each argument must be an attribute from the "\
                         f"'GlobalPermissions' enum class."
                raise ClientException(message)

            arg = arg.value

            if arg in permissions:
                message = f"'{arg}' is already in the role's global permissions."
                raise ClientException(message)

            permissions.append(arg)

        url = API_ENDPOINTS["role"].format(
            radio_url=self._role._admin._request_handler.radio_url,
            id=self._role.id
        )

        body = {
            "permissions": {
                "global": permissions,
                "station": self._role.permissions.station_permissions
            }
        }

        response = self._role._admin._request_handler.put(url, body)

        if response['success']:
            self._role.permissions.global_permissions = permissions

        return response

    def remove_global(
        self,
        *args: GlobalPermissions
    ):
        """
        Removes one or more global permissions from the role.

        :param args: The permission(s) to be removed from the role.
            All arguments must be from the :class:`GlobalPermissions` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions

            admin.permission.remove_global(GlobalPermissions.ADMINISTER_ALL)

            admin.permission.remove_global(
                GlobalPermissions.ADMINISTER_ALL,
                GlobalPermissions.ADMINISTER_BACKUPS
            )
        """
        permissions = self._role.permissions.global_permissions.copy()

        for arg in args:
            if not isinstance(arg, GlobalPermissions):
                message = "Each argument must be an attribute from the "\
                         f"'GlobalPermissions' enum class."
                raise ClientException(message)

            arg = arg.value

            if arg not in permissions:
                message = f"'{arg}' is not in the role's global permissions."
                raise ClientException(message)

            permissions.remove(arg)

        url = API_ENDPOINTS["role"].format(
            radio_url=self._role._admin._request_handler.radio_url,
            id=self._role.id
        )

        body = {
            "permissions": {
                "global": permissions,
                "station": self._role.permissions.station_permissions
            }
        }

        response = self._role._admin._request_handler.put(url, body)

        if response['success']:
            self._role.permissions.global_permissions = permissions

        return response

class Role:
    def __init__(
        self,
        id: int,
        name: str,
        permissions: Dict[Any, Any],
        links: Links,
        is_super_admin: bool,
        _admin
    ):
        self.id = id
        self.name = name
        self.permissions = Permissions.from_dict(permissions)
        self.links = links
        self.is_super_admin = is_super_admin
        self._admin = _admin

        self.permission = PermissionsHelper(_role=self)
        """
        An instance of :class:`.PermissionsHelper`.

        Provides the interface for working with this role's permissions.

        For example, to add one or more global permissions to this role:

        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions

            admin.permission.add_global(GlobalPermissions.ADMINISTER_ALL)

            admin.permission.add_global(
                GlobalPermissions.ADMINISTER_ALL,
                GlobalPermissions.ADMINISTER_BACKUPS
            )

        To remove one or more global permissions from this role:

        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions

            admin.permission.remove_global(GlobalPermissions.ADMINISTER_ALL)

            admin.permission.remove_global(
                GlobalPermissions.ADMINISTER_ALL,
                GlobalPermissions.ADMINISTER_BACKUPS
            )
        """

    def __repr__(self) -> str:
        return generate_repr_string(self)

    def edit(
        self,
        name: Optional[str] = None,
        global_permissions: Optional[List[GlobalPermissions]] = None,
        station_permissions: Optional[Dict[str, List[StationPermissions]]] = None
    ):
        """
        Edits the role's properties.

        Updates all edited attributes of the current :class:`Role` object.

        :param name: (Optional) The new name of the role. Default: ``None``
        :param global_permissions: (Optional) The new global permissions of the role.
            Default: ``None``.
        :param station_permissions: (Optional) The structure representing the new station
            permissions of the role. Generate this using the :meth:`.generate_station_permissions`
            function. Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions

            station.hls_stream(1).edit(
                name="New name",
                global_permissions=[
                    GlobalPermissions.ADMINISTER_BACKUPS,
                    GlobalPermissions.VIEW_ADMINISTRATION
                ]
            )
        """
        if global_permissions:
            if not all(isinstance(permission, GlobalPermissions) for permission in global_permissions):
                message = "All elements of the "\
                         f"{generate_enum_error_text('global_permissions', GlobalPermissions)}"
                raise ClientException(message)

            global_permissions = [permission.value for permission in global_permissions]

        # Generates station permissions structure.
        station_perms = {}
        if station_permissions:
            for station_id, permission_list in station_permissions.items():
                station_permissions[station_id] = [permission.value for permission in permission_list]

        url = API_ENDPOINTS["role"].format(
            radio_url=self._admin._request_handler.radio_url,
            id=self.id
        )

        body = self._build_update_body(name, global_permissions, station_perms)

        response = self._admin._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(name, global_permissions, station_perms)

        return response

    def delete(self):
        """
        Deletes the role from the radio.

        Sets all attributes of the current :class:`Role` object to ``None``.

        Usage:
        .. code-block:: python

            admin.role(1).delete()
        """
        url = API_ENDPOINTS["role"].format(
            radio_url=self._admin._request_handler.radio_url,
            id=self.id
        )

        response = self._admin._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response

    def _build_update_body(
        self,
        name,
        global_permissions,
        station_permissions
    ):
        return {
            "name": name if name else self.name,
            "permissions": {
                "global": global_permissions or self.permissions.global_permissions,
                "station": station_permissions or self.permissions.station_permissions
            }
        }

    def _update_properties(
        self,
        name,
        global_permissions,
        station_permissions
    ):
        self.name = name if name else self.name,
        self.permissions.global_permissions = global_permissions or self.permissions.global_permissions
        self.permissions.station_permissions = station_permissions or self.permissions.station_permissions

    def _clear_properties(self):
        self.id = None
        self.name = None
        self.permissions = None
        self.links = None
        self.is_super_admin = None
        self._admin = None
