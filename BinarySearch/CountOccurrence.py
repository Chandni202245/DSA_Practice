# Brute Force
"""def CountOccurrence(nums,target):
    n=len(nums)
    first=-1
    last=-1
    for i in range(0,n):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i
    if first==-1:
        return 0
    return (last-first+1)

nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3
print(CountOccurrence(nums,target))"""

# TC-> O(N)
# SC-> O(1)

# Optimal Solution

def lowerBound(nums, target):
    n = len(nums)
    lb = n
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb


def upperBound(nums, target):
    n = len(nums)
    ub = n
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub


def CountOccurrence(nums, target):
    n = len(nums)
    if n == 0:
        return 0

    lb = lowerBound(nums, target)
    if lb == n or nums[lb] != target:
        return 0

    ub = upperBound(nums, target)
    return ub - lb

# TC-> O(log n)
# SC-> O(1)