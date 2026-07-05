class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i, word in enumerate(strs):
            res[tuple(sorted(word))].append(strs[i])
            
        return [word_list for word_list in res.values()]