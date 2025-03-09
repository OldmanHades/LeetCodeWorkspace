#LeetCode 3208: Alternating Groups 2
#There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

#    colors[i] == 0 means that tile i is red.
#    colors[i] == 1 means that tile i is blue.

#An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

#Return the number of alternating groups.

#Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

#Example 1:

#Input: colors = [0,1,0,1,0], k = 3
#Output: 3

#Example 2:

#Input: colors = [0,1,0,0,1,0,1], k = 6
#Output: 2

#Example 3:

#Input: colors = [1,1,0,1], k = 4

#Output: 0

#Constraints:

#    3 <= colors.length <= 105
#    0 <= colors[i] <= 1
#    3 <= k <= colors.length

#Solution:
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        if k < 3:
            return 0  # Based on constraints, k is at least 3
            
        n = len(colors)
        count = 0
        
        # Check each possible starting position
        for start in range(n):
            is_alternating = True
            
            # Print for debugging
            group = [colors[(start + i) % n] for i in range(k)]
            print(f"Checking group starting at {start}: {group}")
            
            # Check alternating pattern - each middle tile should differ from neighbors
            for i in range(1, k-1):
                curr = colors[(start + i) % n]
                prev = colors[(start + i - 1) % n]
                next_tile = colors[(start + i + 1) % n]
                
                if curr == prev or curr == next_tile:
                    is_alternating = False
                    print(f"  Not alternating at position {i} in group: {prev},{curr},{next_tile}")
                    break
            
            if is_alternating:
                count += 1
                print(f"  Found alternating group: {group}")
        
        return count

# Example Usage with verbose output:
print("=" * 50)
print("TESTING SOLUTION")
print("=" * 50)
solution = Solution()

# Example 1
colors1 = [0,1,0,1,0]
k1 = 3
print("\nExample 1:")
print(f"Input: colors = {colors1}, k = {k1}")
result1 = solution.numberOfAlternatingGroups(colors1, k1)
print(f"Output: {result1}")
print(f"Expected: 3")

# Example 2
colors2 = [0,1,0,0,1,0,1]
k2 = 6
print("\nExample 2:")
print(f"Input: colors = {colors2}, k = {k2}")
result2 = solution.numberOfAlternatingGroups(colors2, k2)
print(f"Output: {result2}")
print(f"Expected: 2")

# Example 3
colors3 = [1,1,0,1]
k3 = 4
print("\nExample 3:")
print(f"Input: colors = {colors3}, k = {k3}")
result3 = solution.numberOfAlternatingGroups(colors3, k3)
print(f"Output: {result3}")
print(f"Expected: 0")
