#merge sort using divide and conquer
def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    while i<n:
        result.append(left[i])
        i+=1
        
    while j<m:
        result.append(right[j])
        j+=1
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)

arr=[3,1,2,4,1,5,2,6,4]
print(merge_sort(arr))

#  Time Complexity:
# - Best Case:    O(n log n)
# - Average Case: O(n log n)
# - Worst Case:   O(n log n)

#  Space Complexity:
# - O(n) (Extra space is required for merging)


#  Working Principle:
# 1. Divide the given array into two halves.
# 2. Recursively sort both halves.
# 3. Merge the two sorted halves into a single sorted array.

#  Key Idea:
# - The array is continuously divided until each subarray has only one element.
# - Single elements are already sorted.
# - Two sorted subarrays are merged using a merge function.