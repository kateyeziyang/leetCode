from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s==s[::-1] else 2