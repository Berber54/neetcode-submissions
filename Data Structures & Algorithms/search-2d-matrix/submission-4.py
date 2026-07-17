class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml, mr = 0, len(matrix) - 1

        while ml <= mr:
            mmid = (ml + mr) // 2
            if matrix[mmid][-1] < target:
                ml += 1
            elif matrix[mmid][-1] > target:
                mr -= 1
            else:
                return True
            row = matrix[mmid]
            cl, cr = 0, len(row) - 1
            while cl <= cr:
                cmid = (cl + cr) // 2
                if row[cmid] < target:
                    cl += 1
                elif row[cmid] > target:
                    cr -= 1
                else:
                    return True

        return False