def func(arr):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]!=arr[right]:
            return False
        left+=1
        right-=1
    return True
arr="abbaa"
print(func(arr))