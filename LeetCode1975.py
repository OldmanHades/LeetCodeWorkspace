#LeetCode 1975: Maximum Matrix Sum
#You are given an n x n integer matrix. You can do the following operation any number of times:

#    Choose any two adjacent elements of matrix and multiply each of them by -1.

#Two elements are considered adjacent if and only if they share a border.

#Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

#Example 1:
#Input: matrix = [[1,-1],[-1,1]]
#Output: 4
#Explanation: We can follow the following steps to reach sum equals 4:
#- Multiply the 2 elements in the first row by -1.
#- Multiply the 2 elements in the first column by -1.

#Example 2:
#Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
#Output: 16
#Explanation: We can follow the following step to reach sum equals 16:
#- Multiply the 2 last elements in the second row by -1.

 

#Constraints:

#    n == matrix.length == matrix[i].length
#    2 <= n <= 250
#    -105 <= matrix[i][j] <= 105


#Solution:
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        min_val = float('inf')
        sum_val = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] < 0:
                    count += 1
                min_val = min(min_val, abs(matrix[i][j]))
                sum_val += abs(matrix[i][j])
        if count % 2 == 0:
            return sum_val
        else:
            return sum_val - 2 * min_val

#Example Usuage:
matrix = [[1,-1],[-1,1]]
solution = Solution()
print(solution.maxMatrixSum(matrix)) #Output: 4
