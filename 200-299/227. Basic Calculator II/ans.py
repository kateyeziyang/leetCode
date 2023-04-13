import itertools
import operator
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# + -: can conclude previous calculation, add to sum
# * /: store current number, don't add to sum yet
# ' '

class Solution:
    def calculate(self, s: str) -> int:
        ops = {'+': operator.add, '-': operator.add, '*': operator.mul, '/': operator.floordiv}

        totalSum = 0
        ongoingSum = 0
        sign = 1
        num = 0

        op = operator.add

        for c in itertools.chain(s+'+0'):
            if c == ' ':
                continue
            if c.isnumeric():
                num = num * 10 + int(c)
                continue
            
            if c in {'+', '-'}: # add ongoingsum to total
                totalSum += op(ongoingSum, num)*sign
                ongoingSum = 0
                sign = 1 if c=='+' else -1
            else: # * /
                ongoingSum = op(ongoingSum, num)
            num = 0
            op = ops[c]
    
        return totalSum

# finally, I found out in java -3/2 = (-3)/2 = -1
# but in python, -3/2 = (-3)/2 = -2

f = Solution().calculate
assert f('5')==5
assert f('111')==111
assert f('5+111')==116
assert f(' 5  /1')==5
assert f('100*23 -6')==2294
assert f('100*23 -6/2* 2+7')==2301
assert f('100*23 -6/2* 2+10*5*10')==2794
assert f("14-3/2")==13