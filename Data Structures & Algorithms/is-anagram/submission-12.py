class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1

        for c in t:
            seen[c] -= 1

        for c in seen.values():
            if c != 0:
                return False

        return True