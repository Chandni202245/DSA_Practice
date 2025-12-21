def secondLargest(nums):
    sec_largest=float('-inf')
    largest=float('-inf')
    for i in range(0,len(nums)):
        if nums[i]>largest:
            sec_largest=largest
            largest=nums[i]
        elif nums[i]>sec_largest and nums[i]!=largest:
            sec_largest=nums[i]
    return sec_largest

nums=[22,24,67,45,30,10,30]
print("Second largest element in an array is: ",secondLargest(nums))

# Time Complexity: O(n)
# (Single pass through the array)

# Space Complexity: O(1)
# (Only two variables used)