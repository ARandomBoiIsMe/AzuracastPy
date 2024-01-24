from AzuracastPy.constants import LANGUAGES, DAYS

def get_language_code(language: str) -> str:
    try:
        return LANGUAGES[language]
    except (KeyError):
        raise KeyError(f"The language code for '{language}' could not be found.")
    
def generate_repr_string(self) -> str:
    return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_'))})"

def get_day_number(day: str) -> int:
    try:
        return DAYS[day]
    except (KeyError):
        raise KeyError(f"We both know that '{day}' isn't a day of the week.")