class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b, s = 0, 1
        maxP = 0

        for s in range(1, len(prices)):
            # is there a profit
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(maxP, profit)
            else:
                # new minimum found
                b = s
        return maxP