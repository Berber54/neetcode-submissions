class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums))]
        his = defaultdict(int)
        res = []

        for n in nums:
            his[n] += 1

        for n, c in his.items():
            count[len(nums) - c].append(n)

        for c in count:
            if c != None and len(res) < k:
                res += c

        return res