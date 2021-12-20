from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def sortBasedOnStartTime():
            st,et,pf=zip(*sorted(zip(startTime,endTime,profit)))
            return st,et,pf
        def binarySearch(arr,x):# find first index with elem at least x
            if arr[0]>=x:
                return 0

            l,r=0,len(arr)-1
            while l<=r:
                m=(l+r)//2

                if arr[m]>=x:
                    r=m-1
                    continue

                if m+1>=len(arr):
                    return -1

                if arr[m+1]>=x:
                    return m+1

                l=m+1
            return -1
        st,et,pf=sortBasedOnStartTime()
        n=len(startTime)
        maxpf = [0]*n # can interpret as max profit if start working at this point, an non decreasing array
        maxpf[-1] = pf[-1]

        for i in range(n-2,-1,-1):
            nextidx=binarySearch(st,et[i])
            nextpf=0 if nextidx<0 else maxpf[nextidx]
            maxpf[i]=pf[i]+nextpf if pf[i]+nextpf>maxpf[i+1] else maxpf[i+1]
        return maxpf[0]

s = Solution()
st = [5]
et = [10]
profit = [1]
assert s.jobScheduling(st,et,profit)==1

st = [5,10]
et = [10,15]
profit = [1,2]
assert s.jobScheduling(st,et,profit)==3

st = [5,6]
et = [10,8]
profit = [1,2]
assert s.jobScheduling(st,et,profit)==2

st = [5,8]
et = [10,13]
profit = [1,1]
assert s.jobScheduling(st,et,profit)==1

st = [5,8]
et = [10,13]
profit = [1,10]
assert s.jobScheduling(st,et,profit)==10

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(s.jobScheduling(startTime,endTime,profit))

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(s.jobScheduling(startTime,endTime,profit))
"""
1. enumeration, but how?
Does any interview question actually use enumeration?

2. DP
decide whether to take each job.
max profit = max(not take this job's profit, take this job's profit)
Take this job or not changes next possible job
Problem: find jobs that start time satisfy restriction
i) sort jobs based on start time
2) binary search on start time to find non conflicting jobs
3) max profit start on last job

3. Graph
i) next state(s): start time bigger than current end time, but no bigger than another event's end time whose start time is also bigger than current end time
construction:
end state, connect all jobs that cannot start any job after itself to it (depends on end time)
connect job that can start any of the above job with no disjoint job in between...wait, that's too much
ii) next states(s): all job starts later
this is acylic graph
shortest path (negative profit on edge)?
V:n, E: O(n^2)
shortest path will take O(V+E)=O(n^2)
"""

"""
concise binary search in python
https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/918804/Python-Top-Down-and-Bottom-Up-DP-7-lines-each
def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:

	n = len(start)
	start, end, profit = zip(*sorted(zip(start, end, profit)))
	jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)}

	dp = [0 for _ in range(n+1)]
	for i in range(n-1, -1, -1):
		dp[i] = max(dp[i+1], profit[i] + dp[jump[i]])

	return dp[0]
"""