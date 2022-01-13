from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def kthidx(l,r,k):
            # find a pivot
            pidx = (l+r)//2
            pivot = freqs[pidx]
            # [:left] will be freq < pivot
            left = l
            # first place pivot at the end
            freqs[r],freqs[pidx] = freqs[pidx],freqs[r]
            for i in range(l,r):
                if freqs[i][1]<pivot[1]: # when encounter smaller, swap to left position
                    freqs[i],freqs[left] = freqs[left],freqs[i]
                    left += 1
            # swap left(start of bigger part) and pivot to finish the job
            freqs[left],freqs[r] = freqs[r],freqs[left]
            # l..r-k, r-k+1..r
            # l..left-1,left..r
            if left==r-k+1:
                return left
            elif left < r-k+1:
                return kthidx(left+1,r,k)
            else:
                return kthidx(l,left-1,k-(r-left+1))

        numCounts = Counter(nums)
        freqs = list(numCounts.items())
        n = len(freqs)
        idx = kthidx(0,n-1,k)
        ans = [f[0] for f in freqs[idx:]]

        return ans

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(s.topKFrequent([1,1,1,2,2,3,5,5,5,5,-1,3,2,-1,4,4,4,4,4],2))
print(s.topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0],6))