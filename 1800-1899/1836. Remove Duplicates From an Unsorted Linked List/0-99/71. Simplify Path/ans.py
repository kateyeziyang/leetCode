from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = [""]
        parts = path.split("/")
        for part in parts:
            if part:
                if part==".":
                    continue
                elif part=="..":
                    if ans[-1]:
                        ans.pop()
                else:
                    ans.append(part)
        if len(ans)==1:
            return "/"
        return "/".join(ans)

s = Solution()
s.simplifyPath("/home/")