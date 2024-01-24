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

# Countries for whichever class needs them lol
COUNTRIES = {
    "Afghanistan": "AF",
    "Åland Islands": "AX",
    "Albania": "AL",
    "Algeria": "DZ",
    "American Samoa": "AS",
    "Andorra": "AD",
    "Angola": "AO",
    "Anguilla": "AI",
    "Antarctica": "AQ",
    "Antigua and Barbuda": "AG",
    "Argentina": "AR",
    "Armenia": "AM",
    "Aruba": "AW",
    "Australia": "AU",
    "Austria": "AT",
    "Azerbaijan": "AZ",
    "Bahamas": "BS",
    "Bahrain": "BH",
    "Bangladesh": "BD",
    "Barbados": "BB",
    "Belarus": "BY",
    "Belgium": "BE",
    "Belize": "BZ",
    "Benin": "BJ",
    "Bermuda": "BM",
    "Bhutan": "BT",
    "Bolivia": "BO",
    "Caribbean Netherlands": "BQ",
    "Bosnia and Herzegovina": "BA",
    "Botswana": "BW",
    "Bouvet Island": "BV",
    "Brazil": "BR",
    "British Indian Ocean Territory": "IO",
    "Brunei Darussalam": "BN",
    "Bulgaria": "BG",
    "Burkina Faso": "BF",
    "Burundi": "BI",
    "Cabo Verde": "CV",
    "Cambodia": "KH",
    "Cameroon": "CM",
    "Canada": "CA",
    "Cayman Islands": "KY",
    "Central African Republic": "CF",
    "Chad": "TD",
    "Chile": "CL",
    "China": "CN",
    "Christmas Island": "CX",
    "Cocos (Keeling) Islands": "CC",
    "Colombia": "CO",
    "Comoros": "KM",
    "Republic of the Congo": "CG",
    "Democratic Republic of the Congo": "CD",
    "Cook Islands": "CK",
    "Costa Rica": "CR",
    "Ivory Coast": "CI",
    "Croatia": "HR",
    "Cuba": "CU",
    "Curaçao": "CW",
    "Cyprus": "CY",
    "Czech Republic": "CZ",
    "Denmark": "DK",
    "Djibouti": "DJ",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Ecuador": "EC",
    "Egypt": "EG",
    "El Salvador": "SV",
    "Equatorial Guinea": "GQ",
    "Eritrea": "ER",
    "Estonia": "EE",
    "Eswatini": "SZ",
    "Ethiopia": "ET",
    "Falkland Islands": "FK",
    "Faroe Islands": "FO",
    "Fiji": "FJ",
    "Finland": "FI",
    "France": "FR",
    "French Guiana": "GF",
    "French Polynesia": "PF",
    "French Southern and Antarctic Lands": "TF",
    "Gabon": "GA",
    "Gambia": "GM",
    "Georgia (country)": "GE",
    "Germany": "DE",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greece": "GR",
    "Greenland": "GL",
    "Grenada": "GD",
    "Guadeloupe": "GP",
    "Guam": "GU",
    "Guatemala": "GT",
    "Bailiwick of Guernsey": "GG",
    "Guinea": "GN",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Haiti": "HT",
    "Heard Island and McDonald Islands": "HM",
    "Vatican City": "VA",
    "Honduras": "HN",
    "Hong Kong": "HK",
    "Hungary": "HU",
    "Iceland": "IS",
    "India": "IN",
    "Indonesia": "ID",
    "Iran": "IR",
    "Iraq": "IQ",
    "Republic of Ireland": "IE",
    "Isle of Man": "IM",
    "Israel": "IL",
    "Italy": "IT",
    "Jamaica": "JM",
    "Japan": "JP",
    "Jersey": "JE",
    "Jordan": "JO",
    "Kazakhstan": "KZ",
    "Kenya": "KE",
    "Kiribati": "KI",
    "North Korea": "KP",
    "South Korea": "KR",
    "Kuwait": "KW",
    "Kyrgyzstan": "KG",
    "Laos": "LA",
    "Latvia": "LV",
    "Lebanon": "LB",
    "Lesotho": "LS",
    "Liberia": "LR",
    "Libya": "LY",
    "Liechtenstein": "LI",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Macau": "MO",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Malaysia": "MY",
    "Maldives": "MV",
    "Mali": "ML",
    "Malta": "MT",
    "Marshall Islands": "MH",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Mauritius": "MU",
    "Mayotte": "YT",
    "Mexico": "MX",
    "Federated States of Micronesia": "FM",
    "Moldova": "MD",
    "Monaco": "MC",
    "Mongolia": "MN",
    "Montenegro": "ME",
    "Montserrat": "MS",
    "Morocco": "MA",
    "Mozambique": "MZ",
    "Myanmar": "MM",
    "Namibia": "NA",
    "Nauru": "NR",
    "Nepal": "NP",
    "Kingdom of the Netherlands": "NL",
    "New Caledonia": "NC",
    "New Zealand": "NZ",
    "Nicaragua": "NI",
    "Niger": "NE",
    "Nigeria": "NG",
    "Niue": "NU",
    "Norfolk Island": "NF",
    "North Macedonia": "MK",
    "Northern Mariana Islands": "MP",
    "Norway": "NO",
    "Oman": "OM",
    "Pakistan": "PK",
    "Palau": "PW",
    "State of Palestine": "PS",
    "Panama": "PA",
    "Papua New Guinea": "PG",
    "Paraguay": "PY",
    "Peru": "PE",
    "Philippines": "PH",
    "Pitcairn Islands": "PN",
    "Poland": "PL",
    "Portugal": "PT",
    "Puerto Rico": "PR",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saint Barthélemy": "BL",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Saint Kitts and Nevis": "KN",
    "Saint Lucia": "LC",
    "Collectivity of Saint Martin": "MF",
    "Saint Pierre and Miquelon": "PM",
    "Saint Vincent and the Grenadines": "VC",
    "Samoa": "WS",
    "San Marino": "SM",
    "São Tomé and Príncipe": "ST",
    "Saudi Arabia": "SA",
    "Senegal": "SN",
    "Serbia": "RS",
    "Seychelles": "SC",
    "Sierra Leone": "SL",
    "Singapore": "SG",
    "Sint Maarten": "SX",
    "Slovakia": "SK",
    "Slovenia": "SI",
    "Solomon Islands": "SB",
    "Somalia": "SO",
    "South Africa": "ZA",
    "South Georgia and the South Sandwich Islands": "GS",
    "South Sudan": "SS",
    "Spain": "ES",
    "Sri Lanka": "LK",
    "Sudan": "SD",
    "Suriname": "SR",
    "Svalbard and Jan Mayen": "SJ",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Syria": "SY",
    "Taiwan, China": "TW",
    "Tajikistan": "TJ",
    "Tanzania": "TZ",
    "Thailand": "TH",
    "East Timor": "TL",
    "Togo": "TG",
    "Tokelau": "TK",
    "Tonga": "TO",
    "Trinidad and Tobago": "TT",
    "Tunisia": "TN",
    "Turkey": "TR",
    "Turkmenistan": "TM",
    "Turks and Caicos Islands": "TC",
    "Tuvalu": "TV",
    "Uganda": "UG",
    "Ukraine": "UA",
    "United Arab Emirates": "AE",
    "United Kingdom": "GB",
    "United States": "US",
    "United States Minor Outlying Islands": "UM",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vanuatu": "VU",
    "Venezuela": "VE",
    "Vietnam": "VN",
    "British Virgin Islands": "VG",
    "United States Virgin Islands": "VI",
    "Wallis and Futuna": "WF",
    "Western Sahara": "EH",
    "Yemen": "YE",
    "Zambia": "ZM",
    "Zimbabwe": "ZW"
}

# Languages for podcasts
LANGUAGES = {
    "abkhazian": "ab",
    "afar": "aa",
    "afrikaans": "af",
    "akan": "ak",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "aragonese": "an",
    "armenian": "hy",
    "assamese": "as",
    "avestic": "ae",
    "aymara": "ay",
    "azerbaijani": "az",
    "bambara": "bm",
    "bashkir": "ba",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bislama": "bi",
    "bosnian": "bs",
    "breton": "br",
    "bulgarian": "bg",
    "burmese": "my",
    "catalan": "ca",
    "valencian": "ca",
    "chamorro": "ch",
    "chechen": "ce",
    "chichewa": "ny",
    "chewa": "ny",
    "nyanja": "ny",
    "chinese": "zh",
    "church_slavonic": "cu",
    "old_slavonic": "cu",
    "old_church_slavonic": "cu",
    "chuvash": "cv",
    "cornish": "kw",
    "corsican": "co",
    "cree": "cr",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "divehi": "dv",
    "dhivehi": "dv",
    "maldivian": "dv",
    "dutch": "nl",
    "flemish": "nl",
    "dzongkha": "dz",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "ewe": "ee",
    "faroese": "fo",
    "fijian": "fj",
    "finnish": "fi",
    "french": "fr",
    "western_frisian": "fy",
    "fulah": "ff",
    "gaelic": "gd",
    "scottish_gaelic": "gd",
    "galician": "gl",
    "ganda": "lg",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "kalaallisut": "kl",
    "greenlandic": "kl",
    "guarani": "gn",
    "gujarati": "gu",
    "haitian": "ht",
    "haitian_creole": "ht",
    "hausa": "ha",
    "hebrew": "he",
    "herero": "hz",
    "hindi": "hi",
    "hiri_motu": "ho",
    "hungarian": "hu",
    "icelandic": "is",
    "ido": "io",
    "igbo": "ig",
    "indonesian": "id",
    "interlingua": "ia",
    "interlingue": "ie",
    "occidental": "ie",
    "inuktitut": "iu",
    "inupiaq": "ik",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jv",
    "kannada": "kn",
    "kanuri": "kr",
    "kashmiri": "ks",
    "kazakh": "kk",
    "central_khmer": "km",
    "kikuyu": "ki",
    "gikuyu": "ki",
    "kinyarwanda": "rw",
    "kirghiz": "ky",
    "kyrgyz": "ky",
    "komi": "kv",
    "kongo": "kg",
    "korean": "ko",
    "kuanyama": "kj",
    "kwanyama": "kj",
    "kurdish": "ku",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "limburgan": "li",
    "limburger": "li",
    "limburgish": "li",
    "lingala": "ln",
    "lithuanian": "lt",
    "luba-katanga": "lu",
    "luxembourgish": "lb",
    "letzeburgesch": "lb",
    "macedonian": "mk",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "manx": "gv",
    "maori": "mi",
    "marathi": "mr",
    "marshallese": "mh",
    "mongolian": "mn",
    "nauru": "na",
    "navajo": "nv",
    "navaho": "nv",
    "north_ndebele": "nd",
    "south_ndebele": "nr",
    "ndonga": "ng",
    "nepali": "ne",
    "norwegian": "no",
    "norwegian_bokmal": "nb",
    "norwegian_nynorsk": "nn",
    "sichuan_yi": "ii",
    "nuosu": "ii",
    "occitan": "oc",
    "ojibwa": "oj",
    "oriya": "or",
    "oromo": "om",
    "ossetian": "os",
    "ossetic": "os",
    "pali": "pi",
    "pashto_pushto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi_panjabi": "pa",
    "quechua": "qu",
    "romanian": "ro",
    "moldavian": "ro",
    "moldovan": "ro",
    "romansh": "rm",
    "rundi": "rn",
    "russian": "ru",
    "northern_sami": "se",
    "samoan": "sm",
    "sango": "sg",
    "sanskrit": "sa",
    "sardinian": "sc",
    "serbian": "sr",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "sinhalese": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "southern_sotho": "st",
    "spanish": "es",
    "castilian": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swati": "ss",
    "swedish": "sv",
    "tagalog": "tl",
    "tahitian": "ty",
    "tajik": "tg",
    "tamil": "ta",
    "tatar": "tt",
    "telugu": "te",
    "thai": "th",
    "tibetan": "bo",
    "tigrinya": "ti",
    "tonga": "to",
    "tsonga": "ts",
    "tswana": "tn",
    "turkish": "tr",
    "turkmen": "tk",
    "twi": "tw",
    "uighur": "ug",
    "uyghur": "ug",
    "ukrainian": "uk",
    "urdu": "ur",
    "uzbek": "uz",
    "venda": "ve",
    "vietnamese": "vi",
    "volapuk": "vo",
    "walloon": "wa",
    "welsh": "cy",
    "wolof": "wo",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zhuang": "za",
    "chuang": "za",
    "zulu": "zu"
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

# Triggers for webhooks
WEBHOOK_TRIGGERS = [
    "song_changed",
    "song_changed_live",
    "station_online",
    "station_offline",
    "live_disconnect",
    "live_connect",
    "listener_lost",
    "listener_gained"
]

# Formats
FORMATS = ['mp3', 'ogg', 'aac', 'opus', 'flac']

# Bitrates
BITRATES = [32, 48, 64, 96, 128, 192, 256, 320]

# Permissions for roles
GLOBAL_PERMISSIONS = [
    "administer all",
    "view administration",
    "view system logs",
    "administer settings",
    "administer api keys",
    "administer stations",
    "administer custom fields",
    "administer backups",
    "administer storage locations"
]

STATION_PERMISSIONS = [
    "administer all",
    "view station management",
    "view station reports",
    "view station logs",
    "manage station profile",
    "manage station broadcasting",
    "manage station streamers",
    "manage station mounts",
    "manage station remotes",
    "manage station media",
    "manage station automation",
    "manage station web hooks",
    "manage station podcasts"
]