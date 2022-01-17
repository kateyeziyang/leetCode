from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def qs(i,l,r):
            pidx = random.randint(l,r)
            pivot = wcount[uniques[pidx]]
            uniques[pidx],uniques[r] = uniques[r],uniques[pidx]
            cur = l
            for j in range(l,r):
                if wcount[uniques[j]]<pivot:
                    uniques[j],uniques[cur] = uniques[cur],uniques[j]
                    cur += 1
            uniques[r],uniques[cur] = uniques[cur],uniques[r]
            if cur==i:
                return cur
            elif cur<i:
                return qs(i,cur+1,r)
            else:
                return qs(i,l,r-1)
        wcount = Counter(words)
        uniques = list(wcount.keys())
        n = len(uniques)
        idx = qs(n-k,0,n-1)
        ans = []
        d = defaultdict(set)
        minfreq = float("inf")
        for i in range(idx,n):
            d[wcount[uniques[i]]].add(uniques[i])
            minfreq = min(minfreq,wcount[uniques[i]])
        for key,v in wcount.items():
            if v==minfreq:
                d[v].add(key)
        for key in sorted(d.keys(),reverse=True):
            if k-len(d[key]) < 0:
                ans.extend(sorted(d[key])[:k])
            else:
                ans.extend(sorted(d[key]))
            k -= len(d[key])
        return ans

s = Solution()
# print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
# print(s.topKFrequent(["a","aa","aaa"],1))
# print(s.topKFrequent(["i","love","leetcode","i","love","coding"],1))
print(s.topKFrequent(["c","a","c","e","d","d","b","b","b","d","c","c","d","b"],1))