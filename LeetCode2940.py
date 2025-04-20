#LeetCode 2940: Find Building Where Alice and Bob Can Meet
#You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

#If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

#You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

#Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

 

#Example 1:

#Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
#Output: [2,5,-1,5,2]
#Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
#In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
#In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
#In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
#In the fifth query, Alice and Bob are already in the same building.  
#For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
#For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

#Example 2:

#Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
#Output: [7,6,-1,4,6]
#Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
#In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
#In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
#In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
#In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
#For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
#For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

 

#Constraints:

#    1 <= heights.length <= 5 * 104
#    1 <= heights[i] <= 109
#    1 <= queries.length <= 5 * 104
#    queries[i] = [ai, bi]
#    0 <= ai, bi <= heights.length - 1

#Solution
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        """
        Find the leftmost building where Alice and Bob can meet for each query.
        """
        res = [-1] * len(queries)
        groups = defaultdict(list)  # map right index to list of (required_height, query_idx)
        # Preprocess queries for direct moves and grouping
        for idx, (a, b) in enumerate(queries):
            l, r = sorted((a, b))
            # direct move if same building or Alice can move to Bob's building
            if l == r or heights[r] > heights[l]:
                res[idx] = r
            else:
                # require height strictly greater than both
                required_h = max(heights[l], heights[r])
                groups[r].append((required_h, idx))
        min_heap = []
        # scan buildings in increasing index to resolve grouped queries
        for i, h in enumerate(heights):
            # add queries whose right endpoint is current building
            for req_h, q_idx in groups.get(i, []):
                heapq.heappush(min_heap, (req_h, q_idx))
            # resolve any queries satisfied by current building height
            while min_heap and min_heap[0][0] <= h:
                _, q_idx = heapq.heappop(min_heap)
                res[q_idx] = i
        return res

# Example usage section to test implementation with provided examples
if __name__ == '__main__':
    # Example 1
    heights1 = [6, 4, 8, 5, 2, 7]
    queries1 = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    print("Example 1 output:", Solution().leftmostBuildingQueries(
        heights1, queries1
    ))
    # Expected output: [2, 5, -1, 5, 2]

    # Example 2
    heights2 = [5, 3, 8, 2, 6, 1, 4, 6]
    queries2 = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
    print("Example 2 output:", Solution().leftmostBuildingQueries(
        heights2, queries2
    ))
    # Expected output: [7, 6, -1, 4, 6]
