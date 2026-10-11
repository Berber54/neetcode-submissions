class MinStack:

    def __init__(self):
        self.data = []
        self.m = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.m or val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        if self.m[-1] == self.data.pop():
            self.m.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.m[-1]