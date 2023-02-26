from translators import google

languages = {'english': 'en', 'chinese': 'zh', 'arabic': 'ar', 'russian': 'ru', 'french': 'fr', 'german': 'de', 
             'spanish': 'es', 'portuguese': 'pt', 'italian': 'it', 'japanese': 'ja', 'korean': 'ko', 'greek': 'el', 
             'dutch': 'nl', 'hindi': 'hi', 'turkish': 'tr', 'malay': 'ms', 'thai': 'th', 'vietnamese': 'vi', 
             'indonesian': 'id', 'hebrew': 'he', 'polish': 'pl', 'mongolian': 'mn', 'czech': 'cs', 'hungarian': 'hu', 
             'estonian': 'et', 'bulgarian': 'bg', 'danish': 'da', 'finnish': 'fi', 'romanian': 'ro', 'swedish': 'sv', 
             'slovenian': 'sl', 'persian/farsi': 'fa', 'bosnian': 'bs', 'serbian': 'sr', 'fijian': 'fj', 'filipino': 'tl',
             'haitiancreole': 'ht', 'catalan': 'ca', 'croatian': 'hr', 'latvian': 'lv', 'lithuanian': 'lt', 'urdu': 'ur', 
             'ukrainian': 'uk', 'welsh': 'cy', 'tahiti': 'ty', 'tongan': 'to', 'swahili': 'sw', 'samoan': 'sm', 'slovak': 'sk',
             'afrikaans': 'af', 'norwegian': 'no', 'bengali': 'bn', 'malagasy': 'mg', 'maltese': 'mt', 'queretaro': 'otomi',
             'klingon/tlhingan': 'hol', 'gujarati': 'gu', 'tamil': 'ta', 'telugu': 'te', 'punjabi': 'pa', 'amharic': 'am',
             'azerbaijani': 'az', 'bashkir': 'ba', 'belarusian': 'be', 'cebuano': 'ceb', 'chuvash': 'cv', 'esperanto': 'eo',
             'basque': 'eu', 'irish': 'ga'}

def translate(text: str, langauge_from: str, language_to: str) -> str:
    langauge_from = langauge_from.lower()
    language_to = language_to.lower()

    if not langauge_from in languages:
        raise Exception("language_from not in available list of languages")
    if not language_to in languages:
        raise Exception("language_to not in available list of languages")
    
    return google(text, from_language=languages[langauge_from], to_language=languages[language_to])
