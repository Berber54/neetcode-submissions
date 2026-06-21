class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for n in range(len(nums) - 1):
            if nums[n] == nums[n+1]:
                return True
        return False