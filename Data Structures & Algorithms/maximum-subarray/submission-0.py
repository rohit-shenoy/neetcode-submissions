class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running = 0                 # the sum of the stretch I'm currently holding
        best = float('-inf')        # the best sum I've ever seen

        for x in nums:
            running += x                    # 1. add the next number to my stretch
            best = max(best, running)       # 2. is this my best ever? write it down
            if running < 0:                 # 3. is my stretch now a burden?
                running = 0                 #    throw it away and start fresh

        return best


