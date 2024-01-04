class Links:
    def __init__(self_, self: str, intro: str, listen: str, **kwargs):
        self_.self = self
        self_.intro = intro
        self_.listen = listen
        self_.__dict__.update(kwargs) # Incase there are other attributes in the link object from the API
    
    def __repr__(self):
        return f"Links(self={self.self!r}, intro={self.intro!r}, listen={self.listen!r}, {', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"