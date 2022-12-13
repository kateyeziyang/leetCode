from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from itertools import chain

# first asssign result, then words: if when evaludating words, already bigger, stop
# class Solution:
#     def isSolvable(self, words: List[str], result: str) -> bool:
#         noZeros = set()
#         def transform(s, multipliers={}):
#             if len(s)>1:
#                 noZeros.add(s[0])
#             pow = 1
#             for i in range(len(s)-1,-1,-1):
#                 multipliers[s[i]] += pow
#                 pow *= 10

#         def ev(multipliers, limit=float('inf')):
#             res = 0
#             for k,v in multipliers.items():
#                 res += mappings[k] * v
#                 if res>limit:
#                     return res
#             return res

#         def bt1(i):            
#             if i != len(rKeys):
#                 curChar = rKeys[i]
#                 toUse = list(usables) if curChar not in noZeros else list(usables-set([0]))
#                 for digit in toUse:
#                     mappings[curChar] = digit
#                     usables.remove(digit)
#                     if bt1(i+1):
#                         return True
#                     usables.add(digit)
#                 return False
#             rVal = ev(rMultipliers)
#             tmp = wSum
#             for k in wKeys:
#                 if k in rMultipliers:
#                     rVal -= mappings[k]*wMultipliers[k]
#                     tmp -= wMultipliers[k]

#             return bt2(0, rVal, tmp)

#         def bt2(i, target, wSum):
#             if i != len(wKeys):
#                 curChar = wKeys[i]
#                 if curChar in rMultipliers:
#                     return bt2(i+1, target, wSum)
#                 toUse = list(usables) if curChar not in noZeros else list(usables-set([0]))
#                 if not toUse or max(toUse)*wSum < target: return False
#                 if min(toUse)*wSum > target: return False
#                 multiplier = wMultipliers[curChar]
#                 wSum -= multiplier

#                 for digit in toUse:
#                     # if target==10652 and curChar=='D' and digit==7:
#                     #     ccc = ''
#                     mappings[curChar] = digit
#                     usables.remove(digit)
#                     if bt2(i+1, target-digit*multiplier, wSum):
#                         return True
#                     usables.add(digit)
#                 return False
#             return target==0

#         usables = set([0,1,2,3,4,5,6,7,8,9])
#         rMultipliers = defaultdict(int)
#         transform(result, rMultipliers)
#         wMultipliers = defaultdict(int)
#         for w in words:
#             transform(w, wMultipliers)

#         rSum = sum(rMultipliers.values())
#         wSum = sum(wMultipliers.values())
#         if rSum > 10*wSum or 10*rSum < wSum:
#             return False

#         rKeys = list(rMultipliers.keys())
#         wKeys = list(wMultipliers.keys())
#         mappings = {}
        
#         return bt1(0)
        
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        mappings = {}
        nonZeroMappings = set()
        for w in words+[result]:
            nonZeroMappings.add(w[0])
            mappings.update(zip(w, [None]*len(w)))
        digits = set(range(10))
        keyLetters = ''.join(mappings.keys())

        multipliers = defaultdict(int)
        resultMultipliers = defaultdict(int)
        for w in words:
            pow = 1
            for c in w:
                multipliers[c] += pow
                pow *= 10
        pow = 1
        for c in result:
            resultMultipliers[c] += pow
            pow *= 10

        def evaluate():
            return sum(v*mappings[k] for k,v in multipliers.items()) == sum(v*mappings[k] for k,v in resultMultipliers.items())
        def backtracking(i):
            if i==len(keyLetters):
                return evaluate()
            k = keyLetters[i]
            for digit in tuple(digits if k not in nonZeroMappings else digits-set([0])):
                mappings[k] = digit
                digits.remove(digit)
                if backtracking(i+1):
                    return True
                digits.add(digit)
            return False
        
        # return backtracking(0)
        ans = backtracking(0)
        print(mappings)
        return ans
        
# https://leetcode.com/problems/verbal-arithmetic-puzzle/solutions/463921/python-backtracking-with-pruning-tricks/?orderBy=most_votes
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        allWords = words + [result]
        firstChars = set(word[0] for word in allWords if len(word)>1)
        n = max(len(w)
        
        
         for w in allWords)
        if len(result)<n: return False

        def dfs(charIdx,wordIdx,carry,visited,char2digit):
            if charIdx==n: return carry==0
            if wordIdx==len(allWords):
                sums = sum(char2digit[word[-charIdx-1]] if charIdx<len(word) else 0 for word in words)+carry
                if sums%10 == char2digit[result[-charIdx-1]]:
                    return dfs(charIdx+1,0,sums//10,visited,char2digit)
                else:
                    return False
            if wordIdx<len(words) and charIdx>=len(words[wordIdx]):
                return dfs(charIdx,wordIdx+1,carry,visited,char2digit)
            
            c = allWords[wordIdx][-charIdx-1]
            if c in char2digit:
                return dfs(charIdx,wordIdx+1,carry,visited,char2digit)
            else:
                firstDigit=1 if c in firstChars else 0
                for digit in range(firstDigit,10):
                    if digit not in visited:
                        visited.add(digit)
                        char2digit[c]=digit
                        if dfs(charIdx,wordIdx+1,carry,visited,char2digit.copy()): return True
                        visited.remove(digit)
                return False

        return dfs(0,0,0,set(),{})

s = Solution()
# print(s.isSolvable(["LEET","CODE"],"POINT"))
print(s.isSolvable(["SEND","MORE"],"MONEY"))
# print(s.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
# print(s.isSolvable(["THIS","IS","TOO"],"FUNNY"))
# print(s.isSolvable(
# ["GEMINI","VIRGO"],"CANCER"))