class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        new_lst = set()
        for x in strs:
            new_lst.add("".join(sorted(x)))
        result = []
        fresult = []
        for y in new_lst:
            for z in strs:
                if y == "".join(sorted(z)):
                    result.append(z)
            fresult.append(result)
            result = []
        return fresult