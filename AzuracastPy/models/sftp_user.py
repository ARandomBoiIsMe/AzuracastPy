class SFTPUser:
    def __init__(self, id: int, username: str, password: str, publicKeys: str):
        self.id = id
        self.username = username
        self.password = password
        self.public_keys = publicKeys

    def __repr__(self):
        return (
            f"SFTPUser(id={self.id!r}, username={self.username!r}, password={self.password!r}, "
            f"public_keys={self.public_keys!r})"
        )