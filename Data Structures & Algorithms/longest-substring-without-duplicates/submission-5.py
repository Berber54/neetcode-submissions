class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) >= 2:
            l, r = 0, 1
            history = set()
            stack = [s[l]]
        else:
            return len(s)
        
        while r < len(s):
            if s[r] in stack:
                history.add(len(stack))
                l += 1
                r = l
                stack = [s[l]]
            else:
                stack.append(s[r])
                if r == len(s) - 1:
                    history.add(len(stack))

            r += 1

        return max(history)