class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []

        for t in tokens:
            if t in ('+', '-', '*', '/'):
                s = num.pop()
                f = num.pop()
                if t == '+':
                    num.append(f + s)
                elif t == '-':
                    num.append(f - s)
                elif t == '*':
                    num.append(f * s)
                elif t == '/':
                    num.append(int(f / s))

            else:
                num.append(int(t))

        return num[-1]