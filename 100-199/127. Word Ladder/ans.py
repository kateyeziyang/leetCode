from typing import List
import heapq
from collections import defaultdict, deque

"""
try bidirectional BFS!!
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isConnected(a,b):
            diff = False
            for i in range(len(a)):
                if a[i]!=b[i]:
                    if diff:
                        return -1 # not connected
                    else:
                        diff = True
            if diff: return 0 # connected
            return 1 # same
        nodes = {}
        for word in wordList:
            nodes[word] = []
            for node in nodes:
                if isConnected(word,node)==0:
                    nodes[node].append(word)
                    nodes[word].append(node)
        if beginWord not in nodes:
            nodes[beginWord]=[]
            for word in wordList:
                if isConnected(beginWord,word)==0:
                    nodes[beginWord].append(word)
        q = deque([beginWord])
        ans = 1
        visited = {beginWord}
        while q:
            ans += 1

            for i in range(len(q)):
                node = q.popleft()
                for nb in nodes[node]:
                    if nb == endWord:
                        return ans
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
        return 0

s = Solution()
assert s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])==5