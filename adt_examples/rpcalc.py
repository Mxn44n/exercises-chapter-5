"""An implementation of stack."""
from numbers import Number
import math

binary_operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

functions = {
    "sin": math.sin,
    "cos": math.cos
}


class RPCalc:

    def __init__(self):
        self.stack = []

    def push(self, n):
        if isinstance(n, Number):
            self.stack.append(n)

        elif n in binary_operators:
            y = self.pop()
            x = self.pop()
            self.push(binary_operators[n](x, y))

        elif n in functions:
            x = self.pop()
            self.push(functions[n](x))
        
        else:
            raise ValueError(f"Unknown calculator input {n}")
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)

        

