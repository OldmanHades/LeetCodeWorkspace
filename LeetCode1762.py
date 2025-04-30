#LeetCode 1762: Buidlings With an Ocean View
#ou are given an array of integers heights of size n representing a row of buildings, where heights[i] is the height of the ith building.

#There is an ocean located to the far right of the buildings. A building has an ocean view if every building to its right is strictly shorter than it.

#Return a list of indices (0-indexed) of the buildings that have an ocean view, sorted in increasing order.

#Example 1:

#Input: heights = [4,2,3,2,1]

#Output: [0,2,3,4]

#Example 2:

#Input: heights = [1,3,2,4,2,5,1]

#Output: [5,6]

#Example 3:

#Input: heights = [9,8,7,7,6,5,4,3]

#Output: [4,5,6,7,8,9]

#Constraints:

#    1 <= heights.length <= 100,000.
#    1 <= heights[i] <= 1,000,000,000
from typing import List

class Solution:
    def findBuildingsWithOceanView(self, heights: List[int]) -> List[int]:
        result = []
        max_height = 0
        
        # Iterate from right to left
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]
        
        # Reverse to get increasing order
        return result[::-1]

sol = Solution()

# Example 1
print(sol.findBuildingsWithOceanView([4, 2, 3, 2, 1]))  # Output: [0, 2, 3, 4]

# Example 2
print(sol.findBuildingsWithOceanView([1, 3, 2, 4, 2, 5, 1]))  # Output: [1, 3, 5, 6]

# Example 3
print(sol.findBuildingsWithOceanView([9,8,7,7,6,5,4,3]))  # Output: [0, 1, 2, 3, 4, 5, 6, 7]