# LeetCode2661.py
# LeetCode 2661: First Completely Painted Row or Column
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and
# mat both contain all the integers in the range [1, m *n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.

# Example 1:
# Input: arr = [1,3,4,2], mat = [[1,2,3,4], mat = [[1,4], [2,3]]
# Output: 2
# Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

# Example 2:
# Input: arr = [2.8,7,4,1,3,5,6,9], mat = [[3,2,5], [1.4.6], [8,7,9]]
# Output: 3
def first_completely_painted(arr, mat):
    # Get the dimensions of the matrix
    m, n = len(mat), len(mat[0])

    # Create dictionaries to map numbers to their positions in the matrix
    num_to_position = {}
    for i in range(m):
        for j in range(n):
            num_to_position[mat[i][j]] = (i, j)

    # Initialize row and column counters
    row_count = [0] * m
    col_count = [0] * n

    # Iterate through arr and paint cells
    for idx, num in enumerate(arr):
        if num in num_to_position:
            i, j = num_to_position[num]
            row_count[i] += 1
            col_count[j] += 1

            # Check if a row or column is completely painted
            if row_count[i] == n or col_count[j] == m:
                return idx

    return -1  # Return -1 if no row or column is completely painted


# Example 1
arr1 = [1, 3, 4, 2]
mat1 = [[1, 2], [3, 4]]
print(first_completely_painted(arr1, mat1))  # Output: 2

# Example 2
arr2 = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat2 = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
print(first_completely_painted(arr2, mat2))  # Output: 3
