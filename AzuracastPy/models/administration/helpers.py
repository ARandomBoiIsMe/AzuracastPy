from typing import Optional, Dict, Any, List, Tuple

from ...exceptions import ClientException
from ...enums import GlobalPermissions, StationPermissions, AutoAssignValues
from ...constants import API_ENDPOINTS
from ...util.general_util import (
    convert_to_short_name,
    is_text_a_valid_short_name,
    generate_enum_error_text
)

from .admin_station import AdminStation
from .role import Role
from .custom_field import CustomField
from .storage_location import StorageLocation

def _request_single_instance_of_admin_resource(
    admin,
    resource_name,
    resource_id
):
    if type(resource_id) is not int or resource_id < 0:
        raise ValueError("id param must be a non-negative integer.")

    url = API_ENDPOINTS[resource_name].format(
        radio_url=admin._request_handler.radio_url,
        id=resource_id
    )

    return admin._request_handler.get(url)

class AdminStationHelper:
    """Provides a set of functions to interact with admin stations."""
    def __init__(
        self,
        _admin
    ):
        """
        Initializes a :class:`AdminStationHelpe` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.station``.
        """
        self._admin = _admin

    def __call__(
        self,
        id: int
    ) -> AdminStation:
        """
        Retrieves a specific station from the radio, with admin privileges.

        :param id: The numerical ID of the station to be retrieved.

        :returns: A :class:`AdminStation` object.

        Usage:
        .. code-block:: python

            admin_station = admin.admin_station(1)
        """
        response = _request_single_instance_of_admin_resource(
            admin=self._admin,
            resource_name="admin_station",
            resource_id=id
        )

        return AdminStation(**response, _admin=self._admin)

class RoleHelper:
    """Provides a set of functions to interact with radio roles."""
    def __init__(
        self,
        _admin
    ):
        """
        Initializes a :class:`RoleHelper` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.role``.
        """
        self._admin = _admin

    def __call__(
        self,
        id: int
    ) -> Role:
        """
        Retrieves a specific role from the radio.

        :param id: The numerical ID of the role to be retrieved.

        :returns: A :class:`Role` object.

        Usage:
        .. code-block:: python

            role = admin.role(1)
        """
        response = _request_single_instance_of_admin_resource(
            admin=self._admin,
            resource_name="role",
            resource_id=id
        )

        return Role(**response, _admin=self._admin)

    def generate_station_permission(
        self,
        station_name: Optional[str] = None,
        station_id: Optional[int] = None,
        permissions: Optional[List[StationPermissions]] = None
    ) -> Dict[str, List[str]]:
        """
        Generates a single station permissions for a role.

        :param station_name: (Optional) The name of the station where the permission will be
            assigned. Either provide this or the station_id param. Default: ``None``.
        :param station_id: (Optional) The id of the station where the permission will be
            assigned. Either provide this or the station_name param. Default: ``None``.
        :param permissions: (Optional) The list of permissions to assign to the station.
            Each element in this list must be from the ``StationPermissions`` enum class.
            If ``None``, all permissions will be given by default. Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import StationPermissions

            station_permission = admin.role.generate_station_permission(
                station_name="station name",
                station_id=1,
                permissions=[
                    StationPermissions.ADMINISTER_ALL,
                    StationPermissions.VIEW_STATION_LOGS
                ]
            )
        """
        if not station_id and not station_name:
            message = "Either 'station_id' or 'station_name' has to be provided to identify "\
                      "the station."
            raise ClientException(message)

        if not permissions: # Set default permission.
            permissions = [StationPermissions.ADMINISTER_ALL]
        else: # Check given permissions.
            if not all(isinstance(permission, StationPermissions) for permission in permissions):
                message = "All elements of the "\
                         f"{generate_enum_error_text('permissions', StationPermissions)}"
                raise ClientException(message)

        if station_id:
            station_id = int(station_id) # Just making sure.

            # Throws error if station doesn't exist.
            self._admin.station(station_id)

            return {f'{station_id}': permissions}

        if station_name:
            station_name = str(station_name) # Again, just making sure.

            # Why didn't you just give me an ID bro.
            stations = self._admin.stations()

            # Oh no, linear search! My complexity!
            for station in stations:
                if station.name.strip() == station_name.strip():
                    return {f'{station.id}': permissions}

            # Boo!
            message = f"No station named '{station_name.strip()}' was found. Check your spelling "\
                       "and try again. Or you could, you know, give the ID instead ;)."
            raise ClientException(message)

    def generate_station_permissions(self, *args) -> Dict[str, List[str]]:
        """
        Generates a list of station permissions for a role by using the
            :meth:``.generate_station_permission`` function on each argument.

        :param args: Tuples in the format of ``(station_name, station_id, permission_list)``.
            Any of the tuple's values can be ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import StationPermissions

            station_permissions = admin.role.generate_station_permissions(
                ("name", 1, [StationPermissions.VIEW_STATION_LOGS]),
                (None, 1, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                ("name", None, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                (None, 1, None)
            )
        """
        permissions = []

        for arg in args:
            if not isinstance(arg, tuple):
                message = "Each argument must be a tuple of values."
                raise ClientException(message)

            if len(arg) != 3:
                message = "Each tuple must have a value or None for station_name, station_id and "\
                          "permissions."
                raise ClientException(message)

            if arg[0] and not isinstance(arg[0], str):
                message = "station_name must either be a string or None."
                raise ClientException(message)

            if arg[1] and type(arg[1]) is not int:
                message = "station_id must either be an int or None."
                raise ClientException(message)

            if arg[2] and not isinstance(arg[2], list):
                message = "permissions must either be a list or None."
                raise ClientException(message)

            permissions.append(self.generate_station_permission(*arg))

        # Generates a complete station permission dictionary.
        output = {}
        for permission in permissions:
            output.update(**permission)

        return output

    def create(
        self,
        name: str,
        global_permissions: Optional[List[GlobalPermissions]] = None,
        station_permissions: Optional[Dict[str, List[StationPermissions]]] = None
    ) -> Role:
        """
        Adds a new role to the radio.

        :param name: The name of the role.
        :param global_permissions: (Optional) A list of radio-wide permissions.
            Each element in this list must be from the ``GlobalPermissions`` enum class.
            Default: ``None``.
        :param station_permissions: (Optional) A structure representing the station permissions
            for stations on the radio. This can be generated by using the
            :meth:`.generate_station_permissions` function.
            Default: ``None``.

        :returns: A :class:`Role` object for the newly created role.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions, StationPermissions

            station_permissions = admin.role.generate_station_permissions(
                ("name", 1, [StationPermissions.VIEW_STATION_LOGS]),
                (None, 1, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                ("name", None, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                (None, 1, None)
            )

            role = admin.role.create(
                name="New playlist",
                global_permissions=[
                    GlobalPermissions.VIEW_ADMINISTRATION,
                    GlobalPermissions.VIEW_SYSTEM_LOGS
                ],
                station_permissions=station_permissions
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
            for key, value in station_permissions.items():
                station_permissions[key] = [permission.value for permission in value]

        url = API_ENDPOINTS["roles"].format(
            radio_url=self._admin._request_handler.radio_url
        )

        body = {
            "name": name,
            "permissions": {
                "global": global_permissions or [],
                "station": station_perms or []
            }
        }

        response = self._admin._request_handler.post(url, body)

        # This is probably inefficient, but the permissions of the new Role won't be
        # returned otherwise. I'll find a better way soon. (No promises.)
        role_id = response['id']
        return self.__call__(role_id)

class CustomFieldHelper:
    """Provides a set of functions to interact with radio custom fields."""
    def __init__(
        self,
        _admin
    ):
        """
        Initializes a :class:`CustomFieldHelper` object for a :class:`NowPlaying` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.custom_field``.
        """
        self._admin = _admin

    def __call__(
        self,
        id: int
    ) -> CustomField:
        """
        Retrieves a specific custom field from the admin.

        :param id: The numerical ID of the playlist to be retrieved.

        :returns: A :class:`CustomField` object.

        Usage:
        .. code-block:: python

            custom_field = admin.custom_field(1)
        """
        response = _request_single_instance_of_admin_resource(
            admin=self._admin,
            resource_name="custom_field",
            resource_id=id
        )

        return CustomField(**response, _admin=self._admin)

    def create(
        self,
        name: str,
        short_name: Optional[str] = None,
        auto_assign_value: Optional[AutoAssignValues] = None
    ) -> CustomField:
        """
        Adds a new custom field to the radio.

        :param name: The name of the custom field.
        :param short_name: (Optional) The short name of the custom field.
            Leave as ``None`` to generate a default short_name value.
            Default: ``None``.
        :param auto_assign_value: (Optional) A metadata field that, if present,
            will be used to set this field's value.
            Default: ``None``.

        Usage:
        .. code-block :: python

            from AzuracastPy.enums import AutoAssignValues

            admin.custom_field.create(
                name="New Custom Field",
                auto_assign_value=AutoAssignValues.ALBUM
            )
        """
        if not short_name:
            short_name = convert_to_short_name(name)
        else:
            if not is_text_a_valid_short_name(short_name):
                message = "The short_name value is not valid. Please convert it to snake case or "\
                          "remove all spaces. Alternatively, leave the field blank to "\
                          "automatically generate an optimal short_name value."
                raise ClientException(message)

        if auto_assign_value:
            if not isinstance(auto_assign_value, AutoAssignValues):
                raise ClientException(
                    generate_enum_error_text("auto_assign_value", AutoAssignValues)
                )

            auto_assign_value = auto_assign_value.value

        url = API_ENDPOINTS["custom_fields"].format(
            radio_url=self._admin._request_handler.radio_url
        )

        body = {
            "name": name,
            "short_name": short_name,
            "auto_assign": auto_assign_value or ""
        }

        response = self._admin._request_handler.post(url, body)

        return CustomField(**response, _admin=self._admin)

class StorageLocationHelper:
    """Provides a set of functions to interact with radio storage locations."""
    def __init__(
        self,
        _admin
    ):
        """
        Initializes a :class:`StorageLocationHelper` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.storage_location``.
        """
        self._admin = _admin

    def __call__(
        self,
        id: int
    ) -> StorageLocation:
        """
        Retrieves a specific storage location from the radio.

        :param id: The numerical ID of the storage location to be retrieved.

        :returns: A :class:`StorageLocation` object.

        Usage:
        .. code-block:: python

            storage_location = admin.storage_location(1)
        """
        response = _request_single_instance_of_admin_resource(
            admin=self._admin,
            resource_name="storage_location",
            resource_id=id
        )

        return StorageLocation.from_dict(response, _admin=self)
