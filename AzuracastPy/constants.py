# Dictionary of Azuracast API Endpoints
API_ENDPOINTS = {
    "all_now_playing":            "{radio_url}/api/nowplaying",
    "station_now_playing":        "{radio_url}/api/nowplaying/{station_id}",
    "station_fallback":           "{radio_url}/api/station/{station_id}/fallback",
    "stations":                   "{radio_url}/api/stations",
    "station":                    "{radio_url}/api/station/{station_id}",
    "station_stereo_tool_config": "{radio_url}/api/station/{station_id}/stereo-tool-configuration",
    "requestable_songs":          "{radio_url}/api/station/{station_id}/requests",
    "song_request":               "{radio_url}/api/station/{station_id}/request/{request_id}",
    "station_status":             "{radio_url}/api/station/{station_id}/status",
    "restart_station":            "{radio_url}/api/station/{station_id}/restart",
    "frontend_action":            "{radio_url}/api/station/{station_id}/frontend/{action}",
    "backend_action":             "{radio_url}/api/station/{station_id}/backend/{action}",
    "station_history":            "{radio_url}/api/station/{station_id}/history",
    "hls_streams":                "{radio_url}/api/station/{station_id}/hls_streams",
    "hls_stream":                 "{radio_url}/api/station/{station_id}/hls_stream/{id}",
    "station_listeners":          "{radio_url}/api/station/{station_id}/listeners",
    "station_schedule":           "{radio_url}/api/station/{station_id}/schedule",
    "song_art":                   "{radio_url}/api/station/{station_id}/art/{media_id}",
    "station_files":              "{radio_url}/api/station/{station_id}/files",
    "station_file":               "{radio_url}/api/station/{station_id}/file/{id}",
    "mount_intro_track":          "{radio_url}/api/station/{station_id}/mount/{id}/intro",
    "station_mount_points":       "{radio_url}/api/station/{station_id}/mounts",
    "station_mount_point":        "{radio_url}/api/station/{station_id}/mount/{id}",
    "station_playlists":          "{radio_url}/api/station/{station_id}/playlists",
    "station_playlist":           "{radio_url}/api/station/{station_id}/playlist/{id}",
    "podcast_episodes":           "{radio_url}/api/station/{station_id}/podcast/{podcast_id}/episodes",
    "podcast_episode":            "{radio_url}/api/station/{station_id}/podcast/{podcast_id}/episode/{id}",
    "podcast_art":                "{radio_url}/api/station/{station_id}/podcast/{podcast_id}/art",
    "podcast_episode_art":        "{radio_url}/api/station/{station_id}/podcast/{podcast_id}/episode/{episode_id}/art",
    "podcast_episode_media":      "{radio_url}/api/station/{station_id}/podcast/{podcast_id}/episode/{episode_id}/media",
    "station_podcasts":           "{radio_url}/api/station/{station_id}/podcasts",
    "station_podcast":            "{radio_url}/api/station/{station_id}/podcast/{id}",
    "station_queue":              "{radio_url}/api/station/{station_id}/queue",
    "station_queue_item":         "{radio_url}/api/station/{station_id}/queue/{id}",
    "station_remote_relays":      "{radio_url}/api/station/{station_id}/remotes",
    "station_remote_relay_item":  "{radio_url}/api/station/{station_id}/remote/{id}",
    "station_sftp_users":         "{radio_url}/api/station/{station_id}/sftp-users",
    "station_sftp_user":          "{radio_url}/api/station/{station_id}/sftp-user/{id}",
    "station_streamers":          "{radio_url}/api/station/{station_id}/streamers",
    "station_streamer":           "{radio_url}/api/station/{station_id}/streamer/{id}",
    "station_webhooks":           "{radio_url}/api/station/{station_id}/webhooks",
    "station_webhook":            "{radio_url}/api/station/{station_id}/webhook/{id}",
    "custom_fields":              "{radio_url}/api/admin/custom_fields",
    "custom_field":               "{radio_url}/api/admin/custom_field/{id}",
    "users":                      "{radio_url}/api/admin/users",
    "user":                       "{radio_url}/api/admin/user/{id}",
    "relays":                     "{radio_url}/api/internal/relays",
    "permissions":                "{radio_url}/api/admin/permissions",
    "roles":                      "{radio_url}/api/admin/roles",
    "role":                       "{radio_url}/api/admin/role/{id}",
    "settings":                   "{radio_url}/api/admin/settings",
    "admin_stations":             "{radio_url}/api/admin/stations",
    "admin_station":              "{radio_url}/api/admin/station/{id}",
    "storage_locations":          "{radio_url}/api/admin/storage_locations",
    "storage_location":           "{radio_url}/api/admin/storage_location/{id}",
    "api_status":                 "{radio_url}/api/status",
    "time":                       "{radio_url}/api/time",
    "cpu_stats":                  "{radio_url}/api/admin/server/stats"
}

# Categories for podcasts
CATEGORIES = {
    'ARTS': {
        'BOOKS': 'Arts|Books',
        'DESIGN': 'Arts|Design',
        'FASHION_BEAUTY': 'Arts|Fashion & Beauty',
        'FOOD': 'Arts|Food',
        'PERFORMING_ARTS': 'Arts|Performing Arts',
        'VISUAL_ARTS': 'Arts|Visual Arts'
    },
    'BUSINESS': {
        'CAREERS': 'Business|Careers',
        'ENTREPRENEURSHIP': 'Business|Entrepreneurship',
        'INVESTING': 'Business|Investing',
        'MANAGEMENT': 'Business|Management',
        'MARKETING': 'Business|Marketing',
        'NON_PROFIT': 'Business|Non-Profit'
    },
    'COMEDY': {
        'COMEDY_INTERVIEWS': 'Comedy|Comedy Interviews',
        'IMPROV': 'Comedy|Improv',
        'STAND_UP': 'Comedy|Stand-Up'
    },
    'EDUCATION': {
        'COURSES': 'Education|Courses',
        'HOW_TO': 'Education|How To',
        'LANGUAGE_LEARNING': 'Education|Language Learning',
        'SELF_IMPROVEMENT': 'Education|Self-Improvement'
    },
    'FICTION': {
        'COMEDY_FICTION': 'Fiction|Comedy Fiction',
        'DRAMA': 'Fiction|Drama',
        'SCIENCE_FICTION': 'Fiction|Science Fiction'
    },
    'GOVERNMENT': 'Government',
    'HISTORY': 'History',
    'HEALTH_FITNESS': {
        'ALTERNATIVE_HEALTH': 'Health & Fitness|Alternative Health',
        'FITNESS': 'Health & Fitness|Fitness',
        'MEDICINE': 'Health & Fitness|Medicine',
        'MENTAL_HEALTH': 'Health & Fitness|Mental Health',
        'NUTRITION': 'Health & Fitness|Nutrition',
        'SEXUALITY': 'Health & Fitness|Sexuality'
    },
    'KIDS_FAMILY': {
        'PARENTING': 'Kids & Family|Parenting',
        'PETS_ANIMALS': 'Kids & Family|Pets & Animals',
        'STORIES_FOR_KIDS': 'Kids & Family|Stories for Kids'
    },
    'LEISURE': {
        'ANIMATION_MANGA': 'Leisure|Animation & Manga',
        'AUTOMOTIVE': 'Leisure|Automotive',
        'AVIATION': 'Leisure|Aviation',
        'CRAFTS': 'Leisure|Crafts',
        'GAMES': 'Leisure|Games',
        'HOBBIES': 'Leisure|Hobbies',
        'HOME_GARDEN': 'Leisure|Home & Garden',
        'VIDEO_GAMES': 'Leisure|Video Games'
    },
    'MUSIC': {
        'MUSIC_COMMENTARY': 'Music|Music Commentary',
        'MUSIC_HISTORY': 'Music|Music History',
        'MUSIC_INTERVIEWS': 'Music|Music Interviews'
    },
    'NEWS': {
        'BUSINESS_NEWS': 'News|Business News',
        'DAILY_NEWS': 'News|Daily News',
        'ENTERTAINMENT_NEWS': 'News|Entertainment News',
        'NEWS_COMMENTARY': 'News|News Commentary',
        'POLITICS': 'News|Politics',
        'SPORTS_NEWS': 'News|Sports News',
        'TECH_NEWS': 'News|Tech News'
    },
    'RELIGION_SPIRITUALITY': {
        'BUDDHISM': 'Religion & Spirituality|Buddhism',
        'CHRISTIANITY': 'Religion & Spirituality|Christianity',
        'HINDUISM': 'Religion & Spirituality|Hinduism',
        'ISLAM': 'Religion & Spirituality|Islam',
        'JUDAISM': 'Religion & Spirituality|Judaism',
        'RELIGION': 'Religion & Spirituality|Religion',
        'SPIRITUALITY': 'Religion & Spirituality|Spirituality'
    },
    'SCIENCE': {
        'ASTRONOMY': 'Science|Astronomy',
        'CHEMISTRY': 'Science|Chemistry',
        'EARTH_SCIENCES': 'Science|Earth Sciences',
        'LIFE_SCIENCES': 'Science|Life Sciences',
        'MATHEMATICS': 'Science|Mathematics',
        'NATURAL_SCIENCES': 'Science|Natural Sciences',
        'NATURE': 'Science|Nature',
        'PHYSICS': 'Science|Physics',
        'SOCIAL_SCIENCES': 'Science|Social Sciences'
    },
    'SOCIETY_CULTURE': {
        'DOCUMENTARY': 'Society & Culture|Documentary',
        'PERSONAL_JOURNALS': 'Society & Culture|Personal Journals',
        'PHILOSOPHY': 'Society & Culture|Philosophy',
        'PLACES_TRAVEL': 'Society & Culture|Places & Travel',
        'RELATIONSHIPS': 'Society & Culture|Relationships'
    },
    'SPORTS': {
        'BASEBALL': 'Sports|Baseball',
        'BASKETBALL': 'Sports|Basketball',
        'CRICKET': 'Sports|Cricket',
        'FANTASY_SPORTS': 'Sports|Fantasy Sports',
        'FOOTBALL': 'Sports|Football',
        'GOLF': 'Sports|Golf',
        'HOCKEY': 'Sports|Hockey',
        'RUGBY': 'Sports|Rugby',
        'RUNNING': 'Sports|Running',
        'SOCCER': 'Sports|Soccer',
        'SWIMMING': 'Sports|Swimming',
        'TENNIS': 'Sports|Tennis',
        'VOLLEYBALL': 'Sports|Volleyball',
        'WILDERNESS': 'Sports|Wilderness',
        'WRESTLING': 'Sports|Wrestling'
    },
    'TECHNOLOGY': 'Technology',
    'TRUE_CRIME': 'True Crime',
    'TV_FILM': {
        'AFTER_SHOWS': 'TV & Film|After Shows',
        'FILM_HISTORY': 'TV & Film|Film History',
        'FILM_INTERVIEWS': 'TV & Film|Film Interviews',
        'FILM_REVIEWS': 'TV & Film|Film Reviews',
        'TV_REVIEWS': 'TV & Film|TV Reviews'
    }
}

# Days of the week
DAYS = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

# Configuration templates for webhooks
WEBHOOK_CONFIG_TEMPLATES = {
    'generic': ["webhook_url", "basic_auth_username", "basic_auth_password", "timeout"],
    'email': ["to", "subject", "message"],
    'discord': ["webhook_url", "content", "title", "description", "url", "author", "thumbnail", "footer"],
    'telegram': ["bot_token", "chat_id", "api", "text", "parse_mode"],
    'mastodon': [
        "instance_url", "access_token", "visibility", "rate_limit",
        "message", "message_song_changed_live", "message_live_connect",
        "message_live_disconnect", "message_station_offline", "message_station_online"
    ],
    'tunein': ["station_id", "partner_id", "partner_key"],
    'radiode': ["broadcastsubdomain", "apikey"],
    'getmeradio': ["token", "station_id"],
    'google_analytics_v4': ["api_secret", "measurement_id"],
    'matomo_analytics': ["matomo_url", "site_id", "token"],
}