class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        count = [0] * 26
        while r < len(s):
            count[ord('A') - ord(s[r])] += 1
            windowLen = r - l + 1
            freq = max(count)
            if k < windowLen - freq:
                count[ord('A') - ord(s[l])] -= 1
                l += 1
            else:
                if windowLen > res:
                    res = windowLen

            r += 1

        return res