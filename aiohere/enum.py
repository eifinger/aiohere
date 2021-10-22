"""Enums for here."""

from enum import Enum


class WeatherProductType(Enum):
    """Identifies the type of report to obtain."""

    OBSERVATION = "observation"
    FORECAST_7DAYS = "forecast_7days"
    FORECAST_7DAYS_SIMPLE = "forecast_7days_simple"
    FORECAST_HOURLY = "forecast_hourly"
    FORECAST_ASTRONOMY = "forecast_astronomy"
    ALERTS = "alerts"
    NWS_ALERTS = "nws_alerts"

    def __str__(self):
        return "%s" % self.value


class Language(Enum):
    """Available languages."""

    AFRIKAANS = "af-ZA"
    ALBANIAN = "sq"
    AMHARIC = "am-ET"
    ARABIC = "ar"
    ASSAMESE = "as-IN"
    AZERBAIJANI = "az-AZ"
    BASQUE = "eu"
    BELARUSIAN = "be"
    BENGALI_BD = "bn-BD"
    BENGALI = "bn"
    BOSNIAN = "bs-BA"
    BULGARIAN = "bg-BG"
    CATALAN = "ca"
    CHINESE_PRC = "zh-CN"
    CHINESE_HK = "zh-HK"
    CHINESE_TW = "zh-TW"
    CROATIAN = "hr-HR"
    CZECH = "cs-CZ"
    DANISH = "da-DK"
    DUTCH = "nl-NL"
    ENGLISH = "en"
    ENGLISH_US = "en-US"
    ESTONIAN = "et-EE"
    FARSI = "fa"
    FARSI_AF = "fa-AF"
    FINNISH = "fi-FI"
    FRENCH_CA = "fr-CA"
    FRENCH = "fr"
    GALICIAN = "gl"
    GEORGIAN = "ka-GE"
    GERMAN = "de"
    GREEK = "el-GR"
    GUJARATI = "gu-IN"
    HAUSA = "ha"
    HEBREW = "he-IL"
    HINDI = "hi-IN"
    HUNGARIAN = "hu-HU"
    ICELANDIC = "is-IS"
    IGBO = "ig-NG"
    INDONESIAN = "id-ID"
    ITALIAN = "it"
    JAPANESE = "ja-JP"
    KANNADA = "kn-IN"
    KASHMIRI = "ks-IN"
    KAZAKH = "kk-KZ"
    KHMER = "km-KH"
    KIRGHIZ = "ky-KG"
    KOREAN = "ko-KR"
    LAO = "lo-LA"
    LATVIAN = "lv-LV"
    LINGALA = "ln"
    LITHUANIAN = "lt-LT"
    MACEDONIAN = "mk-MK"
    MALAGASY = "mg-MG"
    MALAY = "ms-MY"
    MALAYALAM = "ml-IN"
    MARATHI = "mr-IN"
    MONGOLIAN = "mn-MN"
    NORWEGIAN = "no-NO"
    ORIYA = "or-IN"
    POLISH = "pl-PL"
    PORTUGUESE_BR = "pt-BR"
    PORTUGUESE = "pt-PT"
    PUNJABI = "pa"
    PUSHTO = "ps"
    ROMANIAN = "ro-RO"
    RUSSIAN = "ru-RU"
    SERBIAN = "sr-YU"
    SESOTHO = "st"
    SINHALA = "si-LK"
    SLOVAK = "sk-SK"
    SLOVENE = "sl-SL"
    SPANISH = "es-ES"
    SPANISH_AM = "es-US"
    SWAHILI = "sw"
    SWEDISH = "sv"
    TAGALOG = "tl-PH"
    TAMIL = "ta"
    TELUGU = "te-IN"
    THAI = "th-TH"
    TAJIK = "tg-TJ"
    TURKISH = "tr-TR"
    TURKMEN_LATIN = "tk"
    UKRAINIAN = "uk-UA"
    URDU = "ur"
    UZBEK = "uz-UZ"
    VIETNAMESE = "vi-VN"
    XHOSA = "xh"
    YORUBA = "yo"
    ZULU = "zu"
