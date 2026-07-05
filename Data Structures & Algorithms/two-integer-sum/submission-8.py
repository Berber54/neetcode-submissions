class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, n in enumerate(nums):
            hashtable[n] = i
        
        for n in range(len(nums)):
            if target - nums[n] in hashtable:
                if hashtable[target - nums[n]] > n:
                    return [n, hashtable[target - nums[n]]]