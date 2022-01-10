from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def letterSort(s):
            spaceIdx = s.find(" ")
            return s[spaceIdx+1:],s[:spaceIdx]
        digitLogs = []
        letterLogs = []
        for i,log in enumerate(logs):
            if log[log.find(" ")+1].isnumeric():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs = sorted(letterLogs,key=letterSort)
        return letterLogs+digitLogs

s = Solution()
# print(s.reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(s.reorderLogFiles(["t kvr", "r 3 1", "i 403", "7 so", "t 54"]))