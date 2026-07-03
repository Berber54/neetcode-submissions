class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = list(set(nums))
        nums.sort()
        consecutive = 1
        last_n = nums[0]
        sequences = []
        
        for n in nums[1:]:
            if n == last_n + 1:
                consecutive += 1
            else:
                sequences.append(consecutive)
                consecutive = 1
            last_n = n
        sequences.append(consecutive)
        sequences.sort()
        
        return sequences[-1]