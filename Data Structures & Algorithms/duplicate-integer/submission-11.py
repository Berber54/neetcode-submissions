class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        his = set()
        for n in nums:
            if n in his:
                return True
            his.add(n)
        return False