class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        pos = -1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                pos = m
                l, r = 0, len(matrix[pos]) - 1
                break
        
        if pos == -1:
            return False

        while l <= r:
            m = (l + r) // 2
            if matrix[pos][m] < target:
                l = m + 1
            elif matrix[pos][m] > target:
                r = m - 1
            else:
                return True
        return False