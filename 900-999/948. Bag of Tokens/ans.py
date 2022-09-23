from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# stop when
# if taking biggest power to win as losing 1 score, the smallest power to lose for 1 score

# continue lose power, get one score, then continue to lose
# smallest power to lose is bigger than biggest power to win

# class Solution:
#     def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
#         tokens.sort()
#         n = len(tokens)
#         l, r = 0, n-1
        
#         score = 0
#         maxScore = 0
#         while l <= r:
            
#             while l <= r and power >= tokens[l]:
#                 power -= tokens[l]
#                 l += 1
#                 score += 1
#             maxScore = max(maxScore, score)
            
#             if r >= l and score > 0:
#                 power += tokens[r]
#                 r -= 1
#                 score -= 1
            
#             if l>r or power < tokens[l]:
#                 break
#         return maxScore

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        total = sum(tokens)+power
        half = total // 2
        cur = 0

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if cur + token > half:
                break
            cur += token
            i += 1
        
        return i
        # [50] 100 -> 1
        # [200] 100 -> 0

        # [100 200 200 300] 200 -> 3
        # [100 100 100 200 300] 200 -> 4

        # [1 2 3 4] 1000 -> 4

        # [100 100] 100 -> 1
        # [100 100 100 100] 100 -> 1

        # [100 100 100 200 200 200 | 200 200 300] 200 -> 4
        

s = Solution()
print(s.bagOfTokensScore([100,200,300,400],200))