# Print the matrix
"""def twoDMatrix(nums):
    n=len(nums)
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            print(nums[i][j],end=" ")
        print()

nums=[[5,2,3],[7,1,9],[1,8,6]]
print(twoDMatrix(nums))"""

# Upper Triangle

"""def upperTriangle(nums):
    n=len(nums)
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if j>=i:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()

nums=[[5,2,3],[7,1,9],[1,8,6]]
print(upperTriangle(nums))"""

# Lower Triangle
"""def lowerTriangle(nums):
    n=len(nums)
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if j<=i:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()

nums=[[5,2,3],[7,1,9],[1,8,6]]
print(lowerTriangle(nums))"""

# Print Diagonal elements
"""def diagonal(nums):
    n=len(nums)
    rows=n
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if j==i:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
nums=[[5,2,3],[7,1,9],[1,8,6]]
print(diagonal(nums))"""

def transposeOfMatrix(nums):
    n=len(nums)
    rows=n
    cols=len(nums[0])
    result=[[0]*rows for _ in range(cols)]
    for i in range(0,rows):
        for j in range(0,cols):
            result[j][i]=nums[i][j]
    return result

nums = [[5,9,1],[2,3,7]]
ans = transposeOfMatrix(nums)

for row in ans:
    print(row)

# TC -> O(m * n)
# SC -> O(m * n)