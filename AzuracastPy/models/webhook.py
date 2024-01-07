from typing import List, Dict, Any

class Links:
    def __init__(self_, self, toggle, test):
        self_.self = self
        self_.toggle = toggle
        self_.test = test

    def __repr__(self):
        return f"Links(self={self.self!r}, toggle={self.toggle!r}, test={self.test!r})"

class Webhook:
    def __init__(
            self, name: str, type: str, is_enabled: bool, triggers: List[str], config: Dict[str, Any],
            id: int, links: Links
        ):
        self.name = name
        self.type = type
        self.is_enabled = is_enabled
        self.triggers = triggers
        self.config = config
        self.id = id
        self.links = links

    def __repr__(self):
        return (
            f"Webhook(name={self.name!r}, type={self.type!r}, is_enabled={self.is_enabled!r}, "
            f"triggers={self.triggers!r}, config={self.config!r}, id={self.id!r}, links={self.links!r})"
        )