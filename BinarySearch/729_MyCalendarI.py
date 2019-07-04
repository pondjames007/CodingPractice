# TIPS:
# Use BISECT to do binary search

import bisect

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if not self.events: 
            bisect.insort(self.events, (start, end))
            return True
        
        # should be at index and the value at index shift right
        index = bisect.bisect(self.events, (start, end))
        if index == 0:
            if self.events[0][0] >= end: 
                bisect.insort(self.events, (start, end))
                return True
            else: return False
        if index == len(self.events):
            if self.events[-1][1] <= start: 
                bisect.insort(self.events, (start, end))
                return True
            else: return False
            
            
        if self.events[index][0] >= end and self.events[index-1][1] <= start:
            bisect.insort(self.events, (start, end))
            return True
        else: return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)