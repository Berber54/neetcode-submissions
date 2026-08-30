class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        m = 0

        while r < len(prices):
            p = prices[r] - prices[l]
            if p > m:
                m = p
            if p < 0:
                l = r
            r += 1

        return m