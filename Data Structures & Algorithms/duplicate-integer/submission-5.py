class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        clean_nums = list(set(nums))
        clean_nums.sort()
        if nums == clean_nums:
            return False
        else:
            return True
