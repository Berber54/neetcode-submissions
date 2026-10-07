class MinStack:

    def __init__(self):
        self.minstack = []
        self.m = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if not self.m or self.m[-1] >= val:
            self.m.append(val)
        return

    def pop(self) -> None:
        if self.m[-1] == self.minstack.pop():
            self.m.pop()
        return

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.m[-1]