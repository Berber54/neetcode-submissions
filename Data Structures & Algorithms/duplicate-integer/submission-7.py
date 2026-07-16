class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

        for c in hashmap.values():
            if c > 1:
                return True

        return False