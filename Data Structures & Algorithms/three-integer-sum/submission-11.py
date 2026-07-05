class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()       
        res = []

        for x in range(len(nums)):
            if nums[x] == nums[x - 1] and x != 0:
                continue
            l, r = x + 1, len(nums) - 1
            target = -nums[x]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[x], nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return res