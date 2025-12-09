class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0 
        right = 1
        profit = 0
        max_profit = 0 

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit








        # Two pointesr 
        # maxProfit = 0 
        # profit = 0
        # left, right = 0, len(prices) -1
        # if len(prices) <3 and prices[right] > prices[left]:
        #     return prices[right] - prices[left]
        # for i, v in enumerate(prices):
        #     value = prices[right] - prices[left] 
        #     if v < prices[left] and right > i and value > profit:
        #         left = i
        #     elif v > prices[right] and left < i and value > profit:
        #         right = i 
        #     profit = max(profit, value)
        #     print(left, right)
        # return profit 
        # while left < right: 
        #     val = prices[right] - prices[left]
        #     if val > 0: 
        #         result = max(result, val)
        #     if prices[left+1] < prices[left]:
        #         left += 1
        #     elif prices[right-1] > prices[right]:
        #         right -= 1
        #     else:
        #         return result 
        # return result 
        # Time Limit Exceeded
        # for index, value in enumerate(prices):
        #     right = prices[index:]
        #     profit = max(profit, max(right) - value)
        # return profit
