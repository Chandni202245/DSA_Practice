# Brute Force
"""def RotateMatrix(matrix):
    n=len(matrix)
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result[j][(n-1)-i]=matrix[i][j]
    return result

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
rotate=RotateMatrix(matrix)
for row in rotate:
    print(row)"""

# TC -> O(n^2)
# SC -> O(n^2)

# Optimal Solution
def RotateMatrix(matrix):
    n=len(matrix)
    # Transpose
    for i in range(0,n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    # Reverse rows
    for i in range(0,n):
        matrix[i].reverse()

    return matrix
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
rotate=RotateMatrix(matrix)
for row in rotate:
    print(row)

# TC-> O(N*N)+O(N*N) = O(N^2)
# SC-> O(1)