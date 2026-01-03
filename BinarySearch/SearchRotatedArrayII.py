def SearchInRotatedArrayII(nums,target):
    n=len(nums)
    high=n-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
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
    return False

nums=[7,7,7,7,7,7,7,1,2,4,5,6,7,7]
target=3
print(SearchInRotatedArrayII(nums,target))

# Time Complexity
# Average case: O(log n)
# Worst case (all duplicates): O(n)    Due to duplicate elements, worst-case time complexity degrades to O(n).

# SC-> O(1)