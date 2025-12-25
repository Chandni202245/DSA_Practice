def findMissingNumber(nums):
    n = len(nums)
    xor_all = 0
    for i in range(1, n + 2):
        xor_all=xor_all^i
    for num in nums:
        xor_all=xor_all^num
    return xor_all
nums = [1, 2, 4, 3, 5, 6,8]
print(findMissingNumber(nums))

# TC-> O(n) , SC-> O(1)
