# Leetcode407.py
# LeetCode 407: Trapping Rain Water II
# Given an m x n matrix of  integers heightmap  representing the height of each unit cell in a 2D elevation map
# return the volume of water it can trap after raining.

# Example 1:
# Input: heightmap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.

# Example 2:
# Input: heightmap = [[2,1,1,2,1],[1,2,2,1,1],[1,1,1,1,2],[1,2,2,2,1],[2,2,1,2,1]]
# Output: 10
# Explanation: After the rain, water is trapped between the blocks.
"""Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104

"""

# Solution:
import heapq  # Import the heapq module for priority queue implementation


def trapRainWater(heightMap):
    # If the heightmap is empty or has less than 3 rows or columns, no water can be trapped
    if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
        return 0

    rows, cols = (
        len(heightMap),
        len(heightMap[0]),
    )  # Get the number of rows and columns in the heightmap
    visited = [
        [False] * cols for _ in range(rows)
    ]  # Create a visited matrix to keep track of visited cells
    priority_queue = []  # Initialize an empty priority queue (min-heap)

    # Add boundary cells to the priority queue
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                heapq.heappush(
                    priority_queue, (heightMap[r][c], r, c)
                )  # Push the height, row, and column of the boundary cell to the priority queue
                visited[r][c] = True  # Mark the boundary cell as visited

    water = 0  # Initialize the total trapped water to 0
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]  # Define the four directions to move to adjacent cells

    # While the priority queue is not empty
    while priority_queue:
        height, r, c = heapq.heappop(
            priority_queue
        )  # Pop the cell with the minimum height from the priority queue

        # Iterate through the four directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc  # Calculate the coordinates of the adjacent cell
            # If the adjacent cell is within the bounds of the heightmap and has not been visited
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True  # Mark the adjacent cell as visited
                water += max(
                    0, height - heightMap[nr][nc]
                )  # Calculate the trapped water at the adjacent cell and add it to the total water
                heapq.heappush(
                    priority_queue, (max(height, heightMap[nr][nc]), nr, nc)
                )  # Push the adjacent cell to the priority queue with the maximum of the current height and the adjacent cell's height

    return water  # Return the total trapped water


# Eample usage 1:
heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
print(trapRainWater(heightMap))  # Output: 4

# Example usage 2:
heightmap = [
    [2, 1, 1, 2, 1],
    [1, 2, 2, 1, 1],
    [1, 1, 1, 1, 2],
    [1, 2, 2, 2, 1],
    [2, 2, 1, 2, 1],
]
print(trapRainWater(heightMap))  # Output: 10
