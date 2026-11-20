class MyCalendarTwo:
    
    def __init__(self):
        self.maxMeetings = 2
        self.events = [] # stores (time, change = +1 / -1)

    def book(self, startTime: int, endTime: int) -> bool:
        # append to events and check

        self.events.append([startTime, +1])
        self.events.append([endTime, -1])

        self.events.sort()
                # [(2, +1), (4, +1), (6, +1), (7, -1), (8, -1), (8, +1)..]
        
        current = 0
        for _, change in self.events:
            current += change
            if current > self.maxMeetings:
                self.events.remove([startTime, +1])
                self.events.remove([endTime, -1])
                return False
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)