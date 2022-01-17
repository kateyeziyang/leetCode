from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def compress(self, chars: List[str]) -> int:
        rep = chars[0]
        count = 0
        loc = 0
        for c in chars:
            if c==rep:
                count += 1
            else:
                chars[loc] = rep
                loc += 1
                if count!=1:
                    s = str(count)
                    for i in range(len(s)):
                        chars[loc+i] = s[i]
                    loc += len(s)
                count = 1
                rep = c
        chars[loc] = rep
        loc += 1
        if count!=1:
            s = str(count)
            for i in range(len(s)):
                chars[loc+i] = s[i]
            loc += len(s)
        return loc

s = Solution()
print(s.compress("abcdef"))
print(s.compress("aaaaaffffdeea"))