from typing import List

class Webhook:
    def __init__(self, id: int, name: str, type: str, is_enabled: bool, triggers: List[str], config: List[str], metadata: List[str]):
        self.id = id
        self.name = name
        self.type = type
        self.is_enabled = is_enabled
        self.triggers = triggers
        self.config = config
        self.metadata = metadata

    def __repr__(self):
        return (
            f"Webhook(id={self.id!r}, name={self.name!r}, type={self.type!r}, "
            f"is_enabled={self.is_enabled!r}, triggers={self.triggers!r}, "
            f"config={self.config!r}, metadata={self.metadata!r})"
        )