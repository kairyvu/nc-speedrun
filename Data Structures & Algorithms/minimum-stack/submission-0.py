class MinStack:

    def __init__(self):
        self.stack = [] # (element, currMin)

    def push(self, val: int) -> None:
        prevMin = val if not self.stack else self.stack[-1][1]
        self.stack.append((val, min(prevMin, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
