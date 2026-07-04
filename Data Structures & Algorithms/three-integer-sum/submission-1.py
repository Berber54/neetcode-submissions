class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        res = set()

        for x in range(len(nums)):
            for y in range(len(nums)):
                if 0 - nums[x] - nums[y] in nums_set:
                    if x != y and y != nums.index(0 - nums[x] - nums[y]) and x != nums.index(0 - nums[x] - nums[y]):
                        res.add(tuple(sorted([nums[x], nums[y], 0 - nums[x] - nums[y]])))
        return [list(r) for r in res]