class MinStack:

    def __init__(self):
        self.mem = []
        self.small = []

    def push(self, val: int) -> None:
        self.mem.append(val)
        if self.small == []:
            self.small.append(val)
        elif val < self.small[-1]:
            self.small.append(val)
        else:
            self.small.append(self.small[-1])

    def pop(self) -> None:
        x = self.mem.pop()
        self.small.pop()
        
    def top(self) -> int:
        return self.mem[-1]

    def getMin(self) -> int:
        return self.small[-1]