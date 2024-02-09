from ...util.general_util import generate_repr_string, generate_enum_error_text
from ...exceptions import ClientException
from ...constants import API_ENDPOINTS
from ...enums import (
    RadioAvatarServices,
    AnalyticsTypes,
    IPAddressSources,
    HistoryKeepDays,
    PublicThemes
)

from typing import Optional, List, Union

class UpdateResults:
    def __init__(
        self,
        current_release,
        latest_release,
        needs_rolling_update,
        rolling_updates_available,
        rolling_updates_list,
        needs_release_update,
        can_switch_to_stable
    ):
        self.current_release = current_release
        self.latest_release = latest_release
        self.needs_rolling_update = needs_rolling_update
        self.rolling_updates_available = rolling_updates_available
        self.rolling_updates_list = rolling_updates_list
        self.needs_release_update = needs_release_update
        self.can_switch_to_stable = can_switch_to_stable

    def __repr__(self) -> str:
        return generate_repr_string(self)

class Settings:
    def __init__(
        self,
        app_unique_identifier,
        base_url,
        instance_name,
        prefer_browser_url,
        use_radio_proxy,
        history_keep_days,
        always_use_ssl,
        api_access_control,
        enable_static_nowplaying,
        analytics,
        check_for_updates,
        update_results,
        update_last_run,
        public_theme,
        hide_album_art,
        homepage_redirect_url,
        default_album_art_url,
        use_external_album_art_when_processing_media,
        use_external_album_art_in_apis,
        last_fm_api_key,
        hide_product_name,
        public_custom_css,
        public_custom_js,
        internal_custom_css,
        backup_enabled,
        backup_time_code,
        backup_exclude_media,
        backup_keep_copies,
        backup_storage_location,
        backup_format,
        backup_last_run,
        backup_last_output,
        setup_complete_time,
        sync_disabled,
        sync_last_run,
        external_ip,
        geolite_license_key,
        geolite_last_run,
        enable_advanced_features,
        mail_enabled,
        mail_sender_name,
        mail_sender_email,
        mail_smtp_host,
        mail_smtp_port,
        mail_smtp_username,
        mail_smtp_password,
        mail_smtp_secure,
        avatar_service,
        avatar_default_url,
        acme_email,
        acme_domains,
        ip_source,
        _admin
    ):
        self.app_unique_identifier = app_unique_identifier
        self.base_url = base_url
        self.instance_name = instance_name
        self.prefer_browser_url = prefer_browser_url
        self.use_radio_proxy = use_radio_proxy
        self.history_keep_days = history_keep_days
        self.always_use_ssl = always_use_ssl
        self.api_access_control = api_access_control
        self.enable_static_nowplaying = enable_static_nowplaying
        self.analytics = analytics
        self.check_for_updates = check_for_updates
        self.update_results = update_results
        self.update_last_run = update_last_run
        self.public_theme = public_theme
        self.hide_album_art = hide_album_art
        self.homepage_redirect_url = homepage_redirect_url
        self.default_album_art_url = default_album_art_url
        self.use_external_album_art_when_processing_media = use_external_album_art_when_processing_media
        self.use_external_album_art_in_apis = use_external_album_art_in_apis
        self.last_fm_api_key = last_fm_api_key
        self.hide_product_name = hide_product_name
        self.public_custom_css = public_custom_css
        self.public_custom_js = public_custom_js
        self.internal_custom_css = internal_custom_css
        self.backup_enabled = backup_enabled
        self.backup_time_code = backup_time_code
        self.backup_exclude_media = backup_exclude_media
        self.backup_keep_copies = backup_keep_copies
        self.backup_storage_location = backup_storage_location
        self.backup_format = backup_format
        self.backup_last_run = backup_last_run
        self.backup_last_output = backup_last_output
        self.setup_complete_time = setup_complete_time
        self.sync_disabled = sync_disabled
        self.sync_last_run = sync_last_run
        self.external_ip = external_ip
        self.geolite_license_key = geolite_license_key
        self.geolite_last_run = geolite_last_run
        self.enable_advanced_features = enable_advanced_features
        self.mail_enabled = mail_enabled
        self.mail_sender_name = mail_sender_name
        self.mail_sender_email = mail_sender_email
        self.mail_smtp_host = mail_smtp_host
        self.mail_smtp_port = mail_smtp_port
        self.mail_smtp_username = mail_smtp_username
        self.mail_smtp_password = mail_smtp_password
        self.mail_smtp_secure = mail_smtp_secure
        self.avatar_service = avatar_service
        self.avatar_default_url = avatar_default_url
        self.acme_email = acme_email
        self.acme_domains = acme_domains
        self.ip_source = ip_source
        self._admin = _admin

    def __repr__(self) -> str:
        return generate_repr_string(self)

    def edit(
        self,
        base_url: Optional[str] = None,
        instance_name: Optional[str] = None,
        prefer_browser_url: Optional[bool] = None,
        use_radio_proxy: Optional[bool] = None,
        use_high_performance_now_playing_updates: Optional[bool] = None,
        history_keep_days: Optional[HistoryKeepDays] = None,
        listener_analytics: Optional[AnalyticsTypes] = None,
        always_use_https: Optional[bool] = None,
        ip_address_source: Optional[IPAddressSources] = None,
        api_access_control: Optional[Union[str, List[str]]] = None,
        show_update_announcements: Optional[bool] = None,
        acme_email: Optional[str] = None,
        acme_domains: Optional[List[str]] = None,
        enable_mail_delivery: Optional[bool] = None,
        mail_sender_name: Optional[str] = None,
        mail_sender_email: Optional[str] = None,
        mail_smtp_host: Optional[str] = None,
        mail_smtp_port: Optional[str] = None,
        mail_smtp_username: Optional[str] = None,
        mail_smtp_password: Optional[str] = None,
        mail_smtp_secure: Optional[bool] = None,
        avatar_service: Optional[RadioAvatarServices] = None,
        avatar_default_url: Optional[str] = None,
        check_web_services_for_album_art_for_now_playing_tracks: Optional[bool] = None,
        check_web_services_for_album_art_when_uploading_media: Optional[bool] = None,
        last_fm_api_key: Optional[str] = None,
        public_theme: Optional[PublicThemes] = None,
        hide_album_art_on_public_pages: Optional[bool] = None,
        hide_azuracast_branding_on_public_pages: Optional[bool] = None,
        homepage_redirect_url: Optional[str] = None,
        default_album_art_url: Optional[str] = None,
        public_custom_css: Optional[str] = None,
        public_custom_js: Optional[str] = None,
        internal_custom_css: Optional[str] = None,
        enable_advanced_features: Optional[bool] = None
    ):
        """
        Edits the radio's settings.

        Updates all edited attributes of the current :class:`Settings` object.

        :param base_url: (Optional) The base URL where this service is located.
            Use either the external IP address or fully-qualified domain name (if one exists)
            pointing to this server.
            Default: ``None``.
        :param instance_name: (Optional) This name will appear as a sub-header next to the
            AzuraCast logo, to help identify this server.
            Default: ``None``.
        :param prefer_browser_url: (Optional) If this is set to ``True``, the browser
            URL will be used instead of the base URL when it's available.
            Default: ``None``
        :param use_radio_proxy: (Optional) Determines whether all radio will be routed through
            the web ports.
            Default: ``None``.
        :param use_high_performance_now_playing_updates: (Optional) Uses either Websockets,
            Server-Sent Events (SSE) or static JSON files to serve Now Playing data on public
            pages. This improves performance, especially with large listener volume.
            Disable this if you are encountering problems with the service or use multiple
            URLs to serve your public pages.
            Default: ``None``.
        :param history_keep_days: (Optional) Set longer to preserve more playback history and
            listener metadata for stations. Set shorter to save disk space.
            Default: ``None``.
        :param listener_analytics: (Optional) Full analytics are used to show station reports
            across the system. Limited analytics are used to view live listener tracking and
            may be required for royalty reports.
            Default: ``None``.
        :param always_use_https: (Optional) Set to ``True`` to always use "https://" secure URLs,
            and to automatically redirect to the secure URL when an insecure URL is visited.
            Default: ``None``.
        :param ip_address_source: (Optional) Customize this setting to ensure you get the correct
            IP address for remote users. Only change this setting if you use a reverse proxy,
            either within Docker or a third-party service like CloudFlare.
            Default: ``None``.
        :param api_access_control: (Optional) Set to ``"*"`` to allow all sources,
            or specify a list of origins.
            Default: ``None``.
        :param show_update_announcements: (Optional) Show new releases within your update channel
            on the AzuraCast homepage.
            Default: ``None``.
        :param acme_email: (Optional) E-mail address to receive updates about your certificate.
            Default: ``None``.
        :param acme_domains: (Optional) All listed domain names should point to
            this AzuraCast installation.
            Default: ``None``.
        :param enable_mail_delivery: (Optional) Used for "Forgot Password" functionality,
            web hooks and other functions.
            Default: ``None``.
        :param mail_sender_name: (Optional) The name of the mail sender. Default: ``None``.
        :param mail_sender_email: (Optional) The email of the mail sender. Default: ``None``.
        :param mail_smtp_host: (Optional) The SMTP host. Default: ``None``
        :param mail_smtp_port: (Optional) The SMTP port. Default: ``None``
        :param mail_smtp_username: (Optional) The SMTP username. Default: ``None``
        :param mail_smtp_password: (Optional) The SMTP password. Default: ``None``
        :param mail_smtp_secure: (Optional) Determines whether secure SMTP connection will be used.
            Usually enabled for port 465, disabled for ports 587 or 25.
            Default: ``None``.
        :param avatar_service: (Optional) Default: ``None``
        :param avatar_default_url: (Optional) Default: ``None``
        :param check_web_services_for_album_art_for_now_playing_tracks: (Optional) Default: ``None``
        :param check_web_services_for_album_art_when_uploading_media: (Optional) Default: ``None``
        :param last_fm_api_key: (Optional) This service can provide album art for tracks where
            none is available locally.
            Default: ``None``.
        :param public_theme: (Optional) The theme to be used as a base for station public pages
            and the login page.
            Default: ``None``.
        :param hide_album_art_on_public_pages: (Optional) Determines whether album will be hidden
            on public pages.
            Default: ``None``.
        :param hide_azuracast_branding_on_public_pages: (Optional) Determines whether the
            AzuraCast branding will be removed from public-facing pages.
            Default: ``None``.
        :param homepage_redirect_url: (Optional) If a visitor is not signed in and visits the
            AzuraCast homepage, you can automatically redirect them to the URL specified here.
            Leave blank to redirect them to the login screen by default.
            Default: ``None``.
        :param default_album_art_url: (Optional) If a song has no album art, this URL will be
            listed instead. Leave blank to use the standard placeholder art.
            Default: ``None``.
        :param public_custom_css: (Optional) This CSS will be applied to the station public
            pages and login page.
            Default: ``None``.
        :param public_custom_js: (Optional) This javascript code will be applied to the station
            public pages and login page.
            Default: ``None``.
        :param internal_custom_css: (Optional) This CSS will be applied to
            the main management pages.
            Default: ``None``.
        :param enable_advanced_features: (Optional) Determines whether advanced features in the
            web interface will be enabled.
            Default: ``None``.

        Usage:
        .. code-block:: python

            from AzuracastPy.enums import AnalyticsTypes, PublicThemes

            settings.edit(
                instance_name="newnamehehe",
                always_use_https=True,
                listener_analytics=AnalyticsTypes.LIMITED,
                public_theme=PublicThemes.SYSTEM_DEFAULT
            )
        """
        if avatar_service:
            if not isinstance(avatar_service, RadioAvatarServices):
                raise ClientException(
                    generate_enum_error_text('avatar_service', RadioAvatarServices)
                )

            avatar_service = avatar_service.value

        if listener_analytics:
            if not isinstance(listener_analytics, AnalyticsTypes):
                raise ClientException(
                    generate_enum_error_text('listener_analytics', AnalyticsTypes)
                )

            listener_analytics = listener_analytics.value

        if ip_address_source:
            if not isinstance(ip_address_source, IPAddressSources):
                raise ClientException(
                    generate_enum_error_text('ip_address_source', IPAddressSources)
                )

            ip_address_source = ip_address_source.value

        if history_keep_days:
            if not isinstance(history_keep_days, HistoryKeepDays):
                raise ClientException(
                    generate_enum_error_text('history_keep_days', HistoryKeepDays)
                )

            history_keep_days = history_keep_days.value

        if public_theme:
            if not isinstance(public_theme, PublicThemes):
                raise ClientException(generate_enum_error_text('public_theme', PublicThemes))

            public_theme = public_theme.value

        url = API_ENDPOINTS["settings"].format(
            radio_url=self._admin._request_handler.radio_url
        )

        body = self._build_update_body(
            base_url,
            instance_name,
            prefer_browser_url,
            use_radio_proxy,
            use_high_performance_now_playing_updates,
            history_keep_days,
            listener_analytics,
            always_use_https,
            ip_address_source,
            api_access_control,
            show_update_announcements,
            acme_email,
            acme_domains,
            enable_mail_delivery,
            mail_sender_name,
            mail_sender_email,
            mail_smtp_host,
            mail_smtp_port,
            mail_smtp_username,
            mail_smtp_password,
            mail_smtp_secure,
            avatar_service,
            avatar_default_url,
            check_web_services_for_album_art_for_now_playing_tracks,
            check_web_services_for_album_art_when_uploading_media,
            last_fm_api_key,
            public_theme,
            hide_album_art_on_public_pages,
            hide_azuracast_branding_on_public_pages,
            homepage_redirect_url,
            default_album_art_url,
            public_custom_css,
            public_custom_js,
            internal_custom_css,
            enable_advanced_features
        )

        response = self._admin._request_handler.put(url, body)

        if response['success'] is True:
            self._update_properties(
                base_url,
                instance_name,
                prefer_browser_url,
                use_radio_proxy,
                use_high_performance_now_playing_updates,
                history_keep_days,
                listener_analytics,
                always_use_https,
                ip_address_source,
                api_access_control,
                show_update_announcements,
                acme_email,
                acme_domains,
                enable_mail_delivery,
                mail_sender_name,
                mail_sender_email,
                mail_smtp_host,
                mail_smtp_port,
                mail_smtp_username,
                mail_smtp_password,
                mail_smtp_secure,
                avatar_service,
                avatar_default_url,
                check_web_services_for_album_art_for_now_playing_tracks,
                check_web_services_for_album_art_when_uploading_media,
                last_fm_api_key,
                public_theme,
                hide_album_art_on_public_pages,
                hide_azuracast_branding_on_public_pages,
                homepage_redirect_url,
                default_album_art_url,
                public_custom_css,
                public_custom_js,
                internal_custom_css,
                enable_advanced_features
            )

        return response

    def _build_update_body(
        self,
        base_url,
        instance_name,
        prefer_browser_url,
        use_radio_proxy,
        use_high_performance_now_playing_updates,
        history_keep_days,
        listener_analytics,
        always_use_https,
        ip_address_source,
        api_access_control,
        show_update_announcements,
        acme_email,
        acme_domains,
        enable_mail_delivery,
        mail_sender_name,
        mail_sender_email,
        mail_smtp_host,
        mail_smtp_port,
        mail_smtp_username,
        mail_smtp_password,
        mail_smtp_secure,
        avatar_service,
        avatar_default_url,
        check_web_services_for_album_art_for_now_playing_tracks,
        check_web_services_for_album_art_when_uploading_media,
        last_fm_api_key,
        public_theme,
        hide_album_art_on_public_pages,
        hide_azuracast_branding_on_public_pages,
        homepage_redirect_url,
        default_album_art_url,
        public_custom_css,
        public_custom_js,
        internal_custom_css,
        enable_advanced_features
    ):
        body = {
            "base_url": base_url or self.base_url,
            "instance_name": instance_name or self.instance_name,
            "prefer_browser_url": prefer_browser_url if prefer_browser_url is not None else self.prefer_browser_url,
            "use_radio_proxy": use_radio_proxy if use_radio_proxy is not None else self.use_radio_proxy,
            "history_keep_days": history_keep_days or self.history_keep_days,
            "always_use_ssl": always_use_https if always_use_https is not None else self.always_use_ssl,
            "api_access_control": api_access_control if api_access_control  else self.api_access_control,
            "enable_static_nowplaying": use_high_performance_now_playing_updates if use_high_performance_now_playing_updates else self.enable_static_nowplaying,
            "analytics": listener_analytics or self.analytics,
            "check_for_updates": show_update_announcements if show_update_announcements else self.check_for_updates,
            "public_theme": public_theme if public_theme else self.public_theme,
            "hide_album_art": hide_album_art_on_public_pages if hide_album_art_on_public_pages else self.hide_album_art,
            "homepage_redirect_url": homepage_redirect_url or self.homepage_redirect_url,
            "default_album_art_url": default_album_art_url or self.default_album_art_url,
            "use_external_album_art_when_processing_media": check_web_services_for_album_art_when_uploading_media if check_web_services_for_album_art_when_uploading_media is not None else self.use_external_album_art_when_processing_media,
            "use_external_album_art_in_apis": check_web_services_for_album_art_for_now_playing_tracks if check_web_services_for_album_art_for_now_playing_tracks is not None else self.use_external_album_art_in_apis,
            "last_fm_api_key": last_fm_api_key or self.last_fm_api_key,
            "hide_product_name": hide_azuracast_branding_on_public_pages if hide_azuracast_branding_on_public_pages else self.hide_product_name,
            "public_custom_css": public_custom_css or self.public_custom_css,
            "public_custom_js": public_custom_js or self.public_custom_js,
            "internal_custom_css": internal_custom_css or self.internal_custom_css,
            "avatar_service": avatar_service or self.avatar_service,
            "avatar_default_url": avatar_default_url or self.avatar_default_url,
            "acme_email": acme_email or self.acme_email,
            "acme_domains": ', '.join(acme_domains) if acme_domains else ', '.join(self.acme_domains),
            "ip_source": ip_address_source or self.ip_source,
            "mail_enabled": enable_mail_delivery if enable_mail_delivery is not None else self.mail_enabled,
            "enable_advanced_features": enable_advanced_features if enable_advanced_features is not None else self.enable_advanced_features
        }

        if enable_mail_delivery is not None and enable_mail_delivery is True:
            body["mail_sender_name"] = mail_sender_name or self.mail_sender_name
            body["mail_sender_email"] = mail_sender_email or self.mail_sender_email
            body["mail_smtp_host"] = mail_smtp_host or self.mail_smtp_host
            body["mail_smtp_port"] = mail_smtp_port or self.mail_smtp_port
            body["mail_smtp_username"] = mail_smtp_username or self.mail_smtp_username
            body["mail_smtp_password"] = mail_smtp_password or self.mail_smtp_password
            body["mail_smtp_secure"] = mail_smtp_secure if mail_smtp_secure is not None else self.mail_smtp_secure

        return body

    def _update_properties(
        self,
        base_url,
        instance_name,
        prefer_browser_url,
        use_radio_proxy,
        use_high_performance_now_playing_updates,
        history_keep_days,
        listener_analytics,
        always_use_https,
        ip_address_source,
        api_access_control,
        show_update_announcements,
        acme_email,
        acme_domains,
        enable_mail_delivery,
        mail_sender_name,
        mail_sender_email,
        mail_smtp_host,
        mail_smtp_port,
        mail_smtp_username,
        mail_smtp_password,
        mail_smtp_secure,
        avatar_service,
        avatar_default_url,
        check_web_services_for_album_art_for_now_playing_tracks,
        check_web_services_for_album_art_when_uploading_media,
        last_fm_api_key,
        public_theme,
        hide_album_art_on_public_pages,
        hide_azuracast_branding_on_public_pages,
        homepage_redirect_url,
        default_album_art_url,
        public_custom_css,
        public_custom_js,
        internal_custom_css,
        enable_advanced_features
    ):
        self.base_url = base_url or self.base_url
        self.instance_name = instance_name or self.instance_name
        self.prefer_browser_url = prefer_browser_url if prefer_browser_url else self.prefer_browser_url
        self.use_radio_proxy = use_radio_proxy if use_radio_proxy else self.use_radio_proxy
        self.history_keep_days = history_keep_days or self.history_keep_days
        self.always_use_ssl = always_use_https if always_use_https else self.always_use_ssl
        self.api_access_control = api_access_control if api_access_control  else self.api_access_control
        self.enable_static_nowplaying = use_high_performance_now_playing_updates if use_high_performance_now_playing_updates else self.enable_static_nowplaying
        self.analytics = listener_analytics or self.analytics
        self.check_for_updates = show_update_announcements if show_update_announcements else self.check_for_updates
        self.public_theme = public_theme if public_theme else self.public_theme
        self.hide_album_art = hide_album_art_on_public_pages if hide_album_art_on_public_pages else self.hide_album_art
        self.homepage_redirect_url = homepage_redirect_url or self.homepage_redirect_url
        self.default_album_art_url = default_album_art_url or self.default_album_art_url
        self.use_external_album_art_when_processing_media = check_web_services_for_album_art_when_uploading_media if check_web_services_for_album_art_when_uploading_media else self.use_external_album_art_when_processing_media
        self.use_external_album_art_in_apis = check_web_services_for_album_art_for_now_playing_tracks if check_web_services_for_album_art_for_now_playing_tracks else self.use_external_album_art_in_apis
        self.last_fm_api_key = last_fm_api_key or self.last_fm_api_key
        self.hide_product_name = hide_azuracast_branding_on_public_pages if hide_azuracast_branding_on_public_pages else self.hide_product_name
        self.public_custom_css = public_custom_css or self.public_custom_css
        self.public_custom_js = public_custom_js or self.public_custom_js
        self.internal_custom_css = internal_custom_css or self.internal_custom_css
        self.avatar_service = avatar_service or self.avatar_service
        self.avatar_default_url = avatar_default_url or self.avatar_default_url
        self.acme_email = acme_email or self.acme_email
        self.acme_domains = acme_domains if acme_domains else self.acme_domains
        self.ip_source = ip_address_source or self.ip_source
        self.mail_enabled = enable_mail_delivery if enable_mail_delivery else self.mail_enabled
        self.enable_advanced_features = enable_advanced_features if enable_advanced_features else self.enable_advanced_features

        if enable_mail_delivery is not None and enable_mail_delivery is True:
            self.mail_sender_name = mail_sender_name or self.mail_sender_name
            self.mail_sender_email = mail_sender_email or self.mail_sender_email
            self.mail_smtp_host = mail_smtp_host or self.mail_smtp_host
            self.mail_smtp_port = mail_smtp_port or self.mail_smtp_port
            self.mail_smtp_username = mail_smtp_username or self.mail_smtp_username
            self.mail_smtp_password = mail_smtp_password or self.mail_smtp_password
            self.mail_smtp_secure = mail_smtp_secure if mail_smtp_secure is not None else self.mail_smtp_secure
