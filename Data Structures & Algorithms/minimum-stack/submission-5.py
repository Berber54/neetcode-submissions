class MinStack:

    def __init__(self):
        self.mem = []
        self.small = []

    def push(self, val: int) -> None:
        self.mem.append(val)
        self.small.append(min(val, self.small[-1] if self.small else val))

    def pop(self) -> None:
        self.mem.pop()
        self.small.pop()
        
    def top(self) -> int:
        return self.mem[-1]

    def getMin(self) -> int:
        return self.small[-1]