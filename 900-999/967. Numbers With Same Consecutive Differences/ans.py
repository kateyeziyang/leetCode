from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        initialDigits = filter(lambda i: i+k<=9 or i-k>=0, range(1, 10))
        q = deque(initialDigits)

        for _ in range(n-1):
            newQueue = set()
            for _ in range(len(q)):
                num = q.popleft()
                lastDigit = num%10
                if lastDigit+k<=9:
                    newQueue.add(num*10+lastDigit+k)
                if lastDigit-k>=0:
                    newQueue.add(num*10+lastDigit-k)
            q = deque(newQueue)
        return list(q)

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(idx, num):
            nonlocal ans
            if idx == n:
                ans.append(num)
                return

            lastDigit = num%10
            if lastDigit+k<=9:
                backtrack(idx+1, num*10+lastDigit+k)
            if lastDigit-k>=0:
                backtrack(idx+1, num*10+lastDigit-k)

        if k==0:
            ans = []
            for i in range(1,10):
                ans.append(int(str(i)*n))
            return ans
        ans = []
        initialDigits = filter(lambda i: i+k<=9 or i-k>=0, range(1, 10))
        for initialDigit in initialDigits:
            backtrack(1, initialDigit)
        return ans

s = Solution()
print(s.numsSameConsecDiff(3,7))
# print(s.numsSameConsecDiff(2,0))