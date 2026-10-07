class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r
        buyDay, sellDay = 0, 1
        maxProfit = 0

        while sellDay < len(prices):
            # profit made?
            if prices[buyDay] < prices[sellDay]:
                currentProfit = prices[sellDay] - prices[buyDay]
                maxProfit = max(maxProfit, currentProfit)
            else:
                # min price found
                buyDay = sellDay
            sellDay += 1
        return maxProfit