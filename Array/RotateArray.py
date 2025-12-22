def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


nums = [3, 9, 5, 6, 7, 2, 10, 9]
n = len(nums)
k = 5

k = k % n   # handles k > n cases

# Step 1: reverse whole array
reverse(nums, 0, n - 1)

# Step 2: reverse first k elements
reverse(nums, 0, k - 1)

# Step 3: reverse remaining elements
reverse(nums, k, n - 1)

print(nums)
