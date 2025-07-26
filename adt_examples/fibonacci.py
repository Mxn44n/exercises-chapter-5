class Fib:

    def __init__(self):
        self.state = (0, 1)

    def __iter__(self):
        return self

    def __next__(self):
        self.state = (self.state[1], self.state[0] + self.state[1])
        return self.state[1]
