from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def splitIntoRepeatChars(x):
            repeatedChar = x[0]
            count = 0
            res = []
            for c in x:
                if c != repeatedChar:
                    res.append([repeatedChar,count])
                    repeatedChar,count = c,1
                else:
                    count += 1
            res.append([repeatedChar,count])
            return res
        splittedS = splitIntoRepeatChars(s)
        ans = 0
        for w in words:
            splittedW = splitIntoRepeatChars(w)
            if len(splittedS) != len(splittedW):
                continue
            for i,j in zip(splittedS,splittedW):
                schar,scount = i[0],i[1]
                wchar,wcount = j[0],j[1]
                if schar != wchar:
                    break
                if wcount == scount:
                    continue
                if scount >= 3 and wcount <= scount:
                    continue
                break
            else:
                ans += 1
        return ans

s = Solution()
assert s.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"])==1
assert s.expressiveWords(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"])==3