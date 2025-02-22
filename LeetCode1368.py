# LeetCode1368.py
# LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid

import heapq


def minCost(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    pq = [(0, 0, 0)]
    visited = set()

    while pq:
        cost, x, y = heapq.heappop(pq)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == (m - 1, n - 1):
            return cost

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if 0 <= nx < m and 0 <= ny < n:
                new_cost = cost + (1 if grid[x][y] != i + 1 else 0)
                heapq.heappush(pq, (new_cost, nx, ny))

    return -1


grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]

print(minCost(grid))
