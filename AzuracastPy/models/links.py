from AzuracastPy.util.general_util import generate_repr_string

class Links:
    def __init__(self_, self: str, intro: str, listen: str, **kwargs):
        self_.self = self
        self_.intro = intro
        self_.listen = listen
        self_.__dict__.update(kwargs) # Incase there are other attributes in the link object from the API
    
    def __repr__(self):
        return generate_repr_string(self)