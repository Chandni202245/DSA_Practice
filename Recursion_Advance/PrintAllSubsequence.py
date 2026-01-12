# Print all subsequences
def subsequence(nums):
    result = []
    subset = []

    def func(index):
        # Base case
        if index == len(nums):
            result.append(subset.copy())
            return

        # Include current element
        subset.append(nums[index])
        func(index + 1)

        # Exclude current element
        subset.pop()
        func(index + 1)

    func(0)   # initial call
    return result

nums = [1, 2, 3]
ans = subsequence(nums)
print(ans)

# TC-> O(2^n)
# SC-> O(N) where N is the stack space
