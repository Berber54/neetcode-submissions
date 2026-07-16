class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r

            if profit > max:
                max = profit

            r += 1
        
        return max