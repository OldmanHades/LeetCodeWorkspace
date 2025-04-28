#LeetCode 1072: Flip Columns for Maximum Number of Equal Rows
#You are given an m x n binary matrix matrix.

#You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

#Return the maximum number of rows that have all values equal after some number of flips.

 

#Example 1:

#Input: matrix = [[0,1],[1,1]]
#Output: 1
#Explanation: After flipping no values, 1 row has all values equal.

#Example 2:

#Input: matrix = [[0,1],[1,0]]
#Output: 2
#Explanation: After flipping values in the first column, both rows have equal values.

#Example 3:

#Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
#Output: 2
#Explanation: After flipping values in the first two columns, the last two rows have equal values.

 

#Constraints:

#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 300
#    matrix[i][j] is either 0 or 1.

#Solution:
from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # The key insight: after column flips, two rows can be identical only if
        # they were identical or complementary to each other before flipping
        count = defaultdict(int)
        
        for row in matrix:
            # We can canonicalize each row by ensuring it starts with 0
            # This handles both the original row and its complement
            # (if the row starts with 1, flip all values in the row)
            if row[0] == 1:
                # Create a tuple of the flipped row (complement)
                canonical = tuple(1 - x for x in row)
            else:
                # Create a tuple of the original row
                canonical = tuple(row)
                
            # Increment the count for this canonical pattern
            count[canonical] += 1
            
        # Return the maximum count
        return max(count.values()) if count else 0

# Example Usage:
if __name__ == "__main__":
    # Example 1
    matrix1 = [[0,1],[1,1]]
    print(f"Example 1: {Solution().maxEqualRowsAfterFlips(matrix1)}")  # Expected: 1
    
    # Example 2
    matrix2 = [[0,1],[1,0]]
    print(f"Example 2: {Solution().maxEqualRowsAfterFlips(matrix2)}")  # Expected: 2
    
    # Example 3
    matrix3 = [[0,0,0],[0,0,1],[1,1,0]]
    print(f"Example 3: {Solution().maxEqualRowsAfterFlips(matrix3)}")  # Expected: 2