class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for k in range(1, len(prices)):
            change = prices[k] - prices[k - 1]
            if change > 0:          # price went up today
                profit += change    # be holding the stock for this day
        return profit