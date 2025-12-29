def SpiralOrder(matrix: list[list[int]])->list[int]:
    if not matrix or not matrix[0]:
        return []
    
    result=[]

    # Initialize pointers for traversal
    top, left=0,0
    bottom,right=len(matrix)-1, len(matrix[0])-1

    # Traverse the matrix in a spiral order
    while top<=bottom and left <=right:
        # Move left to right across the top row.
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top+=1

        # Move top to bottom along the right column.
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right-=1

        # Move right to left across the bottom row (if still valid).
        if top <=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1

        # Move bottom to top along the left column
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result

matrix=[
    [1,2,3,4,5,6],
    [20,21,22,23,24,7],
    [19,32,33,34,25,8],
    [18,31,36,35,26,9],
    [17,30,29,28,27,10],
    [16,15,14,13,12,11]
]
print(SpiralOrder(matrix))

# TC -> O(m * n)
# SC -> O(1)   (excluding output list)
