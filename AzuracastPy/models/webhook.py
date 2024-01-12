from typing import List, Dict, Any, Optional

from AzuracastPy.constants import API_ENDPOINTS, WEBHOOK_CONFIG_TEMPLATES, WEBHOOK_TRIGGERS
from AzuracastPy.exceptions import ClientException
from AzuracastPy.util.general_util import generate_repr_string

class Links:
    def __init__(self_, self: str, toggle: str, test: str):
        self_.self = self
        self_.toggle = toggle
        self_.test = test

    def __repr__(self):
        return generate_repr_string(self)
    
class WebhookConfig:
    def __init__(
        self, webhook_url: Optional[str] = None, basic_auth_username: Optional[str] = None, basic_auth_password: Optional[str] = None,
        timeout: Optional[int] = None, to: Optional[str] = None, subject: Optional[str] = None, message: Optional[str] = None,
        content: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None,
        author: Optional[str] = None, thumbnail: Optional[str] = None, footer: Optional[str] = None, bot_token: Optional[str] = None,
        chat_id: Optional[str] = None, api: Optional[str] = None, text: Optional[str] = None, parse_mode: Optional[str] = None,
        instance_url: Optional[str] = None, access_token: Optional[str] = None, visibility: Optional[str] = None, rate_limit: Optional[str] = None,
        message_song_changed_live: Optional[str] = None, message_live_connect: Optional[str] = None, message_live_disconnect: Optional[str] = None,
        message_station_offline: Optional[str] = None, message_station_online: Optional[str] = None, station_id: Optional[str] = None,
        partner_id: Optional[str] = None, partner_key: Optional[str] = None, broadcastsubdomain: Optional[str] = None, apikey: Optional[str] = None,
        token: Optional[str] = None, measurement_id: Optional[str] = None, matomo_url: Optional[str] = None, site_id: Optional[str] = None
    ):        
        self.webhook_url = webhook_url
        self.basic_auth_username = basic_auth_username
        self.basic_auth_password = basic_auth_password
        self.timeout = timeout
        self.to = to
        self.subject = subject
        self.message = message
        self.content = content
        self.title = title
        self.description = description
        self.url = url
        self.author = author
        self.thumbnail = thumbnail
        self.footer = footer
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api = api
        self.text = text
        self.parse_mode = parse_mode
        self.instance_url = instance_url
        self.access_token = access_token
        self.visibility = visibility
        self.rate_limit = rate_limit
        self.message_song_changed_live = message_song_changed_live
        self.message_live_connect = message_live_connect
        self.message_live_disconnect = message_live_disconnect
        self.message_station_offline = message_station_offline
        self.message_station_online = message_station_online
        self.station_id = station_id
        self.partner_id = partner_id
        self.partner_key = partner_key
        self.broadcastsubdomain = broadcastsubdomain
        self.apikey = apikey
        self.token = token
        self.measurement_id = measurement_id
        self.matomo_url = matomo_url
        self.site_id = site_id

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}

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
        return generate_repr_string(self)
    
    def edit(
        self, name: Optional[str] = None, type: Optional[str] = None, webhook_config: Optional[WebhookConfig] = None,
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
            
        if webhook_config is not None:
            config = webhook_config.to_dict()

            if not all(key in config for key in WEBHOOK_CONFIG_TEMPLATES['email']):
                message = f"The provided 'webhook_config' is either incomplete or contains unneeded keys for the '{type}' webhook. The '{type}' webhook's config must only contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[type])}. Refer to the documentation for the config structure of each webhook type."
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
        self.name = name if name else old_webhook.name
        self.type = type if type else old_webhook.type
        self.triggers = triggers if triggers else old_webhook.triggers
        self.config = config if config else old_webhook.config
    
    def _clear_properties(self):
        self.name = None
        self.type = None
        self.is_enabled = None
        self.triggers = None
        self.config = None
        self.id = None
        self.links = None
        self._station = None