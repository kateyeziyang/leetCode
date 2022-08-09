from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Logger:

    def __init__(self):
        self.msgMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msgMap or self.msgMap[message]+10<=timestamp:
            self.msgMap[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

s = Solution()