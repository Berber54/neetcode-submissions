class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        l, r = 0, 0

        while r < len(prices):
            prof = prices[r] - prices[l]
            if prof > max:
                max = prof

            if prof < 0:
                l = r
            
            r += 1
        
        return max