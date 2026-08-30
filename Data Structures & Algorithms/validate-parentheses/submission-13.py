class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(', '}':'{', ']':'['}
        stack = []
        for n in s:
            if n in key:
                if not stack or stack.pop() != key[n]:
                    return False
            else:
                stack.append(n)

        return not stack