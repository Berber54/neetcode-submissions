class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = ""

        for t in tokens:
            try:
                stack.append(int(t))
            except:
                s = f"{stack[-2]} {t} {stack[-1]}"
                stack.pop()
                stack.pop()
                stack.append(int(eval(s)))
                s = ""

        return stack[-1]