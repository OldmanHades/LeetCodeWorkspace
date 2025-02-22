#A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
#The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
#Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

from collections import defaultdict, deque
from typing import List

def maximumInvitations(favorite: List[int]) -> int:
    n = len(favorite)
    # Build graph of who likes whom
    graph = defaultdict(list)
    indegree = [0] * n
    for i in range(n):
        graph[favorite[i]].append(i)
        indegree[favorite[i]] += 1
    
    # Find all nodes with no incoming edges (not liked by anyone)
    queue = deque([i for i in range(n) if indegree[i] == 0])
    visited = [False] * n
    max_chain = 0
    chain_lengths = [1] * n
    
    # Process nodes with no incoming edges and build chains
    while queue:
        node = queue.popleft()
        visited[node] = True
        fav = favorite[node]
        
        # Update chain length
        chain_lengths[fav] = max(chain_lengths[fav], chain_lengths[node] + 1)
        
        indegree[fav] -= 1
        if indegree[fav] == 0:
            queue.append(fav)
    
    # Find cycles and their maximum lengths
    max_cycle = 0
    total_pairs = 0
    
    for i in range(n):
        if not visited[i]:
            # Found a cycle
            curr = i
            cycle_len = 0
            cycle_nodes = []
            
            while not visited[curr]:
                visited[curr] = True
                cycle_nodes.append(curr)
                curr = favorite[curr]
                cycle_len += 1
            
            if cycle_len == 2:
                # For 2-person cycles, we can extend them with chains
                total_pairs += chain_lengths[cycle_nodes[0]] + chain_lengths[cycle_nodes[1]]
            else:
                # For larger cycles, we take the cycle length
                max_cycle = max(max_cycle, cycle_len)
    
    # Return the maximum of either:
    # 1. The longest cycle found
    # 2. The sum of all 2-person cycles with their chains
    return max(max_cycle, total_pairs)

# Example Usage:
favorite = [3,0,1,4,1]
print("Maximum number of employees that can be invited:", maximumInvitations(favorite))