from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# class Solution:
#     def makeGood(self, s: str) -> str:
#         i = 0
#         while i <= len(s)-2:
#             if (s[i].islower() and s[i].upper() == s[i+1]) or (s[i].isupper() and s[i].lower() == s[i+1]):
#                 s = s[:i] + s[i+2:]
#                 if i > 0: i -= 1
#             else:
#                 i += 1
#         return s

class Solution:
    def makeGood(self, s: str) -> str:
        if s == '': return s

        stringBuffer = [' '] * len(s)
        stringBuffer[0] = s[0]
        l = 0
        i = 1
        while i < len(s):
            if (l != -1) and (abs(ord(stringBuffer[l]) - ord(s[i])) == 32):
                l -= 1
            else:
                l += 1
                stringBuffer[l] = s[i]
            i += 1
        return ''.join(stringBuffer[:l+1])
    # last char


s = Solution()
t = ['','a','abcdef','aaaaaa','AaaA','AaAa','AAAA','AAAa','aaaA','AbBcCcCa']
for tc in t:
    print(s.makeGood(tc))