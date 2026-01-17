def subsequence(nums, k):

    def backtrack(index, total):
        # found subsequence
        if total == k:
            return True

        # invalid case
        if total > k or index >= len(nums):
            return False

        # pick
        if backtrack(index + 1, total + nums[index]):
            return True

        # not pick
        if backtrack(index + 1, total):
            return True

        return False

    return backtrack(0, 0)

nums = [1, 2, 3, 4]
k = 6

print(subsequence(nums, k))

# Time: O(2^n)

# Space: O(n) (recursion stack)