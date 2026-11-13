class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]  # always tracks where current interval ended

        for start, end in intervals[1:]:
            # no overlap
            if start >= prevEnd:
                prevEnd = end
            else:
                # overlap
                res += 1
                # we delete the one ending last, to minimize conflicts, and so keep prevEnd
                prevEnd = min(prevEnd, end)
        return res