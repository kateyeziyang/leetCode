from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        q = deque([[0,[]]])
        ans = []

        while q:
            node,intermed = q.popleft()
            for i,w in enumerate(wordDict):
                if s[node:node+len(w)]==w:
                    if node+len(w)==len(s):
                        tmp = []
                        for idx in intermed:
                            tmp.append(wordDict[idx])
                        tmp.append(w)
                        ans.append(" ".join(tmp))
                        continue
                    q.append([node+len(w),intermed + [i]])
        return ans

s = Solution()
assert set(s.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))==set(["cats and dog","cat sand dog"])
assert set(s.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))==set(["pine apple pen apple","pineapple pen apple","pine applepen apple"])