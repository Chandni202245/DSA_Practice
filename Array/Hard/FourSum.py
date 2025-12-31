# Brute Force
"""def FourSum(nums,target):
    n=len(nums)
    if n<4:
        return []
    my_set=set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    result=[]
    for ans in my_set:
        result.append(list(ans))
    return result

nums=[1,0,-1,0,-2,2,5,9]
target=0
print(FourSum(nums,target))"""

# TC-> O(N^4)
# SC-> O(N)

# Better
"""def FourSum(nums, target):
    n = len(nums)
    my_set = set()

    for i in range(n):
        for j in range(i+1, n):
            hash_set = set()
            for k in range(j+1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])

                if fourth in hash_set:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    my_set.add(tuple(temp))   # ✅ use add()

                hash_set.add(nums[k])        # ✅ inside loop

    result = []
    for ans in my_set:
        result.append(list(ans))

    return result    # ✅ return result

nums = [1,0,-1,5,-2,2,0,9]
target = 0
print(FourSum(nums, target))"""

# TC-> O(N^3)
# SC-> O(N)

# Optimal Solution
def FourSum(nums, target):
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    # skip duplicates
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1

                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans

nums = [1,0,-1,5,-2,2,0,9]
target = 13
print(FourSum(nums, target))