"""An implementation of deque."""


class Deque:
    """Deque."""

    def __init__(self, size):
        """Init."""
        self.size = size
        self.buffer = [None] * size
        self.left = 0
        self.right = 0

    def append(self, x):
        """Append."""
        self.buffer[self.right % self.size] = x
        self.right += 1

    def appendleft(self, x):
        """Append left."""
        self.buffer[(self.left - 1) % self.size] = x
        self.left -= 1

    def pop(self):
        """Pop."""
        x = self.buffer[(self.right - 1) % self.size]
        self.buffer[(self.right - 1) % self.size] = None
        self.right -= 1
        return x

    def popleft(self):
        """Pop left."""
        x = self.buffer[self.left % self.size]
        self.buffer[self.left % self.size] = None
        self.left += 1
        return x

    def peek(self):
        """Peek."""
        return self.buffer[(self.right - 1) % self.size]

    def peekleft(self):
        """Peek left."""
        return self.buffer[self.left % self.size]

    def __len__(self):
        """Len."""
        return self.right - self.left

    def __iter__(self):
        """Iterate."""
        return DequeIterator(self)


class DequeIterator:
    """Iterator."""

    def __init__(self, deque):
        """Init."""
        self.deque = deque
        self.pos = deque.left

    def __iter__(self):
        """Iterate."""
        return self

    def __next__(self):
        """Next."""
        if self.pos >= self.deque.right:
            raise StopIteration
        else:
            self.pos += 1
            return self.deque.buffer[(self.pos - 1) % self.deque.size]