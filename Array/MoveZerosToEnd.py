# Brute approach 
"""def moveZerosAtEnd(nums):
    n=len(nums)
    temp=[]
    for i in range(0,n):
        if nums[i]!=0:
            temp.append(nums[i])
    n2=len(temp)
    for i in range(0,n2):
        nums[i]=temp[i]
    for i in range(n2,n):
        nums[i]=0
    return nums
nums=[1,0,2,4,3,0,0,3,5,1]
print(moveZerosAtEnd(nums))
"""


# Optimal solution

def moveZerosAtEnd(nums):
    n = len(nums)
    i = 0

    if n == 1:
        return nums

    # find first zero
    while i < n:
        if nums[i] == 0:
            break
        i += 1

    if i == n:  # no zeros found
        return nums

    j = i + 1  
    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return nums


nums = [1,0,2,4,3,0,0,3,5,1]
print(moveZerosAtEnd(nums))
