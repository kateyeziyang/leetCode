from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[-1] = True
        maxwordlen = float("-inf")
        for w in wordDict:
            if s[-len(w):]==w:
                dp[-len(w)-1]=True
            maxwordlen = max(maxwordlen,len(w))
        for i in range(n-1,-1,-1):
            for w in wordDict:
                dp[i] = i+len(w)<=n and dp[i+len(w)] and s[i:i+len(w)]==w
                if dp[i]: break
        return dp[0]


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         visited = {0}
#         q = deque([0])

#         while q:
#             node = q.popleft()

#             for w in wordDict:
#                 if node+len(w) not in visited and s[node:node+len(w)]==w:
#                     if node+len(w)==len(s):
#                         return True
#                     visited.add(node+len(w))
#                     q.append(node+len(w))
#         return False


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         trie = {}
#         for w in wordDict:
#             p = trie
#             for c in w:
#                 p = p.setdefault(c,{})
#             p["#"] = True
#         q = deque([trie])
#         for c in s:
#             if not q: return False

#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if c in node:
#                     q.append(node[c])
#                 if "#" in node and c in trie:
#                     q.append(trie[c])
#         if not q: return False
#         for _ in range(len(q)):
#             node = q.popleft()
#             if "#" in node:
#                 return True
#         return False

s = Solution()
# assert s.wordBreak(s = "leetcode", wordDict = ["leet","code"])==True
# assert s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])==True
assert s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])==False
assert s.wordBreak("abcd",["a","abc","b","cd"])==True
assert s.wordBreak("aaaaaaa",["aaaa","aa"])==False