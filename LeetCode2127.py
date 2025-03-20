#LeetCode 2127: Maximum Employees to Be Invited to a Meeting
#A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

#The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

#Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

#Example 1:
#Input: favorite = [2,2,1,2]
#Output: 3
#Explanation:
#The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
#All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
#Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
#The maximum number of employees that can be invited to the meeting is 3. 

#Example 2:
#Input: favorite = [1,2,0]
#Output: 3
#Explanation: 
#Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
#The seating arrangement will be the same as that in the figure given in example 1:
#- Employee 0 will sit between employees 2 and 1.
#- Employee 1 will sit between employees 0 and 2.
#- Employee 2 will sit between employees 1 and 0.
#The maximum number of employees that can be invited to the meeting is 3.

#Example 3:
#Input: favorite = [3,0,1,4,1]
#Output: 4
#Explanation:
#The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
#Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
#So the company leaves them out of the meeting.
#The maximum number of employees that can be invited to the meeting is 4.

 

#Constraints:
#n == favorite.length
#2 <= n <= 105
#0 <= favorite[i] <= n - 1
#favorite[i] != i

#Solution:

from typing import List
from collections import defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        print("Starting solution...")

        # Find Cycles
        N = len(favorite)
        visit = [False] * N
        length_2_cycles = []
        longest_cycle = 0

        for i in range(N):
            if visit[i]:
                continue
            
            # Find cycle starting from i
            cycle = []
            cur = i
            while not visit[cur]:
                visit[cur] = True
                cycle.append(cur)
                cur = favorite[cur]
            
            # Check if we found a cycle
            if cur in cycle:
                cycle_start_idx = cycle.index(cur)
                cycle_length = len(cycle) - cycle_start_idx
                print(f"Found cycle of length {cycle_length}")
                
                if cycle_length == 2:
                    node1, node2 = cycle[-2], cycle[-1]
                    length_2_cycles.append((node1, node2))
                else:
                    longest_cycle = max(longest_cycle, cycle_length)
        
        print(f"Longest cycle: {longest_cycle}")
        print(f"Length-2 cycles: {length_2_cycles}")
        
        # Find the sum of the longest chains extending from length-2 cycles
        inverted = defaultdict(list)
        for i, fav in enumerate(favorite):
            inverted[fav].append(i)
        
        def bfs(node, exclude):
            q = deque([(node, 0)])  # (node, length)
            visited = {node, exclude}
            max_length = 0
            
            while q:
                curr, length = q.popleft()
                max_length = max(max_length, length)
                
                for neighbor in inverted[curr]:
                    if neighbor not in visited and neighbor != exclude:
                        visited.add(neighbor)
                        q.append((neighbor, length + 1))
            
            return max_length

        chain_sum = 0
        for n1, n2 in length_2_cycles:
            # For each length-2 cycle, find the longest chains extending from both nodes
            chain1 = bfs(n1, n2)
            chain2 = bfs(n2, n1)
            print(f"Chains for cycle ({n1},{n2}): {chain1} and {chain2}")
            chain_sum += chain1 + chain2 + 2
        
        print(f"Chain sum: {chain_sum}")
        result = max(longest_cycle, chain_sum)
        print(f"Final result: {result}")
        return result

#Example Usage:
if __name__ == '__main__':
    print("Script started")
    favorite = [2,2,1,2]
    solution = Solution()
    print("Solution instance created")
    result = solution.maximumInvitations(favorite)
    print(f"Solution result: {result}")
    print("Script finished")
