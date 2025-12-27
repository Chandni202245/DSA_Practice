# Optimal solution
"""def rearranageArraySign(nums):
    n=len(nums)
    result=[0]*n
    pos_index=0
    neg_index=1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2
    return result

nums=[5,3,2,-1,-4,-6,10]
print(rearranageArraySign(nums))"""

# TC-> O(N)
# SC-> O(1) or O(N)

#Brute force

def rearranageArraySign(nums):
    n=len(nums)
    pos=[]
    neg=[]
    for i in range(0,n):
        if nums[i]>=0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    i = 0
    while i < len(pos) and i < len(neg):
        nums[2*i] = pos[i]
        nums[2*i + 1] = neg[i]
        i += 1

    return nums

nums=[2,3,4,-5,-6,-7,10]
print(rearranageArraySign(nums))

# TC-> O(N+N/2)
# SC-> O(N)