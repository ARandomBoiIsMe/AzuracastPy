from typing import List, Dict, Any

from AzuracastPy.constants import API_ENDPOINTS

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
    
    def _clear_properties(self):
        self.name = None
        self.type = None
        self.is_enabled = None
        self.triggers = None
        self.config = None
        self.id = None
        self.links = None
        self._station = None