class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = set()

        for n in nums:
            if n not in mem:
                mem.add(n)
            else:
                return n