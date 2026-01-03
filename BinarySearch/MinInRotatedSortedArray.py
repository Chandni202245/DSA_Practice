# Brute Force
"""def MiniRotatedSortedArray(nums):
    n=len(nums)
    mini=float("inf")
    for i in range(0,n):
        mini=min(mini,nums[i])
    return mini
nums=[7,8,9,1,2,3,4]
print(MiniRotatedSortedArray(nums))"""

# TC-> O(N)
# SC-> O(1)


# Optimal Solution
def MiniRotatedSortedArray(nums):
    n=len(nums)
    low=0
    high=n-1
    mini=float("inf")
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]:
            mini=min(nums[mid],mini)
            high=mid-1
        else:
            mini=min(nums[low],mini)
            low=mid+1
    return mini

nums=[7,8,9,1,2,3,4]
print(MiniRotatedSortedArray(nums))

# TC->O(log n)
# SC-> O(1)