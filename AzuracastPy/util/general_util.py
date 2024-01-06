from AzuracastPy.constants import LANGUAGES

def get_language_code(language: str) -> str:
    try: 
        return LANGUAGES[language]
    except (KeyError):
        raise KeyError(f"The language code for '{language}' could not be found.")