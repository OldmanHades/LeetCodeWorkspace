#LeetCode 1765: Map of Highest Peak
#You are given an m x n integer matrix isWater of the sum of m x n that represents a map of land and water cells
#if isWater[i][j] == 0, then cell (i, j) is a water cell. Otherwise, it is a land cell.
# You must assign each cell a height in a way that follows these rules:
# The height of each cell must be non-negative.
# If the cell is a water cell, it's height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter. (i.e. their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell [i.j]'s height. If there are multiple solutions, return all of them.

# Example 1:
# input: isWater = [[0,1],[0,0]]
# Output: [[1.0]],[2.1]]

from collections import deque

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:

        ROWS, COLS = len(isWater), len(isWater[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 0:
                    q.append((r, c, 0))
                else:
                    isWater[r][c] = -1
        
        while q:
            r, c, h = q.popleft()

            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < ROWS and 0 <= nc < COLS and isWater[nr][nc] == -1:
                    isWater[nr][nc] = h + 1
                    q.append((nr, nc, h + 1))

        return isWater

if __name__ == '__main__':
    # In the input matrix, 0 represents water cells and non-zero values represent land cells.
    # Water cells will be assigned a height of 0, and land cells will be assigned a height equal
    # to their minimum Manhattan distance from a water cell.
    isWater = [[0,1],[0,0]]
    print(Solution().highestPeak(isWater))