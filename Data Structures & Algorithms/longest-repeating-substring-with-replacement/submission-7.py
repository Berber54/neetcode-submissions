class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alph = [0] * 26
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            alph[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, alph[ord(s[r]) - ord('A')])
            while (r - l + 1 - maxf) > k:
                alph[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res