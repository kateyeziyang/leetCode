from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def calculate(self, s: str) -> int:
        st = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = operand*10+int(ch)
            elif ch == "+":
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                st.append(res)
                st.append(sign)
                sign = 1
                res = 0
            elif ch == ")":
                res += sign * operand
                res *= st.pop()
                res += st.pop()
                operand = 0
        return res+sign*operand

s = Solution()
assert s.calculate(s = "1 + 1")==2
assert s.calculate(s = " 2-1 + 2 ")==3
assert s.calculate("(1+(4+5+2)-3)+(6+8)")==23


def solution(s):
    sign = 1
    operand = 0
    stack = []
    result = 0

    for c in s:
        if c == ' ': continue
        if c == '(': # prev: '(' or '+' or '-'
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif c == ')': # prev: ')' or number
            result += operand * sign
            result *= stack.pop()
            result += stack.pop()
            operand = 0
        elif c in {'+','-'}:
            result += operand * sign
            sign = 1 if c == '+' else -1
            operand = 0
        else: # number
            operand = operand * 10 + int(c)
    
    return result + operand * sign
