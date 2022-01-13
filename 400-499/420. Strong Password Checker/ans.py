from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        n = len(password)
        steps = 0
        c,count = password[0],0
        hasReqs = [0]*3
        minusQuota = max(0,n-20)
        addQuota = max(0,6-n)
        for letter in password:
            if letter.isalpha():
                if letter.islower():
                    hasReqs[0] = 1
                else:
                    hasReqs[1] = 1
            elif letter.isdigit():
                hasReqs[2] = 1
        ChangeQuota = 3-sum(hasReqs)
        if addQuota:
            ChangeQuota = max(addQuota,ChangeQuota)
        steps += ChangeQuota+minusQuota
        for i,letter in enumerate(password):
            if letter==c:
                count += 1
                if count==3:
                    if minusQuota:
                        count -= 1
                        minusQuota -= 1
                    else:
                        steps += 1
                        if ChangeQuota:
                            steps -= 1
                            ChangeQuota -= 1
                        c,count = "",0
            else:
                c,count = letter,1
        return steps

s = Solution()
s.strongPasswordChecker(
"bbaaaaaaaaaaaaaaacccccc")