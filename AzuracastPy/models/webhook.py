"""Class for a station webhook."""

from typing import List, Dict, Any, Optional

from ..enums import WebhookTriggers
from ..constants import WEBHOOK_CONFIG_TEMPLATES, API_ENDPOINTS
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string, generate_enum_error_text

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

class TriggerHelper:
    def __init__(
        self,
        _webhook
    ):
        self._webhook = _webhook

    def add(
        self,
        trigger: WebhookTriggers
    ):
        """
        Adds a trigger to the webhook.

        :param trigger: The trigger to be added to the webhook.
            It must be from the :class:`WebhookTriggers` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            station(1).webhook(1).trigger.add(
                trigger=WebhookTriggers.SONG_CHANGED
            )
        """
        if not isinstance(trigger, WebhookTriggers):
            raise ClientException(generate_enum_error_text('trigger', WebhookTriggers))

        trigger = trigger.value

        if any(trigger == existing_trigger for existing_trigger in self._webhook.triggers):
            message = f"The '{trigger}' trigger is already in the webhook's current trigger list."
            raise ClientException(message)

        triggers = self._webhook.triggers.copy()
        triggers.append(trigger)

        url = API_ENDPOINTS["station_webhook"].format(
            radio_url=self._webhook._station._request_handler.radio_url,
            station_id=self._webhook._station.id,
            id=self._webhook.id
        )

        body = {
            "triggers": triggers
        }

        response = self._webhook._station._request_handler.put(url, body)

        if response['success']:
            self._webhook.triggers = triggers

        return response

    def remove(
        self,
        trigger: WebhookTriggers
    ):
        """
        Removes a trigger from the webhook's current trigger list.

        :param trigger: The trigger to be removed from the webhook's trigger list.
            It must be from the :class:`WebhookTriggers` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            station(1).webhook(1).trigger.remove(
                trigger=WebhookTriggers.SONG_CHANGED
            )
        """
        if not isinstance(trigger, WebhookTriggers):
            raise ClientException(generate_enum_error_text('trigger', WebhookTriggers))

        trigger = trigger.value

        triggers = self._webhook.triggers.copy()
        try:
            triggers.remove(trigger)
        except ValueError:
            message = f"The '{trigger}' trigger is not in the webhook's current trigger list."
            raise ClientException(message)

        url = API_ENDPOINTS["station_webhook"].format(
            radio_url=self._webhook._station._request_handler.radio_url,
            station_id=self._webhook._station.id,
            id=self._webhook.id
        )

        body = {
            "triggers": triggers
        }

        response = self._webhook._station._request_handler.put(url, body)

        if response['success']:
            self._webhook.triggers = triggers

        return response

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

        self.trigger = TriggerHelper(_webhook=self)

    def __repr__(self):
        return generate_repr_string(self)

    def edit(
        self,
        name: Optional[str] = None,
        webhook_config: Optional[Dict[str, Any]] = None,
        triggers: Optional[List[WebhookTriggers]] = None
    ):
        """
        Edits the webhook's properties.

        Updates all edited attributes of the current :class:`Webhook` object.

        :param name: (Optional) The new name of the webhook. Default: ``None``.
        :param webhook_config: (Optional) The new config object for the webhook's type.
            This can be generated using the :meth:`.generate_webhook_config` function.
            Default: ``None``.
        :param triggers: (Optional) The new list of triggers for the webhook.
            Each element of the list must be from the :class:`WebhookTriggers` enum.
            Note: This will override the webhook's existing triggers.
                  Use the :meth:`.add_trigger` function if you want to add a trigger to
                  the existing triggers.
            Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            station.webhook(1).edit(
                name="New name lol",
                triggers=[WebhookTriggers.LIVE_DISCONNECT]
            )
        """
        if triggers:
            if not all(isinstance(trigger, WebhookTriggers) for trigger in triggers):
                message = "All elements of the "\
                         f"{generate_enum_error_text('triggers', WebhookTriggers)}"
                raise ClientException(message)

            triggers = [trigger.value for trigger in triggers]

        if webhook_config and not all(key in webhook_config for key in WEBHOOK_CONFIG_TEMPLATES[self.type]):
            message = "The provided 'webhook_config' is either incomplete or contains unneeded "\
                      f"keys for the '{self.type}' webhook. The '{self.type}' webhook's config "\
                      f"must only contain: {', '.join(WEBHOOK_CONFIG_TEMPLATES[self.type])}. "\
                       "Refer to the documentation for the config structure of each webhook type."
            raise ClientException(message)

        return edit_station_resource(self, "station_webhook", name, webhook_config, triggers)

    def add_trigger(
        self,
        trigger: WebhookTriggers
    ):
        """
        Adds a trigger to the webhook.

        :param trigger: The trigger to be added to the webhook.
            It must be from the :class:`WebhookTriggers` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            station.webhook(1).add_trigger(
                trigger=WebhookTriggers.SONG_CHANGED
            )
        """
        if not isinstance(trigger, WebhookTriggers):
            raise ClientException(generate_enum_error_text('trigger', WebhookTriggers))

        trigger = trigger.value

        url = API_ENDPOINTS["station_webhook"].format(
            radio_url=self._station._request_handler.radio_url,
            station_id=self._station.id,
            id=self.id
        )

        triggers = self.triggers
        triggers.append(trigger)
        body = {
            "triggers": triggers
        }

        response = self._station._request_handler.put(url, body)

        if response['success']:
            self.triggers = triggers

        return response

    def delete(self):
        """
        Deletes the webhook from the station.

        Sets all attributes of the current :class:`Webhook` object to ``None``.

        Usage:
        .. code-block:: python

            station.webhook(1).delete()
        """
        return delete_station_resource(self, "station_webhook")

    def _build_update_body(
        self,
        name,
        config,
        triggers
    ):
        return {
            "name": name or self.name,
            "triggers": triggers or self.triggers,
            "config": config or self.config
        }

    def _update_properties(
        self,
        name,
        config,
        triggers
    ):
        self.name = name or self.name
        self.triggers = triggers or self.triggers
        self.config = config or self.config

    def _clear_properties(self):
        self.name = None
        self.type = None
        self.is_enabled = None
        self.triggers = None
        self.config = None
        self.id = None
        self.links = None
        self._station = None
