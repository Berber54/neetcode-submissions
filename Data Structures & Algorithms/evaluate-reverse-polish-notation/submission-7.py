class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = ""
        operators = ("+", "-", "*", "/")

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                s = f"{stack[-2]} {t} {stack[-1]}"
                stack.pop()
                stack.pop()
                stack.append(int(eval(s)))
                s = ""

        return stack[-1]