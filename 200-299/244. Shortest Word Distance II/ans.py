from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# two word can have multiple instances in dictionary
# find the closest two points between two set of numbers
# word1: 1 2 7 9 16
# word2: 3 10
# 3-1,3-2,7-3,10-7,10-9,16-10
# two pointer? o(n)
# repeated calls?
# I generate almost same code to the solution but very slow, why?????
# 2nd run faster than 81% .....

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsMap = defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.wordsMap[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")
        l1,l2 = self.wordsMap[word1],self.wordsMap[word2]
        i,j = 0,0
        while i<len(l1) and j<len(l2):
            if l1[i] >= l2[j]: # not possible to be equal
                res = min(res,l1[i]-l2[j])
                j += 1
            else:
                res = min(res,l2[j]-l1[i])
                i += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)