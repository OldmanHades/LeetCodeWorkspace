#LeetCode 3243: Shortest Distance After Road Addition I:
#You are given an integer n and a 2D integer array queries.

#There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

#queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

#Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

#Example 1:

#Input: n = 5, queries = [[2,4],[0,2],[0,4]]

#Output: [3,2,1]

#Example 2:

#Input: n = 4, queries = [[0,3],[0,2]]

#Output: [1,1]

#Constraints:

#    3 <= n <= 500
#    1 <= queries.length <= 500
#    queries[i].length == 2
#    0 <= queries[i][0] < queries[i][1] < n
#    1 < queries[i][1] - queries[i][0]
#    There are no repeated roads among the queries.

#Solution:
from typing import List
from collections import defaultdict
from heapq import heappush, heappop
from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def shortest_path():
            q = deque([0])
            dist = [-1] * n
            dist[0] = 0
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dist[u]
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return -1

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res

#Example Usage:

#1
n = 5
queries = [[2,4],[0,2],[0,4]]
#Output: [3,2,1]

#2
n = 4
queries = [[0,3],[0,2]]
#Output: [1,1]

print(Solution().shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))
print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]]))

