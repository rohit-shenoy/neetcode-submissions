class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b, s = 0, 1
        maxP = 0

        while s < len(prices):
            # is there a profit
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(maxP, profit)
            else:
                # new minimum found
                b = s
            s += 1
        return maxP