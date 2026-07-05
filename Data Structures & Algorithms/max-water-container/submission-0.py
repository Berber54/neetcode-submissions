class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max = 0
        for x in range(len(heights)):
            for y in range(len(heights)):
                if heights[x] <= heights[y]:
                    if heights[x] * (y - x) > max and y > x:
                        max = heights[x] * (y - x)
                else:
                    if heights[y] * (y - x) > max and y > x:
                        max = heights[y] * (y - x)
        return max