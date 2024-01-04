class StationStatus:
    def __init__(self, backend_running, frontend_running, station_has_started, station_needs_restart):
        self.backend_running = backend_running
        self.frontend_running = frontend_running
        self.station_has_started = station_has_started
        self.station_needs_restart = station_needs_restart

    def __repr__(self):
        return (
            f"StationStatus(backend_running={self.backend_running}, frontend_running={self.frontend_running}, "
            f"station_has_started={self.station_has_started}, station_needs_restart={self.station_needs_restart})"
        )