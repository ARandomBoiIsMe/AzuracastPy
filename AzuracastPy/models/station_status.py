"""Class for encapsulating data about the status of a station."""

from ..util.general_util import generate_repr_string

class StationStatus:
    """Represents the status data of a station."""
    def __init__(
        self,
        backend_running,
        frontend_running,
        station_has_started,
        station_needs_restart
    ):
        """
        Initializes a :class:`StationStatus` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``station.status()``.
        """
        self.backend_running = backend_running
        self.frontend_running = frontend_running
        self.station_has_started = station_has_started
        self.station_needs_restart = station_needs_restart

    def __repr__(self):
        return generate_repr_string(self)
