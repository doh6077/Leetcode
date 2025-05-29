class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 

        maxProfit = 0 
        while l < len(prices):
            if prices[r] < prices[l]:
                profit = prices[r] - prices[l]
                if maxProfit < profit:
                    maxProfit = profit

            else:
                l = r 
            r += 1 
        return maxProfit 
            
