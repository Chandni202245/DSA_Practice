def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap==False:
            break
       
nums=[5,8,1,6,9,2,4]
bubble_sort(nums)
print(nums)

# Time complexity -> best case - O(n)
                #   -> worst case - O(n^2)  without using is_swap