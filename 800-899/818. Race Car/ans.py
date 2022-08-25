from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def racecar(self, target: int) -> int:
        dp = [float("inf")]*(target+1)
        dp[0] = 0
        n = 1
        for i in range(1, target+1):
            if i==11:
                print("here")
            if 2**n-1 == i:
                dp[i] = n
                n += 1
                continue
            for j in range(1, target//2+1):
                if 2**dp[j]-1 != j or 2**dp[i-j]-1 != i-j:
                    dp[i] = min(dp[i], dp[j]+dp[i-j]+1)
                else:
                    dp[i] = min(dp[i], dp[j]+dp[i-j]+2)
            dp[i] = min(dp[i], n + 1 + dp[2**n-1-i])
            for j in range(target+1, 2**n):
                # dp[i] = min(dp[i], dp[2**n-j]+dp[j-i]+3+n)
                if 2**dp[2**n-1-j]-1 != 2**n-1-j or 2**dp[j-i]-1 != j-i:
                    dp[i] = min(dp[i], n + 2 + dp[2**n-1-j] + dp[j-i])
                else:
                    dp[i] = min(dp[i], n + 3 + dp[2**n-1-j] + dp[j-i])
        return dp[-1]

s = Solution
# s.racecar(9)
for i in range(1,12):
    print(s.racecar(s, i))

# 1 1
# 2 4
# 3 2
# 4 5
# 5 7
# 6 5
# 7 3
# 8 6
# 9 8: 0 1 3 3 2 2 3 5 9
# 10 7
# 11 10: 0 1 3 7 7 7 8 10 10 10 11