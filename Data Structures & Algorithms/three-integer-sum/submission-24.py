class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, n in enumerate(nums):
            target = - n
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    x = [nums[i], nums[r], nums[l]]
                    x.sort()
                    res.add(tuple(x))
                    l += 1
                    r -= 1
        res = [list(z) for z in res]
        return res