class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                s = stack.pop()
                f = stack.pop()
                if t == '+':
                    stack.append(f + s)
                elif t =='-':
                    stack.append(f - s)
                elif t == '*':
                    stack.append(f * s)
                else:
                    stack.append(int(f / s))
            else:
                stack.append(int(t))
        return stack[-1]