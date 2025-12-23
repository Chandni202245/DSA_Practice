 # Right Rotate an array by one place
nums=[5,-2,3,9,0,6,10,7]
n=len(nums)
print(nums)
# nums[:]= [nums[n-1]]+ nums[0:n-1]
# print("Right Rotate an array by one place: ",nums)


# Left Rotate an array
nums[:]=nums[1:]+nums[:1]
print("left rotate: ",nums)

"""def reverse(nums, left, right):
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

print(nums)"""
