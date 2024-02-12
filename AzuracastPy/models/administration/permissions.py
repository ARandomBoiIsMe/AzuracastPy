from typing import Dict, Any, List

from ...util.general_util import generate_repr_string

class Permissions:
    """Represents the permissions of a radio."""
    def __init__(
        self,
        global_permissions: List[str],
        station_permissions: Dict[str, List[str]]
    ):
        """
        Initializes a :class:`Permissions` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.permissions()``.
        """
        self.global_permissions = global_permissions
        self.station_permissions = station_permissions

    @classmethod
    def from_dict(
        cls,
        permissions_dict: Dict[Any, Any]
    ):
        return cls(
            global_permissions=permissions_dict.get("global"),
            station_permissions=permissions_dict.get("station")
        )

    def __repr__(self) -> str:
        return generate_repr_string(self)