class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = set(nums)
        res = 0
        for n in total:
            if n - 1 not in total:
                count = 1
                while n + 1 in total:
                    n += 1
                    count += 1
                res = max(res, count)

        return res