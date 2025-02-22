#LeetCode 802: Find Eventual Safe States
# There is a directed graph of n nodes, where each node is labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph where graph[u] is an array of 
# nodes that are reachable from node u, 
# directed edges are represented as pairs of nodes (u, v) where u is a parent of child node v, and 
# any node in the graph has at most one outgoing edge.
# A node is a terminal node if there are no outgoing edges. 
# A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# Example 1:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2, 4, 5, 6]
# Explanation: 
# Nodes 0 and 3 are the only two safe nodes. 
# A path from node 5 to any other node will contain the node 2, which is connected to both the safe nodes.

# Example 2:
# Input: graph = [[1,2],[2,3],[3,4],[4,5],[3,5]]
# Output: []
# Explanation: No safe nodes are available.

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe = {}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res

# Example Usage:
graph = [[1,2],[2,3],[3,4],[4,5],[3,5]]
print(Solution().eventualSafeNodes(graph))