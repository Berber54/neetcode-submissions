class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            if (target - nums[x]) in nums and x != nums.index(target - nums[x]):
                return sorted([x, nums.index(target - nums[x])])