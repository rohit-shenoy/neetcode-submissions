class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        # O(N^2) brute force
        #best = float('-inf')
        #for j in range(1, len(values)):
        #   for i in range(j):
        #        best = max(best, values[i] + values[j] + i - j)
        #return best


        # Replace inner-loop with running best
        # values[j] - j + OPTIMIZE bestLeft = (values[i]  + i)
        bestLeft = values[0] + 0    # max of values[i] + i over i < j
        best = float('-inf')
        for j in range(1, len(values)):
            best = max(best, bestLeft + values[j] - j)
            bestLeft = max(bestLeft, values[j] + j)
                
        return best