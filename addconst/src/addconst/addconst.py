class ConstAdder:
    def __init__(self, *, constant):
        self.constant = constant

    def __call__(self, n):
        return n + self.constant
