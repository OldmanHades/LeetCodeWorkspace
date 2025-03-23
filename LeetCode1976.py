#LeetCode 1976: Number of Ways to Arrive at Destination
#You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

#You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

#Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

#Example 1:
#Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
#Output: 4
#Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
#The four ways to get there in 7 minutes are:
#- 0 ➝ 6
#- 0 ➝ 4 ➝ 6
#- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
#- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

#Example 2:
#Input: n = 2, roads = [[1,0,10]]
#Output: 1
#Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

 

#Constraints:

#    1 <= n <= 200
#    n - 1 <= roads.length <= n * (n - 1) / 2
#    roads[i].length == 3
#    0 <= ui, vi <= n - 1
#    1 <= timei <= 109
#    ui != vi
#    There is at most one road connecting any two intersections.
#    You can reach any intersection from any other intersection.


#Solution
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        MOD = 10**9 + 7
        min_heap = [(0, 0)] # (cost, node)
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Set the starting node's cost to 0
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)
            
            # Skip if we've already found a better path
            if cost > min_cost[node]:
                continue
                
            for neighbor, neighbor_cost in adj[node]:
                if cost + neighbor_cost < min_cost[neighbor]:
                    min_cost[neighbor] = cost + neighbor_cost
                    path_count[neighbor] = path_count[node]
                    heappush(min_heap, (cost + neighbor_cost, neighbor))
                elif cost + neighbor_cost == min_cost[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD
        return path_count[n - 1]

# Example Usage:

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(Solution().countPaths(n, roads))
