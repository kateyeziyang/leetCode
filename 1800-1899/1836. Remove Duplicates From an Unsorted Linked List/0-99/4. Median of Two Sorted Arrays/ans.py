from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m > n:
            nums1,nums2,m,n = nums2,nums1,n,m
        
        imin,imax,half = 0,m,(m+n+1)//2
        while imin<=imax:
            i = (imin+imax)//2
            j = half-i
            if i<m and nums2[j-1]>nums1[i]:
                imin = i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax = i-1
            else:
                if i==0:
                    maxl = nums2[j-1]
                elif j==0:
                    maxl = nums1[i-1]
                else:
                    maxl = max(nums1[i-1],nums2[j-1])
                if (m+n)%2==1:
                    return maxl
                if i==m:
                    minr = nums2[j]
                elif j==n:
                    minr = nums1[i]
                else:
                    minr = min(nums1[i],nums2[j])
                return (maxl+minr)//2

class Solution:
    # m, n >= 0, m+n >= 1
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 or len(nums2)==0:# this condition ensures half will be positive, and m2 be at least -1
            nums = nums1 if len(nums2)==0 else nums2
            m=(len(nums)-1)//2
            if len(nums)%2==0:
                return (nums[m]+nums[m+1])/2
            else:
                return nums[m]
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total = len(nums1)+len(nums2)
        half = total // 2

        l,r = 0, len(nums1)-1
        while True:
            m1 = (l+r)//2 # will be last elem in left partition of nums1
            m2 = half-(m1+1)-1 # half is number of elements, m1+1 is number of elems in nums1's left partition, -1 is for index

            a = nums1[m1] if m1 >= 0 else float("-inf") # m1 can be -1, in case no element in nums1's left partition
            b = nums1[m1+1] if m1+1 < len(nums1) else float("inf")
            c = nums2[m2] if m2 >= 0 else float("-inf")
            d = nums2[m2+1] if m2+1 < len(nums2) else float("inf")

            if a<=d and c<=b:
                if total%2!=0: # total=half+(1+half)
                    return min(b,d)
                else: # total=half+half
                    return (max(a,c)+min(b,d))/2
            elif a>d:
                r=m1-1
            else:
                l=m1+1

s = Solution()
x=[1]
y=[3]
print(s.findMedianSortedArrays(x,y))

x=[3]
y=[1]
print(s.findMedianSortedArrays(x,y))

x=[1,3]
y=[4,5]
print(s.findMedianSortedArrays(x,y))

x=[4,5]
y=[1,3]
print(s.findMedianSortedArrays(x,y))

x=[3]
y=[1,2,4,5]
print(s.findMedianSortedArrays(x,y))

x=[1,2]
y=[1,3,3]
print(s.findMedianSortedArrays(x,y))

x=[1,2,3]
y=[0,1,4,5]
print(s.findMedianSortedArrays(x,y))

"""
The median can partition an array into two equal parts.
To find the median of two sorted arrays, we need to partition each of the two arrays. 
In each array, the left partition should be part of the left partition of the merged array, and similarly for the right partition.
Notice that if we find the correct partition for one array, the other array's partition can be carried out easily.
So we will focus on finding the correct partition for the shorter array.

We try to find the partition like doing a binary search.
Initially, l and r will be 0 and len(shorter)-1. The median number in this range will be the first number to try as the partition for shorter.
We then find longer's partition number. We compare if nums in left partition of shorter is all less than nums in right partition of longer, and if left partition
of longer is all less than nums in right partition of shorter.
If it is so, then the partition is found correctly.
Otherwise:
1. nums in left partition of shorter contains nums bigger than right partition of longer:
    the correct partition must be in the currect left partition of shorter. Update that.
2. nums in left partition of longer contains nums bigger than right partition of short:
    the correct partition must be in the currect right partition of shorter. Update that.
In each iteration the searched ranged is about the half of before. So it's similar to binary search and get O(log(min(m,n)))

A few things to deal with:
median method for odd length and even length array
"""