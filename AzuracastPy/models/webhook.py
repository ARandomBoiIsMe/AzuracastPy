from typing import List, Dict, Any, Optional

from AzuracastPy.constants import API_ENDPOINTS, WEBHOOK_CONFIG_TEMPLATES, WEBHOOK_TRIGGERS
from AzuracastPy.exceptions import ClientException

class Links:
    def __init__(self_, self: str, toggle: str, test: str):
        self_.self = self
        self_.toggle = toggle
        self_.test = test

    def __repr__(self):
        return f"Links(self={self.self!r}, toggle={self.toggle!r}, test={self.test!r})"

class Webhook:
    def __init__(
            self, name: str, type: str, is_enabled: bool, triggers: List[str], config: Dict[str, Any],
            id: int, links: Links, _station
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
        return (
            f"Webhook(name={self.name!r}, type={self.type!r}, is_enabled={self.is_enabled!r}, "
            f"triggers={self.triggers!r}, config={self.config!r}, id={self.id!r}, links={self.links!r})"
        )
    
    def edit(
        self, name: Optional[str] = None, type: Optional[str] = None, config: Optional[Dict[str, Any]] = None,
        triggers: Optional[List[str]] = None
    ):
        old_webhook = self._station.webhook(self.id)

        # Attempting to update the type without updating the config to match the new type is a crime in my world.
        if type is not None and type != old_webhook.type and config is None:
            message = "To update the webhook type, the new config must be provided as well."
            raise ClientException(message)

        if type is not None:
            valid_types = WEBHOOK_CONFIG_TEMPLATES.keys()
            if type not in valid_types:
                message = f"type param must be one of {', '.join(valid_types)}"
                raise ClientException(message)
            
        if triggers is not None:
            if not all(trigger in WEBHOOK_TRIGGERS for trigger in set(triggers)):
                message = f"Invalid trigger found in triggers list. Elements in trigger list must be one of {', '.join(WEBHOOK_TRIGGERS)}."
                raise ClientException(message)
            
        if config is not None:
            if not all(key in WEBHOOK_CONFIG_TEMPLATES[type] for key in config):
                message = f"The provided 'config' is either incomplete or contains unneeded keys for the '{type}' webhook. The '{type}' webhook's config must only contain {', '.join(WEBHOOK_CONFIG_TEMPLATES[type])}. Refer to the documentation for the config structure of each webhook type."
                raise ClientException(message)

        url = API_ENDPOINTS["station_webhook"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        body = self._build_update_body(old_webhook, name, type, config, triggers)

        response = self._station._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(old_webhook, name, type, config, triggers)
            
        return response

    def delete(self):
        url = API_ENDPOINTS["station_webhook"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        response = self._station._request_handler.delete(url)

        if response['success'] is True:
            self._clear_properties()

        return response
    
    def _build_update_body(self, old_webhook: "Webhook", name, type, config, triggers):
        return {
            "name": name if name else old_webhook.name,
            "type": type if type else old_webhook.type,
            "triggers": triggers if triggers else old_webhook.triggers,
            "config": config if config else old_webhook.config
        }
    
    def _update_properties(self, old_webhook: "Webhook", name, type, config, triggers):
        self.name = None
        self.type = None
        self.triggers = None
        self.config = None
    
    def _clear_properties(self):
        self.name = None
        self.type = None
        self.is_enabled = None
        self.triggers = None
        self.config = None
        self.id = None
        self.links = None
        self._station = None