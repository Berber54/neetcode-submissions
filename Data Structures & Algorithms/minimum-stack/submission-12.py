class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min or self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        tmp = self.data.pop()
        if self.min[-1] == tmp:
            self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]