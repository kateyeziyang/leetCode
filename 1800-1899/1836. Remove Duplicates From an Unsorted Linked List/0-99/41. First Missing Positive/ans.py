from typing import List
from collections import defaultdict, deque

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        findOne = False
        for i in range(len(nums)):
            if nums[i]==1:
                findOne = True
                break
        if not findOne:
            return 1
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i] = 1
        nums.append(1)
        nums.append(1)
        n = len(nums) # n+2, indexed 0 ~ n+1
        for i in range(len(nums)):
            x = nums[i] if nums[i]>0 else -nums[i]
            if x <= n-1 and nums[x]>0:
                nums[x] = -nums[x] 
        for i in range(1,len(nums)):
            if nums[i] > 0:
                return i
        return -1

s = Solution()
print(s.firstMissingPositive(nums = [1,2,0]))
assert s.firstMissingPositive(nums = [1,2,0])==3
assert s.firstMissingPositive(nums = [3,4,-1,1])==2