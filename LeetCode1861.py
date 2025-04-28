#LeetCode 1861: Rotating the Box
#You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

#    A stone '#'
#    A stationary obstacle '*'
#    Empty '.'

#The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

#It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

#Return an n x m matrix representing the box after the rotation described above.

 

#Example 1:
#Input: boxGrid = [["#",".","#"]]
#Output: [["."],
#         ["#"],
#         ["#"]]

#Example 2:
#Input: boxGrid = [["#",".","*","."],
#              ["#","#","*","."]]
#Output: [["#","."],
#         ["#","#"],
#         ["*","*"],
#         [".","."]]

#Example 3:
#Input: boxGrid = [["#","#","*",".","*","."],
#              ["#","#","#","*",".","."],
#              ["#","#","#",".","#","."]]
#Output: [[".","#","#"],
#         [".","#","#"],
#         ["#","#","*"],
#         ["#","*","."],
#         ["#",".","*"],
#         ["#",".","."]]

 

#Constraints:

#    m == boxGrid.length
#    n == boxGrid[i].length
#    1 <= m, n <= 500
#    boxGrid[i][j] is either '#', '*', or '.'.

#Solution:
from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Step 1: For each row, let the stones fall to the right within that row.
        for i in range(m):
            write = n - 1
            # Process from right to left
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    # Obstacle: reset write pointer to just left of obstacle
                    write = j - 1
                elif box[i][j] == '#':
                    # Stone: move it to 'write' position
                    box[i][j] = '.'
                    box[i][write] = '#'
                    write -= 1
                # Empty cells ('.') are skipped
        
        # Step 2: Rotate the entire box 90 degrees clockwise
        # The rotated box has dimensions n x m
        rotated = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        
        return rotated

# Example Usage and Debug
if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (
            [["#",".","#"]],
            [["."],
             ["#"],
             ["#"]]
        ),
        (
            [["#",".","*","."],
             ["#","#","*","."]],
            [["#","."],
             ["#","#"],
             ["*","*"],
             [".","."]]
        ),
        (
            [["#","#","*",".","*","."],
             ["#","#","#","*",".","."],
             ["#","#","#",".","#","."]],
            [[".","#","#"],
             [".","#","#"],
             ["#","#","*"],
             ["#","*","."],
             ["#",".","*"],
             ["#",".","."]]
        )
    ]
    
    for i, (box, expected) in enumerate(tests, 1):
        result = sol.rotateTheBox([row[:] for row in box])  # copy to avoid in-place side effects
        print(f"Test {i}:")
        print("Input:")
        for row in box:
            print(" ", row)
        print("Expected:")
        for row in expected:
            print(" ", row)
        print("Output:")
        for row in result:
            print(" ", row)
        print("Pass:", result == expected)
        print("-" * 30)
