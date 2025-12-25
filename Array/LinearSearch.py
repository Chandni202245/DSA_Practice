def linearSearch(nums,target):
    for i in range(0,len(nums)):
        if nums[i]== target:
            return i
    return -1

nums=[5,3,9,8,1,6,-10,-100]
target=8
print("The target element is present at",linearSearch(nums,target),"this index")