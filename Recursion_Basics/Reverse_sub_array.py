def func(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    func(arr,left+1,right-1)

arr=[1,2,3,4,5,6,7]
def reversArray(arr,left,right):
    func(arr,left,right)
    print(arr)
reversArray(arr,2,4)