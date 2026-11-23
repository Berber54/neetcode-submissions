class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            m = target - nums[i]
            if m in seen:
                return [seen[m], i]

            seen[nums[i]] = i