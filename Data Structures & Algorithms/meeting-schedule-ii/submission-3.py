"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        events = []
        for inter in intervals:
            events.append((inter.start, 1))
            events.append((inter.end, -1))

        # At the same time, -1 sorts before +1, so a meeting ending at 10
        # frees its room before a meeting starting at 10 needs one
        events.sort()

        rooms = max_rooms = 0
        for _, change in events:
            rooms += change
            max_rooms = max(max_rooms, rooms)
        return max_rooms