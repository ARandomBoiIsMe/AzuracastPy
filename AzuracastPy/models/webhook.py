"""Class for a station webhook."""

from typing import List, Dict, Any, Optional, Union

from ..enums import WebhookTriggers
from ..constants import WEBHOOK_CONFIG_TEMPLATES, API_ENDPOINTS
from ..exceptions import ClientException
from ..util.general_util import generate_repr_string, generate_enum_error_text

from .util.station_resource_operations import edit_station_resource, delete_station_resource

class Links:
    """Represents the links associated with a webhook."""
    def __init__(
        self_,
        self: str,
        toggle: str,
        test: str
    ):
        """
        Initializes a :class:`Links` instance for a webhook.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``webhook.links``.
        """
        self_.self = self
        self_.toggle = toggle
        self_.test = test

    def __repr__(self):
        return generate_repr_string(self)

class TriggerHelper:
    """Provides functions for working with the triggers of a webhook."""
    def __init__(
        self,
        _webhook
    ):
        """
        Initializes a :class:`TriggerHelper` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``webhook.trigger``.
        """
        self._webhook = _webhook

    def add(
        self,
        *args: WebhookTriggers
    ):
        """
        Adds one or more triggers to the webhook.

        :param args: The trigger(s) to be added to the webhook.
            All arguments must be from the :class:`WebhookTriggers` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            webhook.trigger.add(WebhookTriggers.SONG_CHANGED)

            webhook.trigger.add(
                WebhookTriggers.SONG_CHANGED,
                WebhookTriggers.LIVE_CONNECT
            )
        """
        triggers = self._webhook.triggers.copy()

        for arg in args:
            if not isinstance(arg, WebhookTriggers):
                message = "Each argument must be an attribute from the "\
                         f"'WebhookTriggers' class."
                raise ClientException(message)

            arg = arg.value

            if arg in triggers:
                message = f"'{arg}' is already in the webhook's triggers."
                raise ClientException(message)

            triggers.append(arg)

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
        *args: WebhookTriggers
    ):
        """
        Removes one or more triggers from the webhook.

        :param args: The trigger(s) to be removed from the webhook.
            All arguments must be from the :class:`WebhookTriggers` enum.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            webhook.trigger.remove(WebhookTriggers.SONG_CHANGED)

            webhook.trigger.remove(
                WebhookTriggers.SONG_CHANGED,
                WebhookTriggers.LIVE_CONNECT
            )
        """
        triggers = self._webhook.triggers.copy()

        for arg in args:
            if not isinstance(arg, WebhookTriggers):
                message = "Each argument must be an attribute from the "\
                         f"'WebhookTriggers' class."
                raise ClientException(message)

            arg = arg.value

            if arg not in self._webhook.triggers:
                message = f"'{arg}' is not in the webhook's triggers."
                raise ClientException(message)

            triggers.remove(arg)

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
    """Represents a webhook on a station."""
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
        """
        Initializes a :class:`Webhook` instance.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.webhook.create()``, ``station.webhooks()`` or ``station.webhook(id)``.
        """
        self.name = name
        self.type = type
        self.is_enabled = is_enabled
        self.triggers = triggers
        self.config = config
        self.id = id
        self.links = Links(**links)
        self._station = _station

        self.trigger = TriggerHelper(_webhook=self)
        """
        An instance of :class:`.TriggerHelper`.

        Provides the interface for working with this webhook's triggers.

        For example, to add one or more triggers to the webhook:

        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            webhook.trigger.add(WebhookTriggers.SONG_CHANGED)

            webhook.trigger.add(
                WebhookTriggers.SONG_CHANGED,
                WebhookTriggers.LIVE_CONNECT
            )

        To remove one or more triggers from the webhook:

        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            webhook.trigger.remove(WebhookTriggers.SONG_CHANGED)

            webhook.trigger.remove(
                WebhookTriggers.SONG_CHANGED,
                WebhookTriggers.LIVE_CONNECT
            )
        """

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
            Note: This will overwrite the webhook's existing triggers.
                  Use the :meth:`.trigger.add` and :meth:`.trigger.remove` methods to
                  interact with the webhook's existing triggers.
            Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import WebhookTriggers

            webhook.edit(
                name="New name lol",
                triggers=[
                    WebhookTriggers.LIVE_DISCONNECT
                ]
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

    def delete(self):
        """
        Deletes the webhook from the station.

        Sets all attributes of the current :class:`Webhook` object to ``None``.

        Usage:
        .. code-block:: python

            webhook.delete()
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
