def firstOccurrence(arr, target):
    n = len(arr)
    first = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1   # move left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first

def lastOccurrence(arr, target):
    n = len(arr)
    last = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1   # move right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last

def FirstAndLastOccurrence(arr, target):
    if len(arr) == 0:
        return [-1, -1]

    first = firstOccurrence(arr, target)
    if first == -1:
        return [-1, -1]

    last = lastOccurrence(arr, target)
    return [first, last]

arr = [1,2,2,2,3,4,5]
target = 2
print(FirstAndLastOccurrence(arr, target))

# Time Complexity: O(log n)

# Space Complexity: O(1)