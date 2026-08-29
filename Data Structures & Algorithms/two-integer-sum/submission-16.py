class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for n in range(len(nums)):
            if target - nums[n] in s:
                return [s[target - nums[n]], n]
            else:
                s[nums[n]] = n
            