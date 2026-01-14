def solve(nums, target):
    result = []

    def backtracking(index, total, subset):
        if total == target:
            result.append(subset.copy())
            return
        if index >= len(nums):
            return

        # Take the element
        subset.append(nums[index])
        backtracking(index + 1, total + nums[index], subset)

        # Backtrack
        subset.pop()

        # Do not take the element
        backtracking(index + 1, total, subset)

    backtracking(0, 0, [])
    return result

nums = [5, 9, 4]
target = 9
print(solve(nums, target))


# TC-> O(2^N)
# SC-> O(1)