class Solution:
    def isValid(self, s: str) -> bool:
        o = '({['
        c = ')}]'
        stack = []
        for x in s:
            if x in o:
                stack.append(x)
            else:
                if not stack:
                    return False
                if c.index(x) != o.index(stack.pop()):
                    return False
        return not stack