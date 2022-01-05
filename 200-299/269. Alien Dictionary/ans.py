from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(set)
        degree = Counter({c:0 for w in words for c in w})
        for fw,sw in zip(words,words[1:]):
            for c,d in zip(fw,sw):
                if c!=d:
                    if d not in g[c]:
                        g[c].add(d)
                        degree[d] += 1
                    break
            else:
                if len(fw)>len(sw): 
                    return ""
        ans = []
        q = deque([c for c in degree if degree[c]==0])
        while q:
            c = q.popleft()
            ans.append(c)
            for d in g[c]:
                degree[d] -= 1
                if degree[d] == 0:
                    q.append(d)
        if len(ans) != len(g):
            return ""
        return "".join(ans)

s = Solution()