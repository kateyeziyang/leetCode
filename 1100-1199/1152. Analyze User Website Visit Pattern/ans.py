from msilib import type_string
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user,time,site in sorted(zip(username,timestamp,website),key = lambda x: (x[0],x[1])):
            users[user].append(site)
        patterns = Counter()
        for user,sites in users.items():
            patterns.update(Counter(set(combinations(sites,3))))
        return max(sorted(patterns),key=patterns.get)

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        username,timestamp,website = zip(*sorted(zip(username,timestamp,website)))
        tree = {}
        visited = {}
        i = 0
        n = len(username)
        ans = []
        ansScore = float("-inf")
        while i<n:
            r = i
            cur = username[i]
            while r+1<n and username[r+1]==cur:
                r += 1
            for j in range(i,r+1):
                p = visited.setdefault(website[j],{})
                q = tree.setdefault(website[j],{})
                for k in range(j+1,r+1):
                    p2 = p.setdefault(website[k],{})
                    q2 = q.setdefault(website[k],defaultdict(int))
                    for l in range(k+1,r+1):
                        if website[l] not in p2:
                            p2[website[l]] = True
                            q2[website[l]] += 1
            i = r+1
            visited = {}
        q = deque([[tree,0,[]]])
        while q:
            node,level,pattern = q.popleft()
            for nb in node:
                newpattern = pattern+[nb]
                if level==2:
                    sc = node[nb]
                    if sc > ansScore:
                        ans,ansScore = newpattern,sc
                    elif sc == ansScore:
                        ans = min(ans,newpattern)
                    continue
                else:
                    q.append([node[nb],level+1,newpattern])
        return ans


s = Solution()
# print(s.mostVisitedPattern(username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]))
# print(s.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]))
# print(s.mostVisitedPattern(["dowg","dowg","dowg"],[158931262,562600350,148438945],["y","loedo","y"]))
# print(s.mostVisitedPattern(["zkiikgv","zkiikgv","zkiikgv","zkiikgv"],[436363475,710406388,386655081,797150921],["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]))
print(s.mostVisitedPattern(["lpgbr","by","by","lpgbr","by","ditctqnahs","by"],[117853717,760542754,858167998,235286033,992196098,273717872,792447849],["inc","inc","inc","ftd","inc","ftd","inc"]))