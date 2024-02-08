"""Enum classes to be utilized when using the library."""

from enum import Enum

class ServiceActions(Enum):
    RESTART = "restart"
    STOP = "stop"
    START = "start"

class GlobalPermissions(Enum):
    ADMINISTER_ALL = "administer all"
    VIEW_ADMINISTRATION = "view administration"
    VIEW_SYSTEM_LOGS = "view system logs"
    ADMINISTER_SETTINGS = "administer settings"
    ADMINISTER_API_KEYS = "administer api keys"
    ADMINISTER_STATIONS = "administer stations"
    ADMINISTER_CUSTOM_FIELDS = "administer custom fields"
    ADMINISTER_BACKUPS = "administer backups"
    ADMINISTER_STORAGE_LOCATIONS = "administer storage locations"

class StationPermissions(Enum):
    ADMINISTER_ALL = "administer all"
    VIEW_STATION_MANAGEMENT = "view station management"
    VIEW_STATION_REPORTS = "view station reports"
    VIEW_STATION_LOGS = "view station logs"
    MANAGE_STATION_PROFILE = "manage station profile"
    MANAGE_STATION_BROADCASTING = "manage station broadcasting"
    MANAGE_STATION_STREAMERS = "manage station streamers"
    MANAGE_STATION_MOUNTS = "manage station mounts"
    MANAGE_STATION_REMOTES = "manage station remotes"
    MANAGE_STATION_MEDIA = "manage station media"
    MANAGE_STATION_AUTOMATION = "manage station automation"
    MANAGE_STATION_WEBHOOKS = "manage station web hooks"
    MANAGE_STATION_PODCASTS = "manage station podcasts"

class PlaylistTypes(Enum):
    DEFAULT = "default"
    ONCE_PER_X_SONGS = "once_per_x_songs"
    ONCE_PER_X_MINUTES = "once_per_x_minutes"
    ONCE_PER_HOUR = "once_per_hour"
    CUSTOM = "custom"

class PlaylistOrders(Enum):
    RANDOM = "random"
    SHUFFLE = "shuffle"
    SEQUENTIAL = "sequential"

class PlaylistSources(Enum):
    SONGS = "songs"
    REMOTE_URL = "remote_url"

class PlaylistRemoteTypes(Enum):
    STREAM = "stream"
    PLAYLIST = "playlist"
    OTHER = "other"

class RadioAvatarServices(Enum):
    LIBRAVATAR = "libravatar"
    GRAVATAR = "gravatar"
    DISABLED = "disabled"

class WebhookTriggers(Enum):
    SONG_CHANGED = "song_changed"
    SONG_CHANGED_LIVE = "song_changed_live"
    STATION_ONLINE = "station_online"
    STATION_OFFLINE = "station_offline"
    LIVE_DISCONNECT = "live_disconnect"
    LIVE_CONNECT = "live_connect"
    LISTENER_LOST = "listener_lost"
    LISTENER_GAINED = "listener_gained"

class WebhookConfigTypes(Enum):
    GENERIC = "generic"
    EMAIL = "email"
    DISCORD = "discord"
    TELEGRAM = "telegram"
    MASTODON = "mastodon"
    TUNEIN = "tunein"
    RADIODE = "radiode"
    GETMERADIO = "getmeradio"
    GOOGLE_ANALYTICS_V4 = "google_analytics_v4"
    MATOMO_ANALYTICS = "matomo_analytics"

class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Formats(Enum):
    MP3 = 'mp3'
    OGG = 'ogg'
    AAC = 'aac'
    OPUS = 'opus'
    FLAC = 'flac'

class Bitrates(Enum):
    BITRATE_32 = 32
    BITRATE_48 = 48
    BITRATE_64 = 64
    BITRATE_96 = 96
    BITRATE_128 = 128
    BITRATE_192 = 192
    BITRATE_256 = 256
    BITRATE_320 = 320

class AnalyticsTypes(Enum):
    FULL = "all"
    LIMITED = "no_ip"
    NONE = "none"

class PublicThemes(Enum):
    DARK = "dark"
    LIGHT = "light"
    SYSTEM_DEFAULT = "browser"

class IPAddressSources(Enum):
    LOCAL = "local"
    CLOUDFARE = "cloudfare"
    REVERSE = "xff"

class BackendTypes(Enum):
    LIQUIDSOAP = "liquidsoap"

class FrontendTypes(Enum):
    ICECAST = "icecast"

class RemoteTypes(Enum):
    ICECAST = "icecast"
    SHOUTCAST1 = "shoutcast1"
    SHOUTCAST2 = "shoutcast2"

class AutoAssignValues(Enum):
    ALBUM = 'album'
    ALBUM_ARTIST = 'album_artist'
    ALBUM_ARTIST_SORT_ORDER = 'album_artist_sort_order'
    ALBUM_SORT_ORDER = 'album_sort_order'
    ARTIST = 'artist'
    BAND = 'band'
    BPM = 'bpm'
    COMMENT = 'comment'
    COMMERCIAL_INFORMATION = 'commercial_information'
    COMPOSER = 'composer'
    COMPOSER_SORT_ORDER = 'composer_sort_order'
    CONDUCTOR = 'conductor'
    CONTENT_GROUP_DESCRIPTION = 'content_group_description'
    COPYRIGHT = 'copyright'
    COPYRIGHT_MESSAGE = 'copyright_message'
    ENCODED_BY = 'encoded_by'
    ENCODER_SETTINGS = 'encoder_settings'
    ENCODING_TIME = 'encoding_time'
    FILE_OWNER = 'file_owner'
    FILE_TYPE = 'file_type'
    GENRE = 'genre'
    INITIAL_KEY = 'initial_key'
    INTERNET_RADIO_STATION_NAME = 'internet_radio_station_name'
    INTERNET_RADIO_STATION_OWNER = 'internet_radio_station_owner'
    INVOLVED_PEOPLE_LIST = 'involved_people_list'
    LINKED_INFORMATION = 'linked_information'
    ISRC = 'isrc'
    LANGUAGE = 'language'
    LENGTH = 'length'
    LYRICIST = 'lyricist'
    MEDIA_TYPE = 'media_type'
    MOOD = 'mood'
    MUSIC_CD_IDENTIFIER = 'music_cd_identifier'
    MUSICIAN_CREDITS_LIST = 'musician_credits_list'
    ORIGINAL_ALBUM = 'original_album'
    ORIGINAL_ARTIST = 'original_artist'
    ORIGINAL_FILENAME = 'original_filename'
    ORIGINAL_LYRICIST = 'original_lyricist'
    ORIGINAL_RELEASE_TIME = 'original_release_time'
    ORIGINAL_YEAR = 'original_year'
    PART_OF_A_COMPILATION = 'part_of_a_compilation'
    PART_OF_A_SET = 'part_of_a_set'
    PERFORMER_SORT_ORDER = 'performer_sort_order'
    PLAYLIST_DELAY = 'playlist_delay'
    PRODUCED_NOTICE = 'produced_notice'
    PUBLISHER = 'publisher'
    RECORDING_TIME = 'recording_time'
    RELEASE_TIME = 'release_time'
    REMIXER = 'remixer'
    SET_SUBTITLE = 'set_subtitle'
    SUBTITLE = 'subtitle'
    TAGGING_TIME = 'tagging_time'
    TERMS_OF_USE = 'terms_of_use'
    TITLE = 'title'
    TITLE_SORT_ORDER = 'title_sort_order'
    TRACK_NUMBER = 'track_number'
    UNSYNCHRONISED_LYRICS = 'unsynchronised_lyrics'
    URL_ARTIST = 'url_artist'
    URL_FILE = 'url_file'
    URL_PAYMENT = 'url_payment'
    URL_PUBLISHER = 'url_publisher'
    URL_SOURCE = 'url_source'
    URL_STATION = 'url_station'
    URL_USER = 'url_user'
    YEAR = 'year'

class HistoryKeepDays(Enum):
    ZERO_DAYS = 0
    FOURTEEN_DAYS = 14
    THIRTY_DAYS = 30
    SIXTY_DAYS = 60
    ONE_YEAR = 365
    TWO_YEARS = 730

class Languages(Enum):
    ABKHAZIAN = "ab"
    AFAR = "aa"
    AFRIKAANS = "af"
    AKAN = "ak"
    ALBANIAN = "sq"
    AMHARIC = "am"
    ARABIC = "ar"
    ARAGONESE = "an"
    ARMENIAN = "hy"
    ASSAMESE = "as"
    AVESTIC = "ae"
    AYMARA = "ay"
    AZERBAIJANI = "az"
    BAMBARA = "bm"
    BASHKIR = "ba"
    BASQUE = "eu"
    BELARUSIAN = "be"
    BENGALI = "bn"
    BISLAMA = "bi"
    BOSNIAN = "bs"
    BRETON = "br"
    BULGARIAN = "bg"
    BURMESE = "my"
    CATALAN = "ca"
    VALENCIAN = "ca"
    CHAMORRO = "ch"
    CHECHEN = "ce"
    CHICHEWA = "ny"
    CHEWA = "ny"
    NYANJA = "ny"
    CHINESE = "zh"
    CHURCH_SLAVONIC = "cu"
    OLD_SLAVONIC = "cu"
    OLD_CHURCH_SLAVONIC = "cu"
    CHUVASH = "cv"
    CORNISH = "kw"
    CORSICAN = "co"
    CREE = "cr"
    CROATIAN = "hr"
    CZECH = "cs"
    DANISH = "da"
    DIVEHI = "dv"
    DHIVEHI = "dv"
    MALDIVIAN = "dv"
    DUTCH = "nl"
    FLEMISH = "nl"
    DZONGKHA = "dz"
    ENGLISH = "en"
    ESPERANTO = "eo"
    ESTONIAN = "et"
    EWE = "ee"
    FAROESE = "fo"
    FIJIAN = "fj"
    FINNISH = "fi"
    FRENCH = "fr"
    WESTERN_FRISIAN = "fy"
    FULAH = "ff"
    GAELIC = "gd"
    SCOTTISH_GAELIC = "gd"
    GALICIAN = "gl"
    GANDA = "lg"
    GEORGIAN = "ka"
    GERMAN = "de"
    GREEK = "el"
    KALAALLISUT = "kl"
    GREENLANDIC = "kl"
    GUARANI = "gn"
    GUJARATI = "gu"
    HAITIAN = "ht"
    HAITIAN_CREOLE = "ht"
    HAUSA = "ha"
    HEBREW = "he"
    HERERO = "hz"
    HINDI = "hi"
    HIRI_MOTU = "ho"
    HUNGARIAN = "hu"
    ICELANDIC = "is"
    IDO = "io"
    IGBO = "ig"
    INDONESIAN = "id"
    INTERLINGUA = "ia"
    INTERLINGUE = "ie"
    OCCIDENTAL = "ie"
    INUKTITUT = "iu"
    INUPIAQ = "ik"
    IRISH = "ga"
    ITALIAN = "it"
    JAPANESE = "ja"
    JAVANESE = "jv"
    KANNADA = "kn"
    KANURI = "kr"
    KASHMIRI = "ks"
    KAZAKH = "kk"
    CENTRAL_KHMER = "km"
    KIKUYU = "ki"
    GIKUYU = "ki"
    KINYARWANDA = "rw"
    KIRGHIZ = "ky"
    KYRGYZ = "ky"
    KOMI = "kv"
    KONGO = "kg"
    KOREAN = "ko"
    KUANYAMA = "kj"
    KWANYAMA = "kj"
    KURDISH = "ku"
    LAO = "lo"
    LATIN = "la"
    LATVIAN = "lv"
    LIMBURGAN = "li"
    LIMBURGER = "li"
    LIMBURGISH = "li"
    LINGALA = "ln"
    LITHUANIAN = "lt"
    LUBA_KATANGA = "lu"
    LUXEMBOURGISH = "lb"
    LETZEBURGESCH = "lb"
    MACEDONIAN = "mk"
    MALAGASY = "mg"
    MALAY = "ms"
    MALAYALAM = "ml"
    MALTESE = "mt"
    MANX = "gv"
    MAORI = "mi"
    MARATHI = "mr"
    MARSHALLESE = "mh"
    MONGOLIAN = "mn"
    NAURU = "na"
    NAVAJO = "nv"
    NAVAHO = "nv"
    NORTH_NDEBELE = "nd"
    SOUTH_NDEBELE = "nr"
    NDONGA = "ng"
    NEPALI = "ne"
    NORWEGIAN = "no"
    NORWEGIAN_BOKMAL = "nb"
    NORWEGIAN_NYNORSK = "nn"
    SICHUAN_YI = "ii"
    NUOSU = "ii"
    OCCITAN = "oc"
    OJIBWA = "oj"
    ORIYA = "or"
    OROMO = "om"
    OSSETIAN = "os"
    OSSETIC = "os"
    PALI = "pi"
    PASHTO_PUSHTO = "ps"
    PERSIAN = "fa"
    POLISH = "pl"
    PORTUGUESE = "pt"
    PUNJABI_PANJABI = "pa"
    QUECHUA = "qu"
    ROMANIAN = "ro"
    MOLDAVIAN = "ro"
    MOLDOVAN = "ro"
    ROMANSH = "rm"
    RUNDI = "rn"
    RUSSIAN = "ru"
    NORTHERN_SAMI = "se"
    SAMOAN = "sm"
    SANGO = "sg"
    SANSKRIT = "sa"
    SARDINIAN = "sc"
    SERBIAN = "sr"
    SHONA = "sn"
    SINDHI = "sd"
    SINHALA = "si"
    SINHALESE = "si"
    SLOVAK = "sk"
    SLOVENIAN = "sl"
    SOMALI = "so"
    SOUTHERN_SOTHO = "st"
    SPANISH = "es"
    CASTILIAN = "es"
    SUNDANESE = "su"
    SWAHILI = "sw"
    SWATI = "ss"
    SWEDISH = "sv"
    TAGALOG = "tl"
    TAHITIAN = "ty"
    TAJIK = "tg"
    TAMIL = "ta"
    TATAR = "tt"
    TELUGU = "te"
    THAI = "th"
    TIBETAN = "bo"
    TIGRINYA = "ti"
    TONGA = "to"
    TSONGA = "ts"
    TSWANA = "tn"
    TURKISH = "tr"
    TURKMEN = "tk"
    TWI = "tw"
    UIGHUR = "ug"
    UYGHUR = "ug"
    UKRAINIAN = "uk"
    URDU = "ur"
    UZBEK = "uz"
    VENDA = "ve"
    VIETNAMESE = "vi"
    VOLAPUK = "vo"
    WALLOON = "wa"
    WELSH = "cy"
    WOLOF = "wo"
    XHOSA = "xh"
    YIDDISH = "yi"
    YORUBA = "yo"
    ZHUANG = "za"
    CHUANG = "za"
    ZULU = "zu"

class Countries(Enum):
    AFGHANISTAN = "AF"
    ALAND_ISLANDS = "AX"
    ALBANIA = "AL"
    ALGERIA = "DZ"
    AMERICAN_SAMOA = "AS"
    ANDORRA = "AD"
    ANGOLA = "AO"
    ANGUILLA = "AI"
    ANTARCTICA = "AQ"
    ANTIGUA_AND_BARBUDA = "AG"
    ARGENTINA = "AR"
    ARMENIA = "AM"
    ARUBA = "AW"
    AUSTRALIA = "AU"
    AUSTRIA = "AT"
    AZERBAIJAN = "AZ"
    BAHAMAS = "BS"
    BAHRAIN = "BH"
    BANGLADESH = "BD"
    BARBADOS = "BB"
    BELARUS = "BY"
    BELGIUM = "BE"
    BELIZE = "BZ"
    BENIN = "BJ"
    BERMUDA = "BM"
    BHUTAN = "BT"
    BOLIVIA = "BO"
    CARIBBEAN_NETHERLANDS = "BQ"
    BOSNIA_AND_HERZEGOVINA = "BA"
    BOTSWANA = "BW"
    BOUVET_ISLAND = "BV"
    BRAZIL = "BR"
    BRITISH_INDIAN_OCEAN_TERRITORY = "IO"
    BRUNEI_DARUSSALAM = "BN"
    BULGARIA = "BG"
    BURKINA_FASO = "BF"
    BURUNDI = "BI"
    CABO_VERDE = "CV"
    CAMBODIA = "KH"
    CAMEROON = "CM"
    CANADA = "CA"
    CAYMAN_ISLANDS = "KY"
    CENTRAL_AFRICAN_REPUBLIC = "CF"
    CHAD = "TD"
    CHILE = "CL"
    CHINA = "CN"
    CHRISTMAS_ISLAND = "CX"
    COCOS_KEELING_ISLANDS = "CC"
    COLOMBIA = "CO"
    COMOROS = "KM"
    CONGO = "CG"
    DEMOCRATIC_REPUBLIC_OF_THE_CONGO = "CD"
    COOK_ISLANDS = "CK"
    COSTA_RICA = "CR"
    IVORY_COAST = "CI"
    CROATIA = "HR"
    CUBA = "CU"
    CURACAO = "CW"
    CYPRUS = "CY"
    CZECH_REPUBLIC = "CZ"
    DENMARK = "DK"
    DJIBOUTI = "DJ"
    DOMINICA = "DM"
    DOMINICAN_REPUBLIC = "DO"
    ECUADOR = "EC"
    EGYPT = "EG"
    EL_SALVADOR = "SV"
    EQUATORIAL_GUINEA = "GQ"
    ERITREA = "ER"
    ESTONIA = "EE"
    ESWATINI = "SZ"
    ETHIOPIA = "ET"
    FALKLAND_ISLANDS = "FK"
    FAROE_ISLANDS = "FO"
    FIJI = "FJ"
    FINLAND = "FI"
    FRANCE = "FR"
    FRENCH_GUIANA = "GF"
    FRENCH_POLYNESIA = "PF"
    FRENCH_SOUTHERN_AND_ANTARCTIC_LANDS = "TF"
    GABON = "GA"
    GAMBIA = "GM"
    GEORGIA = "GE"
    GERMANY = "DE"
    GHANA = "GH"
    GIBRALTAR = "GI"
    GREECE = "GR"
    GREENLAND = "GL"
    GRENADA = "GD"
    GUADELOUPE = "GP"
    GUAM = "GU"
    GUATEMALA = "GT"
    BAILIWICK_OF_GUERNSEY = "GG"
    GUINEA = "GN"
    GUINEA_BISSAU = "GW"
    GUYANA = "GY"
    HAITI = "HT"
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = "HM"
    VATICAN_CITY = "VA"
    HONDURAS = "HN"
    HONG_KONG = "HK"
    HUNGARY = "HU"
    ICELAND = "IS"
    INDIA = "IN"
    INDONESIA = "ID"
    IRAN = "IR"
    IRAQ = "IQ"
    REPUBLIC_OF_IRELAND = "IE"
    ISLE_OF_MAN = "IM"
    ISRAEL = "IL"
    ITALY = "IT"
    JAMAICA = "JM"
    JAPAN = "JP"
    JERSEY = "JE"
    JORDAN = "JO"
    KAZAKHSTAN = "KZ"
    KENYA = "KE"
    KIRIBATI = "KI"
    NORTH_KOREA = "KP"
    SOUTH_KOREA = "KR"
    KUWAIT = "KW"
    KYRGYZSTAN = "KG"
    LAOS = "LA"
    LATVIA = "LV"
    LEBANON = "LB"
    LESOTHO = "LS"
    LIBERIA = "LR"
    LIBYA = "LY"
    LIECHTENSTEIN = "LI"
    LITHUANIA = "LT"
    LUXEMBOURG = "LU"
    MACAU = "MO"
    MADAGASCAR = "MG"
    MALAWI = "MW"
    MALAYSIA = "MY"
    MALDIVES = "MV"
    MALI = "ML"
    MALTA = "MT"
    MARSHALL_ISLANDS = "MH"
    MARTINIQUE = "MQ"
    MAURITANIA = "MR"
    MAURITIUS = "MU"
    MAYOTTE = "YT"
    MEXICO = "MX"
    MICRONESIA = "FM"
    MOLDOVA = "MD"
    MONACO = "MC"
    MONGOLIA = "MN"
    MONTENEGRO = "ME"
    MONTSERRAT = "MS"
    MOROCCO = "MA"
    MOZAMBIQUE = "MZ"
    MYANMAR = "MM"
    NAMIBIA = "NA"
    NAURU = "NR"
    NEPAL = "NP"
    KINGDOM_OF_THE_NETHERLANDS = "NL"
    NEW_CALEDONIA = "NC"
    NEW_ZEALAND = "NZ"
    NICARAGUA = "NI"
    NIGER = "NE"
    NIGERIA = "NG"
    NIUE = "NU"
    NORFOLK_ISLAND = "NF"
    NORTH_MACEDONIA = "MK"
    NORTHERN_MARIANA_ISLANDS = "MP"
    NORWAY = "NO"
    OMAN = "OM"
    PAKISTAN = "PK"
    PALAU = "PW"
    STATE_OF_PALESTINE = "PS"
    PANAMA = "PA"
    PAPUA_NEW_GUINEA = "PG"
    PARAGUAY = "PY"
    PERU = "PE"
    PHILIPPINES = "PH"
    PITCAIRN_ISLANDS = "PN"
    POLAND = "PL"
    PORTUGAL = "PT"
    PUERTO_RICO = "PR"
    QATAR = "QA"
    REUNION = "RE"
    ROMANIA = "RO"
    RUSSIA = "RU"
    RWANDA = "RW"
    SAINT_BARTHELEMY = "BL"
    SAINT_HELENA = "SH"
    SAINT_KITTS_AND_NEVIS = "KN"
    SAINT_LUCIA = "LC"
    COLLECTIVITY_OF_SAINT_MARTIN = "MF"
    SAINT_PIERRE_AND_MIQUELON = "PM"
    SAINT_VINCENT_AND_THE_GRENADINES = "VC"
    SAMOA = "WS"
    SAN_MARINO = "SM"
    SAO_TOME_AND_PRINCIPE = "ST"
    SAUDI_ARABIA = "SA"
    SENEGAL = "SN"
    SERBIA = "RS"
    SEYCHELLES = "SC"
    SIERRA_LEONE = "SL"
    SINGAPORE = "SG"
    SINT_MAARTEN = "SX"
    SLOVAKIA = "SK"
    SLOVENIA = "SI"
    SOLOMON_ISLANDS = "SB"
    SOMALIA = "SO"
    SOUTH_AFRICA = "ZA"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "GS"
    SOUTH_SUDAN = "SS"
    SPAIN = "ES"
    SRI_LANKA = "LK"
    SUDAN = "SD"
    SURINAME = "SR"
    SVALBARD_AND_JAN_MAYEN = "SJ"
    SWEDEN = "SE"
    SWITZERLAND = "CH"
    SYRIA = "SY"
    TAIWAN_CHINA = "TW"
    TAJIKISTAN = "TJ"
    TANZANIA = "TZ"
    THAILAND = "TH"
    EAST_TIMOR = "TL"
    TOGO = "TG"
    TOKELAU = "TK"
    TONGA = "TO"
    TRINIDAD_AND_TOBAGO = "TT"
    TUNISIA = "TN"
    TURKEY = "TR"
    TURKMENISTAN = "TM"
    TURKS_AND_CAICOS_ISLANDS = "TC"
    TUVALU = "TV"
    UGANDA = "UG"
    UKRAINE = "UA"
    UNITED_ARAB_EMIRATES = "AE"
    UNITED_KINGDOM = "GB"
    UNITED_STATES = "US"
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = "UM"
    URUGUAY = "UY"
    UZBEKISTAN = "UZ"
    VANUATU = "VU"
    VENEZUELA = "VE"
    VIETNAM = "VN"
    BRITISH_VIRGIN_ISLANDS = "VG"
    UNITED_STATES_VIRGIN_ISLANDS = "VI"
    WALLIS_AND_FUTUNA = "WF"
    WESTERN_SAHARA = "EH"
    YEMEN = "YE"
    ZAMBIA = "ZM"
    ZIMBABWE = "ZW"

# I know these aren't enums, leave me alone.
class _Arts:
    BOOKS = 'Arts|Books'
    DESIGN = 'Arts|Design'
    FASHION_BEAUTY = 'Arts|Fashion & Beauty'
    FOOD = 'Arts|Food'
    PERFORMING_ARTS = 'Arts|Performing Arts'
    VISUAL_ARTS = 'Arts|Visual Arts'

class _Business:
    CAREERS = 'Business|Careers'
    ENTREPRENEURSHIP = 'Business|Entrepreneurship'
    INVESTING = 'Business|Investing'
    MANAGEMENT = 'Business|Management'
    MARKETING = 'Business|Marketing'
    NON_PROFIT = 'Business|Non-Profit'

class _Comedy:
    COMEDY_INTERVIEWS = 'Comedy|Comedy Interviews'
    IMPROV = 'Comedy|Improv'
    STAND_UP = 'Comedy|Stand-Up'

class _Education:
    COURSES = 'Education|Courses'
    HOW_TO = 'Education|How To'
    LANGUAGE_LEARNING = 'Education|Language Learning'
    SELF_IMPROVEMENT = 'Education|Self-Improvement'

class _Fiction:
    COMEDY_FICTION = 'Fiction|Comedy Fiction'
    DRAMA = 'Fiction|Drama'
    SCIENCE_FICTION = 'Fiction|Science Fiction'

class _HealthFitness:
    ALTERNATIVE_HEALTH = 'Health & Fitness|Alternative Health'
    FITNESS = 'Health & Fitness|Fitness'
    MEDICINE = 'Health & Fitness|Medicine'
    MENTAL_HEALTH = 'Health & Fitness|Mental Health'
    NUTRITION = 'Health & Fitness|Nutrition'
    SEXUALITY = 'Health & Fitness|Sexuality'

class _KidsFamily:
    PARENTING = 'Kids & Family|Parenting'
    PETS_ANIMALS = 'Kids & Family|Pets & Animals'
    STORIES_FOR_KIDS = 'Kids & Family|Stories for Kids'

class _Leisure:
    ANIMATION_MANGA = 'Leisure|Animation & Manga'
    AUTOMOTIVE = 'Leisure|Automotive'
    AVIATION = 'Leisure|Aviation'
    CRAFTS = 'Leisure|Crafts'
    GAMES = 'Leisure|Games'
    HOBBIES = 'Leisure|Hobbies'
    HOME_GARDEN = 'Leisure|Home & Garden'
    VIDEO_GAMES = 'Leisure|Video Games'

class _Music:
    MUSIC_COMMENTARY = 'Music|Music Commentary'
    MUSIC_HISTORY = 'Music|Music History'
    MUSIC_INTERVIEWS = 'Music|Music Interviews'

class _News:
    BUSINESS_NEWS = 'News|Business News'
    DAILY_NEWS = 'News|Daily News'
    ENTERTAINMENT_NEWS = 'News|Entertainment News'
    NEWS_COMMENTARY = 'News|News Commentary'
    POLITICS = 'News|Politics'
    SPORTS_NEWS = 'News|Sports News'
    TECH_NEWS = 'News|Tech News'

class _ReligionSpirituality:
    BUDDHISM = 'Religion & Spirituality|Buddhism'
    CHRISTIANITY = 'Religion & Spirituality|Christianity'
    HINDUISM = 'Religion & Spirituality|Hinduism'
    ISLAM = 'Religion & Spirituality|Islam'
    JUDAISM = 'Religion & Spirituality|Judaism'
    RELIGION = 'Religion & Spirituality|Religion'
    SPIRITUALITY = 'Religion & Spirituality|Spirituality'

class _Science:
    ASTRONOMY = 'Science|Astronomy'
    CHEMISTRY = 'Science|Chemistry'
    EARTH_SCIENCES = 'Science|Earth Sciences'
    LIFE_SCIENCES = 'Science|Life Sciences'
    MATHEMATICS = 'Science|Mathematics'
    NATURAL_SCIENCES = 'Science|Natural Sciences'
    NATURE = 'Science|Nature'
    PHYSICS = 'Science|Physics'
    SOCIAL_SCIENCES = 'Science|Social Sciences'

class _SocietyCulture:
    DOCUMENTARY = 'Society & Culture|Documentary'
    PERSONAL_JOURNALS = 'Society & Culture|Personal Journals'
    PHILOSOPHY = 'Society & Culture|Philosophy'
    PLACES_TRAVEL = 'Society & Culture|Places & Travel'
    RELATIONSHIPS = 'Society & Culture|Relationships'

class _Sports:
    BASEBALL = 'Sports|Baseball'
    BASKETBALL = 'Sports|Basketball'
    CRICKET = 'Sports|Cricket'
    FANTASY_SPORTS = 'Sports|Fantasy Sports'
    FOOTBALL = 'Sports|Football'
    GOLF = 'Sports|Golf'
    HOCKEY = 'Sports|Hockey'
    RUGBY = 'Sports|Rugby'
    RUNNING = 'Sports|Running'
    SOCCER = 'Sports|Soccer'
    SWIMMING = 'Sports|Swimming'
    TENNIS = 'Sports|Tennis'
    VOLLEYBALL = 'Sports|Volleyball'
    WILDERNESS = 'Sports|Wilderness'
    WRESTLING = 'Sports|Wrestling'

class _TVFilm:
    AFTER_SHOWS = 'TV & Film|After Shows'
    FILM_HISTORY = 'TV & Film|Film History'
    FILM_INTERVIEWS = 'TV & Film|Film Interviews'
    FILM_REVIEWS = 'TV & Film|Film Reviews'
    TV_REVIEWS = 'TV & Film|TV Reviews'

class PodcastCategories:
    Arts = _Arts
    Business = _Business
    Comedy = _Comedy
    Education = _Education
    Fiction = _Fiction
    GOVERNMENT = 'Government'
    HISTORY = 'History'
    HealthFitness = _HealthFitness
    KidsFamily = _KidsFamily
    Leisure = _Leisure
    Music = _Music
    News = _News
    ReligionSpirituality = _ReligionSpirituality
    Science = _Science
    SocietyCulture = _SocietyCulture
    Sports = _Sports
    TECHNOLOGY = 'Technology'
    TRUE_CRIME = 'True Crime'
    TVFilm = _TVFilm
