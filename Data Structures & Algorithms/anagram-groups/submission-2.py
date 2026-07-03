class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            if "".join(sorted(x)) not in hashmap:
                hashmap["".join(sorted(x))] = [x]
            else:
                hashmap["".join(sorted(x))].append(x)
        return [x for i, x in hashmap.items()]