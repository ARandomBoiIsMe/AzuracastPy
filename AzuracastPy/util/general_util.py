from AzuracastPy.constants import DAYS
    
def generate_repr_string(self) -> str:
    return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_'))})"

def get_day_number(day: str) -> int:
    try:
        return DAYS[day]
    except KeyError:
        raise KeyError(f"We both know that '{day}' isn't a day of the week.")
    
def convert_to_short_name(original_text: str) -> str:
    return original_text.strip().lower().replace(' ', '_')

def is_text_a_valid_short_name(text: str) -> bool:
    for char in text:
        if char.isspace():
            return False

    return True