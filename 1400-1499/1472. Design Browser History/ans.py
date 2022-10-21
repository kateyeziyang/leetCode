from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

"""
stack?

Want to remove part of stack very quickly.
Want to jump to some part of stack, but possibly not remove the history.

Array
"""

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 1
        self.historyLen = 1

    def visit(self, url: str) -> None:
        if self.idx != len(self.history):
            self.history[self.idx] = url
            self.historyLen = self.idx + 1
        else:
            self.history.append(url)
            self.historyLen += 1
        self.idx += 1

    def back(self, steps: int) -> str:
        # if self.idx == 1: return
        if steps > self.idx-1:
            steps = self.idx-1
        self.idx -= steps
        return self.history[self.idx-1]

    # [lc, google]
    # idx = 2
    # can move back 1
    # idx = 1
    # return [0] (idx-1)
    # idx = 1
    # can move 1
    # idx = 2
    # return [1]
    # idx = 2
    # can move 0

    def forward(self, steps: int) -> str:
        forwardLimit = self.historyLen - self.idx
        # if forwardLimit == 0: return
        if steps > forwardLimit:
            steps = forwardLimit
        self.idx += steps
        return self.history[self.idx-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps) 

s = Solution()