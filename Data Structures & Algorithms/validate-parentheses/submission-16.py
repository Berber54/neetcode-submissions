class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(':')', '{':'}','[':']'}
        stack = []

        for b in s:
            if b in table:
                stack.append(b)
            else:
                if stack and table[stack.pop()] == b:
                    continue
                else:
                    return False

        return not stack