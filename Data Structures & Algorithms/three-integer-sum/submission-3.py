class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1
        
        res = set()

        for x in range(len(nums)):
            l, r = x + 1, len(nums) - 1
            target = -nums[x]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add(tuple(sorted([nums[x], nums[r], nums[l]])))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return [list(r) for r in res]