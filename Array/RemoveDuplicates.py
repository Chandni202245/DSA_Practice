# Remove duplicates from a sorted array in-place and return the count of unique elements.
def removeDuplicates(arr):
    n=len(arr)
    i=0
    j=i+1
    if n==1:
        return
    while (j<n):
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1

arr=[1,1,1,2,3,4,4,7,9,9,10]
print(removeDuplicates(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)   (in-place, no extra space used)
