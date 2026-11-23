class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []
        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord('a')] += 1
            groups[tuple(char)].append(s)
        
        for l in groups.values():
            res.append(l)

        return res