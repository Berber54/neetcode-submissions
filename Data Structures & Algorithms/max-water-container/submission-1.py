class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max = 0
        while l < r:
            lh = heights[l]
            rh = heights[r]
            if lh <= rh:
                cap = lh * (r - l)
                if cap > max:
                    max = cap
                l += 1
                
            else:
                cap = rh * (r - l)
                if cap > max:
                    max = cap
                r -= 1
            
        return max