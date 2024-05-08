"""Class for encapsulating listener count across objects."""

from ..util.general_util import generate_repr_string

class Listeners:
    """Represents the number of listeners on a station resource."""
    def __init__(
        self,
        total: int,
        unique: int,
        current: int
    ):
        """
        Initializes a :class:`Listeners` object.

        .. note::

            This class should not be initialized directly. Instead, an instance will be made
            available as an attribute of other classes: :class:`~.models.now_playing.NowPlaying`,
            :class:`~.models.mount.Mount` or :class:`~.models.remote.Remote`.
        """
        self.total = total
        self.unique = unique
        self.current = current

    def __repr__(self):
        return generate_repr_string(self)
