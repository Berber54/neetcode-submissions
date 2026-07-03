class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] += 1
            if hashtable[num] > 1:
                return True
        return False