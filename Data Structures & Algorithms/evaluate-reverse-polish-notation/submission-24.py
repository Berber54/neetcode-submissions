class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        operator = ['+', '-', '*', '/']

        for x in tokens:
            if x in operator:
                s = operand.pop()
                f = operand.pop()
                if x == '+':
                    operand.append(f + s)
                elif x == '-':
                    operand.append(f - s)
                elif x == '*':
                    operand.append(f * s)
                else:
                    operand.append(int(f / s))
            else:
                operand.append(int(x))

        return operand[-1]