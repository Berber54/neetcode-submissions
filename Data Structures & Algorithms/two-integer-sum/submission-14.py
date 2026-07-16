class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(nums)): #O(n)
            diff = target - nums[i]
            if diff in hashmap: #O(1)
                return [hashmap[diff], i]
            hashmap[nums[i]] = i