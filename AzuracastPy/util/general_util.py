from AzuracastPy.constants import LANGUAGES

def get_language_code(language: str) -> str:
    try:
        return LANGUAGES[language]
    except (KeyError):
        raise KeyError(f"The language code for '{language}' could not be found.")
    
def generate_repr_string(self) -> str:
    return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_'))})"