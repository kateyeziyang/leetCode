from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.bookings = []
    
    def isOverlapping(x1, x2, y1, y2):
        return x1 < y2 and y1 < x2

    def book(self, start: int, end: int) -> bool:
        for i in range(0, len(self.bookings), 2):
            if self.isOverlapping(start, end, self.bookings[i], self.bookings[i+1]):
                return False
        self.bookings += [start, end]
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

s = Solution()