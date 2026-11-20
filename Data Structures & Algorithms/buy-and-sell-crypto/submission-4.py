class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j] - buy
                max_profit = max(max_profit, sell)
        return max_profit


