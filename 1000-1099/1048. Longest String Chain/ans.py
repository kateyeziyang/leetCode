from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        dp = defaultdict(int)
        lenLongestChain = 1

        for k in range(len(words)):
            w = words[k]
            lenLongestChainOfWord = 1
            for j in range(len(w)):
                preWord = w[:j]+w[j+1:]
                lenLongestChainOfWord = max(lenLongestChainOfWord, dp[preWord]+1)
            dp[w] = lenLongestChainOfWord
            lenLongestChain = max(lenLongestChain, lenLongestChainOfWord)
        return lenLongestChain


s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))