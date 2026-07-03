class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for n in range(len(s)):
            count_s[s[n]] = 1 + count_s.get(s[n], 0)
            count_t[t[n]] = 1 + count_t.get(t[n], 0)

        for x in count_s:
            if count_s[x] != count_t.get(x, 0):
                return False
        
        return True