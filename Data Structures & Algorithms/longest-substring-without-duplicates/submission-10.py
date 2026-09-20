class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        his = set()
        res = 0
        while r < len(s):
            while s[r] in his:
                his.remove(s[l])
                l += 1
            his.add(s[r])
            r += 1
            res = max(res, r - l)
        return res