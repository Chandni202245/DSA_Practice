def countAllSubsequence(nums, k):

    def backtrack(index, total):

        if index == len(nums):
            return 1 if total == k else 0

        # pick
        pick = backtrack(index + 1, total + nums[index])

        # not pick
        not_pick = backtrack(index + 1, total)

        return pick + not_pick

    return backtrack(0, 0)


# ---------------- TEST CASES ---------------- #

# Test case 1
nums = [1, 2, 1]
k = 2
print("Output:", countAllSubsequence(nums, k))
# Expected: 2  → [2], [1,1]


# Test case 2
"""nums = [1, 1, 1]
k = 2
print("Output:", countAllSubsequence(nums, k))
# Expected: 3 → (1,1) combinations


# Test case 3
nums = [2, 3, 5]
k = 5
print("Output:", countAllSubsequence(nums, k))
# Expected: 2 → [5], [2,3]


# Test case 4
nums = [5, 1, 2, 7, 6, 1, 5]
k = 8
print("Output:", countAllSubsequence(nums, k))
# Expected: 3
# [1,7], [2,6], [5,1,2]


# Test case 5
nums = [3, 34, 4, 12, 5, 2]
k = 9
print("Output:", countAllSubsequence(nums, k))
# Expected: 2 → [4,5], [3,4,2]"""
