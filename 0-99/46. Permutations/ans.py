import enum
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first==n:
                output.append(nums.copy())
            else:
                for i in range(first, n):
                    nums[i], nums[first] = nums[first], nums[i]
                    backtrack(first+1)
                    nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        output = []
        backtrack()
        return output
    
    # def recursion(self, i, buf):
    #     if i==self.n-1:
    #         self.result.append(buf)
    #         return

    #     self.recursion(i+1, buf)
    #     for j in range(i+1, self.n):
    #         new_buf = buf.copy()
    #         new_buf[i], new_buf[j] = new_buf[j], new_buf[i]
    #         self.recursion(i+1, new_buf)


s = Solution()
print(s.permute([1,2,3]))