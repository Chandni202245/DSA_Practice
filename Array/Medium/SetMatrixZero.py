# Brute force 
"""def markInfinity(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    # mark row
    for j in range(cols):
        if matrix[r][j] != 0:
            matrix[r][j] = float("inf")

    # mark column
    for i in range(rows):
        if matrix[i][c] != 0:
            matrix[i][c] = float("inf")


def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: mark infinity
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)

    # Step 2: convert infinity to zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

    return matrix


matrix = [
    [7,9,5,3],
    [10,20,0,1],
    [29,0,8,5],
    [4,14,6,7]
]

result = setZeros(matrix)

for row in result:
    print(row)"""


# Optimal Solution
def SetZeros(matrix):
    r=len(matrix)
    c=len(matrix[0])
    rowtrack=[0 for _ in range(r)]
    coltrack=[0 for _ in range(c)]
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j]==0:
                rowtrack[i]=-1
                coltrack[j]=-1
    for i in range(0,r):
        for j in range(0,c):
            if rowtrack[i]==-1 or coltrack[j]==-1:
                matrix[i][j]=0
    return matrix
matrix = [
    [7,9,5,3],
    [10,20,0,1],
    [29,0,8,5],
    [4,14,6,7]
]
SetZeros(matrix)

for row in matrix:
    print(row)


# TC -> O(r * c)
# SC -> O(r + c)
