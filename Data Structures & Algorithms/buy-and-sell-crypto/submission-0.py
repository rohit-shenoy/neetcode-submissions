class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0

        l, r = 0, 1  # left: buy, right: sell

        while r < len(prices):
            # profit?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_price = max(max_price, profit)
            else:
                # slide all the way to right
                l = r
            r += 1
        return max_price
        