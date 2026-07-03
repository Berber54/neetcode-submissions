class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            if target - numbers[n] not in numbers:
                continue
            elif n < numbers.index(target - numbers[n]):
                return [n + 1, numbers.index(target - numbers[n]) + 1]