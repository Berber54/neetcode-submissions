class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(':')', '{':'}','[':']'}
        stack = []

        for b in s:
            if b in table:
                stack.append(b)
            elif not stack or table[stack.pop()] != b:
                return False

        return not stack