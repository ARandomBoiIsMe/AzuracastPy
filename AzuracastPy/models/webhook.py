from typing import List, Dict, Any, Optional

from AzuracastPy.constants import WEBHOOK_CONFIG_TEMPLATES, WEBHOOK_TRIGGERS
from AzuracastPy.exceptions import ClientException
from AzuracastPy.util.general_util import generate_repr_string

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    def __init__(
        self_, 
        self: str, 
        toggle: str, 
        test: str
    ):
        self_.self = self
        self_.toggle = toggle
        self_.test = test

    def __repr__(self):
        return generate_repr_string(self)

class Webhook:
    def __init__(
        self, 
        name: str, 
        type: str, 
        is_enabled: bool, 
        triggers: List[str], 
        config: Dict[str, Any],
        id: int, 
        links: Links, 
        _station
    ):
        self.name = name
        self.type = type
        self.is_enabled = is_enabled
        self.triggers = triggers
        self.config = config
        self.id = id
        self.links = links
        self._station = _station

    def __repr__(self):
        return generate_repr_string(self)
    
    def edit(
        self, 
        name: Optional[str] = None,
        webhook_config: Optional[Dict[str, Any]] = None,
        triggers: Optional[List[str]] = None
    ):
        """
        Edits the webhook's properties.

        :param name:
        :param webhook_config:
        :param triggers:
        """
        if triggers is not None:
            if not all(trigger in WEBHOOK_TRIGGERS for trigger in triggers):
                message = f"Invalid trigger found in triggers list. Elements in trigger list must be one of: {', '.join(WEBHOOK_TRIGGERS)}."
                raise ClientException(message)
            
        if webhook_config is not None:
            if not all(key in webhook_config for key in WEBHOOK_CONFIG_TEMPLATES[self.type]):
                message = f"The provided 'webhook_config' is either incomplete or contains unneeded keys for the '{self.type}' webhook. The '{self.type}' webhook's config must only contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[self.type])}. Refer to the documentation for the config structure of each webhook type."
                raise ClientException(message)

        return edit_station_resource(self, "station_webhook", name, webhook_config, triggers)
    
    def delete(self):
        """
        Deletes the webhook from the station.
        """
        return delete_station_resource(self, "station_webhook")
    
    def _build_update_body(
        self, 
        name, 
        config, 
        triggers
    ):
        return {
            "name": name if name else self.name,
            "triggers": triggers if triggers else self.triggers,
            "config": config if config else self.config
        }
    
    def _update_properties(
        self, 
        name, 
        config, 
        triggers
    ):
        self.name = name if name else self.name
        self.triggers = triggers if triggers else self.triggers
        self.config = config if config else self.config
    
    def _clear_properties(self):
        self.name = None
        self.type = None
        self.is_enabled = None
        self.triggers = None
        self.config = None
        self.id = None
        self.links = None
        self._station = None