from collections import defaultdict, deque
from datetime import datetime, timedelta
from typing import List

# class Solution:
#     def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#         def getTime(s):
#             return datetime.strptime(s, '%H:%M')
        
#         # assume already sorted
#         def shouldAlert(n):
#             swipes[n].sort()
#             q = deque()
            
#             for time in swipes[n]:
#                 q.append(time)
#                 while q[0] < time - timedelta(hours=1):
#                     q.popleft()
#                 if len(q) == 3:
#                     return True
#             return False
        
#         swipes = defaultdict(list)
#         result = []
        
#         for n, t in zip(keyName, keyTime):
#             swipes[n].append(getTime(t))
#         for n in swipes.keys():
#             if shouldAlert(n):
#                 result.append(n)
#         return sorted(result)

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def getTime(s):
            return datetime.strptime(s, '%H:%M')
        
        # assume already sorted
        def shouldAlert(n):
            swipes[n].sort()

            l, r = 0, 0

            while r < len(swipes[n]):
                while swipes[n][l] < swipes[n][r] - timedelta(hours=1):
                    l += 1
                if r-l+1 == 3:
                    return True
                r += 1
            return False
        
        swipes = defaultdict(list)
        result = []
        
        for n, t in zip(keyName, keyTime):
            swipes[n].append(getTime(t))
        for n in swipes.keys():
            if shouldAlert(n):
                result.append(n)
        return sorted(result)

Solution().alertNames(["john","john","john"],
["23:58","23:59","00:01"])
