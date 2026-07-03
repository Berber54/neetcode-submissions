class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for x in range(len(nums)):
            if target - nums[x] in hashset:
                return [hashset[target - nums[x]], x]
            hashset[nums[x]] = x