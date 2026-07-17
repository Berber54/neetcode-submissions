class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml, mr = 0, len(matrix) - 1

        while ml <= mr:
            mmid = (ml + mr) // 2
            row = matrix[mmid]
            if matrix[mmid][-1] < target and matrix[mmid][0] < target:
                ml = mmid + 1

            elif matrix[mmid][-1] > target and matrix[mmid][0] > target:
                mr = mmid - 1
            else:
                break

        cl, cr = 0, len(row) - 1

        while cl <= cr:
            cmid = (cl + cr) // 2
            if row[cmid] < target:
                cl = cmid + 1

            elif row[cmid] > target:
                cr = cmid - 1

            else:
                return True

        return False