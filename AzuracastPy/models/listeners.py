class Listeners:
    def __init__(self, total, unique, current):
        self.total = total
        self.unique = unique
        self.current = current

    def __repr__(self):
        return (
            f"Listeners(total={self.total}, unique={self.unique}, current={self.current})"
        )