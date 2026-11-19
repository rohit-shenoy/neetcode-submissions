class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        runningMax, runningMin = 0, 0
        bestMax, bestMin = 0, float('inf')

        for x in nums:
            runningMax += x
            bestMax = max(bestMax, runningMax)
            if runningMax < 0:
                runningMax = 0
            

            runningMin += x
            bestMin = min(bestMin, runningMin)
            if runningMin > 0:
                runningMin = 0
        
        return max(bestMax, bestMin * -1)
        
