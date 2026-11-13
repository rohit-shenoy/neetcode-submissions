class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        intervals.sort(key = lambda x: x[0])

        # iterate through the intervals one by one
        for i in range(len(intervals)):
            # For each interval, compare it with the next one, and check for overlap    
            # if no overlap, append current one
            if (i + 1) == len(intervals) or intervals[i][1] < intervals[i + 1][0]:
                merged.append(intervals[i])
            else:
                # overlap
                intervals[i + 1] = [
                    min(intervals[i][0], intervals[i + 1][0]),
                    max(intervals[i][1], intervals[i + 1][1])
                ]
        return merged