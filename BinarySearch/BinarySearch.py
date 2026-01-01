def binarySearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

nums=[2,3,5,6,8,9,10]
target=9
print(binarySearch(nums,target))

# TC-> O(log N)
# SC-> O(1)