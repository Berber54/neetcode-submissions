class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit < 0:
                l = r

            if profit > result:
                result = profit
            
            r += 1

        return result