class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26

        for c in s:
            alpha[ord(c) - ord('a')] += 1

        for c in t:
            alpha[ord(c) - ord('a')] -= 1

        if alpha == [0] * 26:
            return True
        else:
            return False