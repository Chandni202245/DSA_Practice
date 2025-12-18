def func(nums):
    largest = float('-inf')
    for i in range(len(nums)):
        largest = max(largest, nums[i])
    return largest

nums = [12,34,26,23,10,45,78,90]
print(func(nums))
