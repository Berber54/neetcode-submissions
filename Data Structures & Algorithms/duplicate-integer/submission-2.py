class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        nums2 = sorted(list(set(nums)))
        if nums2 == nums:
            return False
        else:
            return True