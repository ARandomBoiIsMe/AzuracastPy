from typing import List

from ...util.general_util import generate_repr_string

from ..mount import Mount

class Relay:
    """Represents a relay item of a radio."""
    def __init__(
        self,
        id: int,
        name: str,
        shortcode: str,
        description: str,
        url: str,
        genre: str,
        type: str,
        port: int,
        relay_pw: str,
        admin_pw: str,
        mounts: List[Mount]
    ):
        """
        Initializes a :class:`Relay` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.Admin.relays`.
        """
        self.id = id
        self.name = name
        self.shortcode = shortcode
        self.description = description
        self.url = url
        self.genre = genre
        self.type = type
        self.port = port
        self.relay_pw = relay_pw
        self.admin_pw = admin_pw
        self.mounts = [Mount(**m) for m in mounts] if mounts else []

    def __repr__(self) -> str:
        return generate_repr_string(self)
