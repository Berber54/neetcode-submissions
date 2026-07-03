class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            if target - numbers[n] not in numbers[n + 1:]:
                continue
            else:
                return [n + 1, numbers.index(target - numbers[n]) + 1]