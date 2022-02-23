import enum
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and (suffix in d or dfs(suffix)):
                    memo[word] = True
                    break
                
        return ans

# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         words.sort(key=lambda x:len(x))
#         ans = []
#         visited = {}
#         for i,w in enumerate(words):
#             q = deque([0])
#             seen = set()
#             shouldBreak = False
#             while q:
#                 l = q.pop()
#                 for j in range(i):
#                     word = words[j]
#                     r = l+len(word)
#                     if r > len(w):
#                         break
#                     if r not in seen and w[l:r]==word:
#                         if r==len(w):
#                             ans.append(w)
#                             shouldBreak = True
#                             break
#                         seen.add(r)
#                         q.append(r)
#                 if shouldBreak:
#                     break
#         return ans

s = Solution()
print(s.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))