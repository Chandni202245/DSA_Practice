# Find the maximum SubArray sum
"""def maxSubArray(arr):
    n=len(arr)
    maxi=float("-inf")
    for i in range(0,n):
        total=0
        for j in range(i,n):
            total=total+arr[j]
            maxi=max(maxi,total)
    return maxi

arr=[-3,1,4,0,-2,6,-3,4,-5]
print("Maximum sub array sum is",maxSubArray(arr))"""

# TC-> O(n^2)
# SC-> O(1)

# Optimal Solution

def maxSubArray(nums):
    n=len(nums)
    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi

nums=[-3,1,4,0,-2,6,-3,4,-5]
print("Maximum sub array sum is",maxSubArray(nums))

# TC-> O(N)
# SC-> O(1)