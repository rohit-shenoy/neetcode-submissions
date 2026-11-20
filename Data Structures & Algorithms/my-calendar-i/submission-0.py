class MyCalendar:
    
    def __init__(self):
        self.events = [] # (time, +1 / -1)
        self.maxCapacity = 1

    def book(self, startTime: int, endTime: int) -> bool:
        self.events.append((startTime, +1))
        self.events.append((endTime, -1))

        self.events.sort()

        currentBookings = 0
        for _, change in self.events:
            currentBookings += change
            
            # remove added, and save False
            if currentBookings > self.maxCapacity:
                self.events.remove((startTime, +1))
                self.events.remove((endTime, -1))
                return False
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)