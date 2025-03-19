#LeetCode 2658: Maximum Number of Fish in a Grid
#You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

#    A land cell if grid[r][c] = 0, or
#    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

#A fisher can start at any water cell (r, c) and can do the following operations any number of times:

#    Catch all the fish at cell (r, c), or
#    Move to any adjacent water cell.

#Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

#An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

#Example 1:
#Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
#Output: 7
#Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

#Example 2:
#Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
#Output: 1
#Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

 

#Constraints:
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 10
#0 <= grid[i][j] <= 10

#Solution:
import time

class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or visit[r][c]):
                return 0
            visit[r][c] = True
            res = grid[r][c]
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                res += dfs(nr, nc)
            return res

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = [[False] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] or not visit[r][c]:
                    res = max(res, dfs(r, c))
        return res

#Example Usage:
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]

# Time the execution with more precision
NUM_RUNS = 1000
solution = Solution()

# Warm-up run
result = solution.findMaxFish(grid)

# Timing with multiple runs for more accurate measurement
start_time = time.perf_counter()
for _ in range(NUM_RUNS):
    solution.findMaxFish(grid)
end_time = time.perf_counter()

avg_time = (end_time - start_time) * 1000 / NUM_RUNS

print(f"Result: {result}")
print(f"Execution time (average over {NUM_RUNS} runs): {avg_time:.6f} ms")