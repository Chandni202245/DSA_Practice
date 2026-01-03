# Brute Force
"""def searchInRotatedArray(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1

nums=[17,18,20,13,1,2,3,4,8]
target=20
print(searchInRotatedArray(nums,target))"""

# TC-> O(N)
# SC-> O(1)

# Optimal Solution
def SearchInRotatedArray(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1

nums=[17,18,20,1,2,4,5,7,8,10,11,13,14,16]
target=8
print(SearchInRotatedArray(nums,target))

# TC-> O(log n)
# SC-> O(1)


