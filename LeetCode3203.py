# LeetCode 3203: Find Minimum Diameter After Merging Two Trees
# There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

# You must connect one node from the first tree with another node from the second tree with an edge.

# Return the minimum possible diameter of the resulting tree.

# The diameter of a tree is the length of the longest path between any two nodes in the tree.
# Example 1:

# Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

# Output: 3

# Explanation:

# We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.
# Example 2:

# Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

# Output: 5

# Explanation:

# We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

# Constraints:

#     1 <= n, m <= 105
#     edges1.length == n - 1
#     edges2.length == m - 1
#     edges1[i].length == edges2[i].length == 2
#     edges1[i] = [ai, bi]
#     0 <= ai, bi < n
#     edges2[i] = [ui, vi]
#     0 <= ui, vi < m
#     The input is generated such that edges1 and edges2 represent valid trees.
from collections import deque

def bfs(start_node, adj, n):
    """
    Performs BFS starting from start_node to find distances, the farthest node,
    and its distance.
    Returns: (farthest_node, max_distance, distances_array)
    """
    dist = [-1] * n
    dist[start_node] = 0
    q = deque([start_node])
    farthest_node = start_node
    max_dist = 0

    while q:
        u = q.popleft()

        if dist[u] > max_dist:
            max_dist = dist[u]
            farthest_node = u

        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    return farthest_node, max_dist, dist

def get_tree_info(edges, n):
    """
    Calculates the diameter and radius of a tree.
    The radius is the minimum maximum distance from any node to any other node.
    This minimum maximum distance is achieved at the tree's center(s).
    We find this by taking max(distance from one diameter endpoint, distance from the other)
    for every node, and then taking the minimum of these values.
    """
    if n == 1:
        return 0, 0 # Diameter and radius of a single node tree is 0

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # 1. Find one endpoint of a diameter (farthest node from an arbitrary node, say 0)
    u, _, _ = bfs(0, adj, n)

    # 2. Find the other endpoint of a diameter and the diameter length
    v, diameter, dist_u = bfs(u, adj, n)

    # 3. Get distances from the other diameter endpoint v
    _, _, dist_v = bfs(v, adj, n)

    # 4. Calculate max_dist[i] for each node i (max distance from i to any node in the tree)
    # This is max(dist(i, u), dist(i, v)) where u and v are diameter endpoints
    # The radius is the minimum of these max_dist[i] values.
    radius = float('inf')
    for i in range(n):
        max_dist_i = max(dist_u[i], dist_v[i])
        radius = min(radius, max_dist_i)

    return diameter, radius

def find_minimum_diameter(n: int, edges1: list[list[int]], m: int, edges2: list[list[int]]) -> int:
    """
    Finds the minimum possible diameter of the resulting tree after connecting
    one node from tree1 to one node from tree2 with a new edge.
    """
    # Get diameter and radius for tree 1
    diam1, radius1 = get_tree_info(edges1, n)

    # Get diameter and radius for tree 2
    diam2, radius2 = get_tree_info(edges2, m)

    # The diameter of the merged tree will be the maximum of:
    # 1. The diameter of tree 1.
    # 2. The diameter of tree 2.
    # 3. The longest path that traverses the newly added edge.
    # The longest path traversing the new edge (u, v) is max_dist1(u) + 1 + max_dist2(v).
    # To minimize this path length, we should choose nodes u and v that minimize
    # max_dist1(u) and max_dist2(v) respectively.
    # The node that minimizes the maximum distance to any other node in a tree
    # is the tree's center(s). The minimum possible max distance is the radius.
    # So, the minimum length of a path traversing the new edge is radius1 + 1 + radius2.

    min_merged_diameter = max(diam1, diam2, radius1 + radius2 + 1)

    return min_merged_diameter

# --- Example Usage ---

# Example 1
edges1_ex1 = [[0,1],[0,2],[0,3]]
n_ex1 = 4
edges2_ex1 = [[0,1]]
m_ex1 = 2
output_ex1 = find_minimum_diameter(n_ex1, edges1_ex1, m_ex1, edges2_ex1)
print(f"Example 1 Input:")
print(f"  edges1 = {edges1_ex1}, n = {n_ex1}")
print(f"  edges2 = {edges2_ex1}, m = {m_ex1}")
print(f"Example 1 Output: {output_ex1}") # Expected: 3

# Example 2
edges1_ex2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
n_ex2 = 8
edges2_ex2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
m_ex2 = 8
output_ex2 = find_minimum_diameter(n_ex2, edges1_ex2, m_ex2, edges2_ex2)
print(f"\nExample 2 Input:")
print(f"  edges1 = {edges1_ex2}, n = {n_ex2}")
print(f"  edges2 = {edges2_ex2}, m = {m_ex2}")
print(f"Example 2 Output: {output_ex2}") # Expected: 5

# Additional Test Case (e.g., path graphs)
edges1_ex3 = [[0,1],[1,2],[2,3]] # Path 0-1-2-3, n=4
n_ex3 = 4
edges2_ex3 = [[0,1],[1,2]]      # Path 0-1-2, m=3
m_ex3 = 3
output_ex3 = find_minimum_diameter(n_ex3, edges1_ex3, m_ex3, edges2_ex3)
print(f"\nAdditional Test Case (Path Graphs) Input:")
print(f"  edges1 = {edges1_ex3}, n = {n_ex3}")
print(f"  edges2 = {edges2_ex3}, m = {m_ex3}")
# Expected calculation:
# Tree1 (0-1-2-3): diam=3 (0-3), endpoints=0,3. dist(0) from 0/3 is 0/3. dist(1) 1/2. dist(2) 2/1. dist(3) 3/0.
# max_dist: 0:max(0,3)=3, 1:max(1,2)=2, 2:max(2,1)=2, 3:max(3,0)=3. radius1=min(3,2,2,3)=2. (Centers 1, 2)
# Tree2 (0-1-2): diam=2 (0-2), endpoints=0,2. dist(0) from 0/2 is 0/2. dist(1) 1/1. dist(2) 2/0.
# max_dist: 0:max(0,2)=2, 1:max(1,1)=1, 2:max(2,0)=2. radius2=min(2,1,2)=1. (Center 1)
# Result: max(diam1, diam2, radius1 + radius2 + 1) = max(3, 2, 2 + 1 + 1) = max(3, 2, 4) = 4
print(f"Additional Test Case Output: {output_ex3}") # Expected: 4

# Additional Test Case (Single Nodes)
edges1_ex4 = []
n_ex4 = 1
edges2_ex4 = []
m_ex4 = 1
output_ex4 = find_minimum_diameter(n_ex4, edges1_ex4, m_ex4, edges2_ex4)
print(f"\nAdditional Test Case (Single Nodes) Input:")
print(f"  edges1 = {edges1_ex4}, n = {n_ex4}")
print(f"  edges2 = {edges2_ex4}, m = {m_ex4}")
# Expected: diam1=0, radius1=0, diam2=0, radius2=0. Result: max(0, 0, 0+0+1) = 1
print(f"Additional Test Case Output: {output_ex4}") # Expected: 1