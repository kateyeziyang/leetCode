from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        q = deque([[]])
        for digit in digits:
            for _ in range(len(q)):
                strBuf = q.popleft()
                for c in lMap[digit]:
                    q.append(strBuf+[c])
        ans = []
        while q:
            strBuf = q.popleft()
            ans.append("".join(strBuf))
        return ans

s = Solution()
print(s.letterCombinations("23"))