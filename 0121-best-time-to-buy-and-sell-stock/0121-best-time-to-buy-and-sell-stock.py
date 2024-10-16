class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force solution: O(n^2)
        # profit = 0
        # buy = 0
        # while buy <= len(prices):
        #     sell = buy + 1
        #     while sell <= len(prices) - 1:
        #         if prices[sell] - prices[buy] > profit:
        #             profit = prices[sell] - prices[buy]
        #             sell += 1
        #         else: 
        #             sell += 1
        #     buy += 1
        # return profit

        # Optimal/Efficient Solution
        buy = 0
        sell = 1
        profit = 0
        maxprofit = 0
        while (sell < len(prices)):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(maxprofit, profit)
            else:
                buy = sell
            sell += 1
        return maxprofit