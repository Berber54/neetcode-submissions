class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        key = {')':'(', '}':'{', ']':'['}
        stack = []
        for n in s:
            if n not in key:
                stack.append(n)
            else:
                if stack:
                    if stack.pop() != key[n]:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False