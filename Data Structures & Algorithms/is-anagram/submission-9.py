class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)

        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)

        for c in t:
            hashmap[c] -= 1
        
        for c in hashmap.values():
            if c != 0:
                return False

        return True