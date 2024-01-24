from AzuracastPy.util.general_util import generate_repr_string

class Listeners:
    def __init__(
        self, 
        total, 
        unique, 
        current
    ):
        self.total = total
        self.unique = unique
        self.current = current

    def __repr__(self):
        return generate_repr_string(self)