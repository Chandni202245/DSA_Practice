def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j

def quick_sort(nums,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

nums=[4,1,7,6,3,2,8]
low=0
high=len(nums)-1
quick_sort(nums,low,high)
print(nums)

# Quick Sort is an in-place sorting algorithm, so it modifies the array directly instead of returning a new one.

# Best Case
# Pivot divides the array into two equal halves every time.
# Recursive depth ≈ log n
# 𝑂(𝑛 log 𝑛)

# Average Case
# Random pivot selection or random input.
# Partitions are reasonably balanced.
# 𝑂(𝑛 log 𝑛)

# Worst Case
# Pivot is always the smallest or largest element
# Happens when:
# Array is already sorted
# Array is reverse sorted
# Poor pivot choice (like always picking first element)
# O(n^2)​

# Auxiliary Space (Recursive Stack)
# Case	            Space Complexity
# Best/Average	    O(log n)
# Worst	            O(n)

# Reason:
# Quick Sort is in-place, no extra array used
# Space is consumed only by recursive function calls

# Quick Sort is an in-place, divide-and-conquer sorting algorithm with 
# average and best time complexity O(n log n) and worst-case O(n²). 
# Its space complexity is O(log n) due to recursion stack (O(n) in worst case).