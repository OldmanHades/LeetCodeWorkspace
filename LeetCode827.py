#LeetCode 827: Making a Large Island
#You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#Return the size of the largest island in grid after applying this operation.
#An island is a group of 1s that are adjacent (4-directionally) in grid. Rows are considered adjacent if they share an edge, and columns are considered adjacent if they share a vertex.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change one 0 to 1 and connect three 1s, then we get an island with area = 4.

# Example 3:
# Input: grid = [(1,1),(1,1)]
# Output: 4
# Explanation: We can connect two 1s in the first row and connect two 1s in the second row, then we get an island with area = 4.

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        # Step 1: Label each island with a unique id and record its area
        island_id = 2  # start from 2 since 0 and 1 are used in the grid
        island_area = {}

        def dfs(i: int, j: int, id: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            area = 1
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                area += dfs(x, y, id)
            return area

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, island_id)
                    island_area[island_id] = area
                    island_id += 1

        # If there is no water, the whole grid is one island
        res = max(island_area.values()) if island_area else 0

        # Step 2: For each water cell, compute potential island size by flipping it
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1  # flip the water cell to land
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1 and grid[x][y] not in seen:
                            seen.add(grid[x][y])
                            total += island_area[grid[x][y]]
                    res = max(res, total)

        return res


def main():
    # Sample usage with a grid not from the typical examples.
    grid = [
        [1, 1, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 0]
    ]
    # Create a copy of the grid if needed to preserve original data
    sol = Solution()
    result = sol.largestIsland([row[:] for row in grid])
    print("Largest Island:", result)


if __name__ == '__main__':
    main()

