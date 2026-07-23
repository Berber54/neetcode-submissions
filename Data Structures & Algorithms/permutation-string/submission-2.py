class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1, map2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1

        l, r = 0, len(s1) - 1
        while map1 != map2:
            if r == len(s2) - 1:
                return False
            map2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            map2[ord(s2[r]) - ord('a')] += 1
            

        return True