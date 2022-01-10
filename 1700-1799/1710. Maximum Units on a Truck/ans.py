from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedTypes = sorted(boxTypes,key=lambda x:x[1],reverse=True)
        ans = 0
        for numBoxes,numUnits in sortedTypes:
            numLoaded = numBoxes if truckSize >= numBoxes else truckSize
            ans += numLoaded * numUnits
            truckSize -= numLoaded
            if not truckSize:
                break
        return ans

s = Solution()
assert s.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)==91