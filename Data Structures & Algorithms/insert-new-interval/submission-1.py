class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        finalIntervals = []
        

        for i in range(len(intervals)):
            newStart, newEnd = newInterval
            # ends before current interval starts
            if newEnd < intervals[i][0]:
                finalIntervals.append(newInterval)
                return finalIntervals + intervals[i:]
            # starts after current interval ends
            elif newStart > intervals[i][1]:
                finalIntervals.append(intervals[i])
            else:
                # overlaps with current interval
                newInterval = [
                    min(intervals[i][0], newStart), 
                    max(intervals[i][1], newEnd)
                    ]
                

        finalIntervals.append(newInterval)
        return finalIntervals
        