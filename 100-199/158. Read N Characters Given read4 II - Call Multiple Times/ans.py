from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

def read4(buf4):
    return 0

class Solution:
    def __init__(self) -> None:
        self.storage = [' '] * 4
        self.storageLen = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [' '] * 4
        i = 0
        remaining = n
        numRead = 0

        if self.storageLen:
            numToBeRead = min(self.storageLen, n)
            buf[:numToBeRead] = self.storage[:numToBeRead]
            i += numToBeRead
            remaining -= numToBeRead
            self.storage = self.storage[numToBeRead:] + [' '] * numToBeRead
            self.storageLen -= numToBeRead

        while remaining >= 4:
            numRead = read4(buf4)
            if not numRead: break
            remaining -= numRead
            buf[i:i+numRead] = buf4[:numRead]
            i += numRead

        if remaining:
            numRead = read4(buf4)
            if numRead <= remaining:
                buf[i:i+numRead] = buf4[:numRead]
                i += numRead
            else:
                buf[i:i+remaining] = buf4[:remaining]
                i += remaining
                self.storage[:numRead - remaining] = buf4[remaining:numRead]
                self.storageLen = numRead - remaining
        
        return i

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def read(self, buf: List[str], n: int) -> int:
        

s = Solution()