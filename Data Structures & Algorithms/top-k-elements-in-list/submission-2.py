class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        
        ret = []
        for l in range(k):
            largest = 0
            res = None
            for v in nums:
                if dic[v] > largest:
                    largest = dic[v]
                    res = v
            dic[res] = 0
            ret.append(res)
        return ret