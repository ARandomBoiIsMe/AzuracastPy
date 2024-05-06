from typing import List

from ...request_handler import RequestHandler
from ...constants import API_ENDPOINTS

from .helpers import AdminStationHelper, RoleHelper, CustomFieldHelper, StorageLocationHelper
from .admin_station import AdminStation
from .permissions import Permissions
from .role import Role
from .custom_field import CustomField
from .storage_location import StorageLocation
from .relay import Relay
from .settings import Settings

class Admin:
    """
    Represents administration functionality on a radio,
    such as managing stations and changing settings.
    """
    def __init__(
        self,
        _request_handler: RequestHandler
    ):
        """
        Initializes an :class:`Admin` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``client.admin()``.
        """
        self._request_handler = _request_handler

        self.station = AdminStationHelper(_admin=self)
        """
        An instance of :class:`.AdminStationHelper`.

        Provides the interface for working with :class:`.AdminStation` instances.

        For example, to get a station with admin priviledges on this radio, whose is ``1``:

        .. code-block:: python

            admin_station = admin.station(1)
        """

        self.role = RoleHelper(_admin=self)
        """
        An instance of :class:`.RoleHelper`.

        Provides the interface for working with :class:`.Role` instances.

        For example, to get a role with an id of ``1`` from this radio:

        .. code-block:: python

            role = admin.role(1)

        To create a role on this radio:

        .. code-block:: python

            from AzuracastPy.enums import GlobalPermissions, StationPermissions

            station_permissions = admin.role.generate_station_permissions(
                ("name", 1, [StationPermissions.VIEW_STATION_LOGS]),
                (None, 2, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                ("name", None, [StationPermissions.ADMINISTER_ALL, StationPermissions.VIEW_STATION_LOGS]),
                (None, 3, None)
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

        self.custom_field = CustomFieldHelper(_admin=self)
        """
        An instance of :class:`.CustomFieldHelper`.

        Provides the interface for working with :class:`.CustomField` instances.

        For example, to get a custom field with an id of ``1`` from this radio:

        .. code-block:: python

            custom_field = admin.custom_field(1)

        To create a custom field on this radio:

        .. code-block:: python

            from AzuracastPy.enums import AutoAssignValues

            admin.custom_field.create(
                name="New Custom Field",
                auto_assign_value=AutoAssignValues.ALBUM
            )
        """

        self.storage_location = StorageLocationHelper(_admin=self)
        """
        An instance of :class:`.StorageLocationHelper`.

        Provides the interface for working with :class:`.StorageLocation` instances.

        For example, to get a storage location with an id of ``1`` from this radio:

        .. code-block:: python

            storage_location = admin.storage_location(1)
        """

    def _request_multiple_instances_of(
        self,
        resource_name: str
    ):
        url = API_ENDPOINTS[resource_name].format(
            radio_url=self._request_handler.radio_url
        )

        return self._request_handler.get(url)

    def stations(self) -> List[AdminStation]:
        """
        Retrieves all stations on the radio.

        :returns: A list of :class:`AdminStation` objects.

        Usage:
        .. code-block:: python

            admin_stations = admin.stations()
        """
        response = self._request_multiple_instances_of("admin_stations")

        return [AdminStation(**a, _admin=self) for a in response]

    def permissions(self) -> Permissions:
        """
        Retrieves the available permissions on the radio.

        :returns: A :class:`Permissions` object.

        Usage:
        .. code-block:: python

            radio_permissions = admin.permissions()
        """
        response = self._request_multiple_instances_of("permissions")

        return Permissions.from_dict(response)

    def roles(self) -> List[Role]:
        """
        Retrieves the created roles on the radio.

        :returns: A list of :class:`Role` objects.

        Usage:
        .. code-block:: python

            radio_roles = admin.roles()
        """
        response = self._request_multiple_instances_of("roles")

        return [Role(**r, _admin=self) for r in response]

    def custom_fields(self) -> List[CustomField]:
        """
        Retrieves the created custom fields on the radio.

        :returns: A list of :class:`CustomField` objects.

        Usage:
        .. code-block:: python

            custom_fields = admin.custom_fields()
        """
        response = self._request_multiple_instances_of("custom_fields")

        return [CustomField(**cf, _admin=self) for cf in response]

    def storage_locations(self) -> List[StorageLocation]:
        """
        Retrieves the available storage loactions on the radio.

        :returns: A list of :class:`StorageLocation` objects.

        Usage:
        .. code-block:: python

            storage_locations = admin.storage_locations()
        """
        response = self._request_multiple_instances_of("storage_locations")

        return [StorageLocation.from_dict(sl, _admin=self) for sl in response]

    def relays(self) -> List[Relay]:
        """
        Retrieves the internal relays on the radio.

        :returns: A list of :class:`Relay` objects.

        Usage:
        .. code-block:: python

            relays = admin.relays()
        """
        response = self._request_multiple_instances_of("relays")

        return [Relay(**r) for r in response]

    def settings(self) -> Settings:
        """
        Retrieves the radio's settings.

        :returns: A :class:`Settings` object.

        Usage:
        .. code-block:: python

            settings = admin.settings()
        """
        response = self._request_multiple_instances_of("settings")

        return Settings(**response, _admin=self)

    def cpu_stats(self):
        """
        :returns: The statistics of the system running the radio.

        Usage:
        .. code-block:: python

            stats = admin.cpu_stats()
        """
        return self._request_multiple_instances_of("cpu_stats")
