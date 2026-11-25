"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        THRESHOLD = 1

        events = []
        for inter in intervals:
            events.append((inter.start, +1))
            events.append((inter.end, -1))
        
        events.sort(key = lambda x:x[0])

        currentLoad = 0
        for _, change in events:
            currentLoad += change
            if currentLoad > THRESHOLD:
                return False
        return True
