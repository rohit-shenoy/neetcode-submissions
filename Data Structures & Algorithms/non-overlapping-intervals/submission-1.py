class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end time

        removed = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:      # no overlap (touching is fine)
                prev_end = end         # keep it
            else:
                removed += 1           # overlaps with a kept interval: remove it
        return removed