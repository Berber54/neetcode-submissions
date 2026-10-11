class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            l, r = n + 1, len(nums) - 1
            target = -nums[n]
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[n]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res