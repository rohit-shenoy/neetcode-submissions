class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Need to place new interval once and done
        # New Interval can have one of 3 cases against current intervals

        resultIntervals = []

        for i in range(len(intervals)):
            # case 1: completely before current interval - placed and return
            if newInterval[1] < intervals[i][0]:
                resultIntervals.append(newInterval)
                return resultIntervals + intervals[i:]
            # case 2: completely after current interval - append current, not yet time to place newInterval
            elif newInterval[0] > intervals[i][1]:
                resultIntervals.append(intervals[i])
            # overlaps with current interval - may overlap with next ones - merge one at a time
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]
        # if theres no more intervals for case 1 return after adding - new goes to end
        resultIntervals.append(newInterval)
        return resultIntervals