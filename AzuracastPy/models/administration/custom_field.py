from typing import Optional

from ...enums import AutoAssignValues
from ...exceptions import ClientException
from ...util.general_util import (
    generate_repr_string,
    convert_to_short_name,
    is_text_a_valid_short_name,
    generate_enum_error_text
)

from .util.admin_resource_operations import edit_admin_resource, delete_admin_resource

class Links:
    """Represents the links associated with a custom field."""
    def __init__(
        self_,
        self
    ):
        """
        Initializes a :class:`Links` object for a custom field.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``custom_field.links``.
        """
        self_.self = self

    def __repr__(self) -> str:
        return generate_repr_string(self)

class CustomField:
    """Represents a custom field on a radio."""
    def __init__(
        self,
        name: str,
        short_name: str,
        auto_assign: str,
        id: int,
        links: Links,
        _admin
    ):
        """
        Initializes a :class:`CustomField` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``admin.custom_field.create()``, ``admin.custom_field(id)`` or
            ``admin.custom_fields()``.
        """
        self.name = name
        self.short_name = short_name
        self.auto_assign = auto_assign
        self.id = id
        self.links = Links(**links)
        self._admin = _admin

    def __repr__(self) -> str:
        return generate_repr_string(self)

    def edit(
        self,
        name: Optional[str] = None,
        short_name: Optional[str] = None,
        auto_assign_value: Optional[AutoAssignValues] = None
    ):
        """
        Edits the custom field's properties.

        Updates all edited attributes of the current :class:`CustomField` object.

        :param name: (Optional) The new name of the custom field. Default: ``None``.
        :param short_name: (Optional) The new short name of the custom field. Default: ``None``.
        :param auto_assign_value: (Optional) The new auto assign value of the custom field.
            Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import AutoAssignValues

            custom_field.edit(
                name="New name"
                auto_assign_value=AutoAssignValues.ALBUM_ARTIST
            )
        """
        if short_name:
            if not is_text_a_valid_short_name(short_name):
                message = "The short_name value is not valid. Please convert it to snake case "\
                          "or remove all spaces. Alternatively, leave the field blank to "\
                          "automatically generate an optimal short_name value."
                raise ClientException(message)

        if auto_assign_value:
            if not isinstance(auto_assign_value, AutoAssignValues):
                raise ClientException(
                    generate_enum_error_text("auto_assign_value", AutoAssignValues)
                )

            auto_assign_value = auto_assign_value.value

        return edit_admin_resource(self, "custom_field", name, short_name, auto_assign_value)

    def delete(self):
        """
        Deletes the custom field from the radio.

        Sets all attributes of the current :class:`CustomField` object to ``None``.

        Usage:
        .. code-block:: python

            custom_field.delete()
        """
        return delete_admin_resource(self, "custom_field")

    def _build_update_body(
        self,
        name,
        short_name,
        auto_assign_value
    ):
        return {
            "name": name or self.name,
            "short_name": short_name or self.short_name,
            "auto_assign": auto_assign_value or self.auto_assign
        }

    def _update_properties(
        self,
        name,
        short_name,
        auto_assign_value
    ):
        self.name = name or self.name,
        self.short_name = short_name or self.short_name,
        self.auto_assign = auto_assign_value or self.auto_assign

    def _clear_properties(self):
        self.name = None
        self.short_name = None
        self.auto_assign = None
        self.id = None
        self.links = None
        self._admin = None
