from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# if there aren't brackets inside brackets, simply split by "]"
# Since there is... Use stack
# if see left bracket, store letter process stack until finish last right brackt
# if see num/letter, store to current
# if see right bracket, store num and start letter

class Solution:
    def decodeString(self, s: str) -> str:
        def process():
            s = ""
            while type(st[-1]) is str:
                s = st.pop()+s
            times = st.pop()
            st.append(s*times)
        cur = ""
        st = deque()
        for i,c in enumerate(s):
            if c=="]":
                st.append(cur)
                cur = ""
                process()
            elif c=="[":
                st.append(int(cur))
                # st.append("[")
                cur = ""
            else:
                if cur and cur[-1].isdigit()!=c.isdigit():
                    st.append(cur)
                    cur = ""
                cur += c
        if cur:
            st.append(cur)
        return "".join(list(st))

s = Solution()
print(s.decodeString("3[a2[c]]"))