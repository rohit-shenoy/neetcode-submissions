class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Can there be zero intervals? Then return newInterval
        # Overlap is strict - 1st needs to end before next starts
        # Intervals are sorted - place just once
        # Compare new interval with every interval in array
        #   Three cases:
        #       a) Ends fully before current interval: add to start and append rest
        #       b) Starts without overlap after CI: add CI to output, continue iteration
        #       c) Overlap: Merge the two, but don't yet append, can merge with next too, update newInterval

        if len(intervals) == 0:
            return [newInterval]

        inserted = []
        # Atleast one
        for i in range(len(intervals)):
            newStart, newEnd = newInterval[0], newInterval[1]
            # before current interval - place found insert
            if newEnd < intervals[i][0]:
                inserted.append(newInterval)
                return inserted + intervals[i:]
            # starts after current interval
            elif newStart > intervals[i][1]:
                inserted.append(intervals[i])
            else:
                # overlap
                newInterval = [min(intervals[i][0], newStart), 
                                max(intervals[i][1], newEnd)]
        # If no return, then newInterval (merged or not goes to end, insert)
        inserted.append(newInterval)
        return inserted