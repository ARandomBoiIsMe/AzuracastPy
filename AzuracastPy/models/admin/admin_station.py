from typing import List, Optional, Dict, Any

from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.util import file_upload_util, general_util
from AzuracastPy.util.general_util import generate_repr_string
from AzuracastPy.exceptions import ClientException
from AzuracastPy.constants import (
    API_ENDPOINTS,
    WEBHOOK_CONFIG_TEMPLATES,
    WEBHOOK_TRIGGERS,
    HLS_FORMATS
)

class BackendConfig:
    def __init__(
        self, charset: str, dj_port: int, telnet_port: int, record_streams: bool, record_streams_format: str,
        record_streams_bitrate: int, use_manual_autodj: bool, autodj_queue_length: int, dj_mount_point: str,
        dj_buffer: int, audio_processing_method: str, post_processing_include_live: bool, stereo_tool_license_key: str,
        master_me_preset: str, master_me_loudness_target: int, enable_replaygain_metadata: bool,
        crossfade_type: str, crossfade: int, duplicate_prevention_time_range: int, performance_mode: str,
        hls_segment_length: int, hls_segments_in_playlist: int, hls_segments_overhead: int,
        hls_enable_on_public_player: bool, hls_is_default: bool, live_broadcast_text: str
    ):
        self.charset = charset
        self.dj_port = dj_port
        self.telnet_port = telnet_port
        self.record_streams = record_streams
        self.record_streams_format = record_streams_format
        self.record_streams_bitrate = record_streams_bitrate
        self.use_manual_autodj = use_manual_autodj
        self.autodj_queue_length = autodj_queue_length
        self.dj_mount_point = dj_mount_point
        self.dj_buffer = dj_buffer
        self.audio_processing_method = audio_processing_method
        self.post_processing_include_live = post_processing_include_live
        self.stereo_tool_license_key = stereo_tool_license_key
        self.master_me_preset = master_me_preset
        self.master_me_loudness_target = master_me_loudness_target
        self.enable_replaygain_metadata = enable_replaygain_metadata
        self.crossfade_type = crossfade_type
        self.crossfade = crossfade
        self.duplicate_prevention_time_range = duplicate_prevention_time_range
        self.performance_mode = performance_mode
        self.hls_segment_length = hls_segment_length
        self.hls_segments_in_playlist = hls_segments_in_playlist
        self.hls_segments_overhead = hls_segments_overhead
        self.hls_enable_on_public_player = hls_enable_on_public_player
        self.hls_is_default = hls_is_default
        self.live_broadcast_text = live_broadcast_text

    def __repr__(self):
        return generate_repr_string(self)

class FrontendConfig:
    def __init__(
        self, custom_config: str, source_pw: str, admin_pw: str, relay_pw: str, streamer_pw: str, port: int,
        max_listeners: str, banned_ips: str, banned_user_agents: str, banned_countries: List[str], allowed_ips: str,
        sc_license_id: str, sc_user_id: str
    ):
        self.custom_config = custom_config
        self.source_pw = source_pw
        self.admin_pw = admin_pw
        self.relay_pw = relay_pw
        self.streamer_pw = streamer_pw
        self.port = port
        self.max_listeners = max_listeners
        self.banned_ips = banned_ips
        self.banned_user_agents = banned_user_agents
        self.banned_countries = banned_countries
        self.allowed_ips = allowed_ips
        self.sc_license_id = sc_license_id
        self.sc_user_id = sc_user_id

    def __repr__(self):
        return generate_repr_string(self)

class Links:
    def __init__(self_, self: str, manage: str, clone: str):
        self_.self = self
        self_.manage = manage
        self_.clone = clone

    def __repr__(self):
        return generate_repr_string(self)

class AdminStation:
    def __init__(
        self, name: str, short_name: str, is_enabled: bool, frontend_type: str, frontend_config: FrontendConfig,
        backend_type: str, backend_config: BackendConfig, description: str, url: str, genre: str, radio_base_dir: str,
        enable_requests: bool, request_delay: int, request_threshold: int, disconnect_deactivate_streamer: int,
        enable_streamers: bool, is_streamer_live: bool, enable_public_page: bool, enable_on_demand: bool,
        enable_on_demand_download: bool, enable_hls: bool, api_history_items: int, timezone: str, branding_config,
        media_storage_location: int, recordings_storage_location: int, podcasts_storage_location: int, fallback_path,
        id: int, links: Links
    ):
        self.name = name
        self.short_name = short_name
        self.is_enabled = is_enabled
        self.frontend_type = frontend_type
        self.frontend_config = frontend_config
        self.backend_type = backend_type
        self.backend_config = backend_config
        self.description = description
        self.url = url
        self.genre = genre
        self.radio_base_dir = radio_base_dir
        self.enable_requests = enable_requests
        self.request_delay = request_delay
        self.request_threshold = request_threshold
        self.disconnect_deactivate_streamer = disconnect_deactivate_streamer
        self.enable_streamers = enable_streamers
        self.is_streamer_live = is_streamer_live
        self.enable_public_page = enable_public_page
        self.enable_on_demand = enable_on_demand
        self.enable_on_demand_download = enable_on_demand_download
        self.enable_hls = enable_hls
        self.api_history_items = api_history_items
        self.timezone = timezone
        self.branding_config = branding_config
        self.media_storage_location = media_storage_location
        self.recordings_storage_location = recordings_storage_location
        self.podcasts_storage_location = podcasts_storage_location
        self.fallback_path = fallback_path
        self.id = id
        self.links = links

    def __repr__(self):
        return generate_repr_string(self)