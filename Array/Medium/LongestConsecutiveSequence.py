# Brute force
"""def longestConsecutiveSequence(nums):
    n=len(nums)
    max_count=0
    for i in range(0,n):
        num=nums[i]
        count=1
        while num+1 in nums:
            count+=1
            num=num+1
        max_count=max(max_count,count)
    return max_count

nums=[1,99,100,98,2,5,3,100,1,101]
print(longestConsecutiveSequence(nums))"""

# TC-> O(N^2)
# SC-> O(1)


"""def longestConsecutiveSequence(nums):
    n=len(nums)
    nums.sort()
    count=0
    last_smaller=float("-inf")
    longest=0
    for i in range(0,n):
        num=nums[i]
        if num-1==last_smaller:
            count+=1
            last_smaller=num
        elif num!=last_smaller:
            count=1
            last_smaller=num
        longest=max(longest,count)
    return longest

nums=[1,5,3,99,100,2,101,1,1,98]
print(longestConsecutiveSequence(nums))"""

# TC-> O(n log n + n)
# SC-> O(1)

def longestConsecutiveSequence(nums):
    n=len(nums)
    my_set=set()
    for i in range(0,n):
        my_set.add(nums[i])
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)
    return longest

nums=[1,5,3,99,100,2,101,1,1,98]
print("The longest consecutive sequence is:",longestConsecutiveSequence(nums))

# TC-> O(N+N+N) = O(N)
# SC-> O(N)