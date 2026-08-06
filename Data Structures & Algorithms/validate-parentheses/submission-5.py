class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for c in s:
            if c in m.values():
                stack.append(c)
            else:
                if stack:
                    if stack.pop() != m[c]:
                        return False
                else:
                    return False
        
        if stack != []:
            return False
        else:
            return True