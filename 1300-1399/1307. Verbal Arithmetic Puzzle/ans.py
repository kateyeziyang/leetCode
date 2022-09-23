from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from itertools import chain

# first asssign result, then words: if when evaludating words, already bigger, stop
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        noZeros = set()
        def transform(s, multipliers={}):
            if len(s)>1:
                noZeros.add(s[0])
            pow = 1
            for i in range(len(s)-1,-1,-1):
                multipliers[s[i]] += pow
                pow *= 10

        def ev(multipliers, limit=float('inf')):
            res = 0
            for k,v in multipliers.items():
                res += mappings[k] * v
                if res>limit:
                    return res
            return res

        def bt1(i):            
            if i != len(rKeys):
                curChar = rKeys[i]
                toUse = list(usables) if curChar not in noZeros else list(usables-set([0]))
                for digit in toUse:
                    mappings[curChar] = digit
                    usables.remove(digit)
                    if bt1(i+1):
                        return True
                    usables.add(digit)
                return False
            rVal = ev(rMultipliers)
            tmp = wSum
            for k in wKeys:
                if k in rMultipliers:
                    rVal -= mappings[k]*wMultipliers[k]
                    tmp -= wMultipliers[k]

            return bt2(0, rVal, tmp)

        def bt2(i, target, wSum):
            if i != len(wKeys):
                curChar = wKeys[i]
                if curChar in rMultipliers:
                    return bt2(i+1, target, wSum)
                toUse = list(usables) if curChar not in noZeros else list(usables-set([0]))
                if not toUse or max(toUse)*wSum < target: return False
                if min(toUse)*wSum > target: return False
                multiplier = wMultipliers[curChar]
                wSum -= multiplier

                for digit in toUse:
                    # if target==10652 and curChar=='D' and digit==7:
                    #     ccc = ''
                    mappings[curChar] = digit
                    usables.remove(digit)
                    if bt2(i+1, target-digit*multiplier, wSum):
                        return True
                    usables.add(digit)
                return False
            return target==0

        usables = set([0,1,2,3,4,5,6,7,8,9])
        rMultipliers = defaultdict(int)
        transform(result, rMultipliers)
        wMultipliers = defaultdict(int)
        for w in words:
            transform(w, wMultipliers)

        rSum = sum(rMultipliers.values())
        wSum = sum(wMultipliers.values())
        if rSum > 10*wSum or 10*rSum < wSum:
            return False

        rKeys = list(rMultipliers.keys())
        wKeys = list(wMultipliers.keys())
        mappings = {}
        
        return bt1(0)
        

s = Solution()
# print(s.isSolvable(["LEET","CODE"],"POINT"))
# print(s.isSolvable(["SEND","MORE"],"MONEY"))
# print(s.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
# print(s.isSolvable(["THIS","IS","TOO"],"FUNNY"))
print(s.isSolvable(
["GEMINI","VIRGO"],"CANCER"))