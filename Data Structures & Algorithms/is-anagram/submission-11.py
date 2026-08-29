class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = [0] * 26
        
        for c in s:
            x[ord(c) - ord('a')] += 1

        for c in t:
            x[ord(c) - ord('a')] -= 1

        if x == [0] * 26:
            return True
        else:
            return False