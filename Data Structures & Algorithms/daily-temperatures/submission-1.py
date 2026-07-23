class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 0
        res = []

        while l < len(temperatures):
            if temperatures[r] <= temperatures[l]:
                if r == len(temperatures) - 1:
                    res.append(0)
                    l += 1
                    r = l

                else:
                    r += 1

            else:
                res.append(r - l)
                l += 1
                r = l
        
        return res