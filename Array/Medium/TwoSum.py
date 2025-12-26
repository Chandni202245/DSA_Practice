# Optimal solution
"""def twoSum(nums,target):
    n=len(nums)
    hash_map={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i

nums=[5,9,2,4,15,6,3]
target=13
print("The indexes of target element is:",twoSum(nums,target))"""
# Time Complexity: O(n)
# Space Complexity: O(n)



# Brute force
def twoSum(nums,target):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
            
nums=[5,9,2,4,15,6,3]
target=10
print("The indexes of target element is:",twoSum(nums,target))

# Time Complexity: O(n^2)
# Space Complexity: O(1)