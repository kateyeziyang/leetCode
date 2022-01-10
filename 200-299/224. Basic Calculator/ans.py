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
        # st = deque()
        # num = []
        # def cleanStack():
        #     nonlocal st
        #     val = count = 0
        #     while st and st[-1]!="(":
        #         word = st.pop()
        #         if word=="+":
        #             count += val
        #             val = 0
        #         elif word=="-":
        #             count -= val
        #             val = 0
        #         else:
        #             val = word
        #     count += val
        #     if st:
        #         st.pop()
        #     st.append(count)
        # for i,c in enumerate(s):
        #     if c==" ": continue
        #     if c.isnumeric():
        #         num.append(c)
        #         continue
        #     if num:
        #         st.append(int("".join(num)))
        #         num = []
        #     if c != ")":
        #         st.append(c)
        #         continue
        #     cleanStack()
        # if num:
        #     st.append(int("".join(num)))
        # cleanStack()
        # return st[0]

s = Solution()
assert s.calculate(s = "1 + 1")==2
assert s.calculate(s = " 2-1 + 2 ")==3
assert s.calculate("(1+(4+5+2)-3)+(6+8)")==23