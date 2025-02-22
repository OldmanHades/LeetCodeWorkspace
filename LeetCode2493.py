#LeetCode 2493: Divide Nodes into the Minimum Number of Groups
#You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

#You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

#Divide the nodes of the graph into m groups (1-indexed) such that:

#    Each node in the graph belongs to exactly one group.
#    For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.

#Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

#Example 1:
#Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
#Output: 4
#Explanation: As shown in the image we:
#- Add node 5 to the first group.
#- Add node 1 to the second group.
#- Add nodes 2 and 4 to the third group.
#- Add nodes 3 and 6 to the fourth group.
#We can see that every edge is satisfied.
#It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

from collections import deque
from typing import List


def max_groups(n: int, edges: List[List[int]]) -> int:
    # Build graph
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    # Arrays for bipartite check and visited
    color = [0] * (n + 1)  # 0: uncolored, 1 and -1 for the two colors
    visited = [False] * (n + 1)
    
    # BFS to check bipartite and collect all nodes in the component
    def bfs_component(start: int) -> List[int] or None:
        comp = []
        queue = deque([start])
        color[start] = 1
        comp.append(start)
        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if color[nbr] == 0:
                    color[nbr] = -color[node]
                    comp.append(nbr)
                    queue.append(nbr)
                elif color[nbr] == color[node]:
                    # Not bipartite, return None
                    return None
        return comp
    
    # BFS to find farthest node in a component and distances
    def bfs_farthest(start: int, comp_set: set) -> (int, dict):
        dist = {node: -1 for node in comp_set}
        dist[start] = 0
        queue = deque([start])
        farthest = start
        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr in dist and dist[nbr] == -1:
                    dist[nbr] = dist[node] + 1
                    queue.append(nbr)
                    if dist[nbr] > dist[farthest]:
                        farthest = nbr
        return farthest, dist
    
    total_diameter = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = bfs_component(i)
            if comp is None:
                # Graph is not bipartite
                return -1
            comp_set = set(comp)
            for node in comp:
                visited[node] = True
            
            # Compute the diameter of the component using two BFS passes
            if len(comp) == 1:
                diam = 0
            else:
                u = comp[0]
                v, _ = bfs_farthest(u, comp_set)
                _, dist = bfs_farthest(v, comp_set)
                diam = max(dist.values())
            total_diameter += diam
    
    # Maximum number of global groups = sum(diameters of components) + 1
    return total_diameter + 1


if __name__ == "__main__":
    # Example usage not shown in the comments:
    # Consider a graph with 7 nodes and two components:
    # Component 1: a chain 1-2-3 (diameter = 2, groups needed = 3)
    # Component 2: a star: 4 connected to 5, 6, and 7 (diameter = 1, groups needed = 2)
    # We can assign the chain as [1,2,3] and the star as [3,4] (sharing group 3) for a total of 4 groups.
    n = 7
    edges = [[1,2], [2,3], [4,5], [4,6], [4,7]]
    result = max_groups(n, edges)
    print("Maximum groups:", result)
    
    # You can add more tests, for example, a simple chain graph where: 
    # n = 5, edges = [[1,2], [2,3], [3,4], [4,5]] should return 5 groups.
    n2 = 5
    edges2 = [[1,2], [2,3], [3,4], [4,5]]
    print("Chain graph maximum groups:", max_groups(n2, edges2))
