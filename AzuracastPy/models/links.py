class Links:
    def __init__(self_, self: str, intro: str, listen: str, **kwargs):
        self_.self = self
        self_.intro = intro
        self_.listen = listen
        self_.__dict__.update(kwargs) # Incase there are other attributes in the link object from the API
    
    def __repr__(self_):
        return f"Links(self={self_.self!r}, intro={self_.intro!r}, listen={self_.listen!r}, {', '.join(f'{k}={v!r}' for k, v in self_.__dict__.items())})"