#LeetCode 3202: Maximum Length of Valid Subsequence II
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Initialize 2D DP table
        f = [[0] * k for _ in range(k)]
        ans = 0
        
        for num in nums:
            x = num % k  # Current remainder
            
            # Try all possible sum remainders j
            for j in range(k):
                y = (j - x + k) % k  # Required previous remainder
                f[x][y] = f[y][x] + 1  # Extend subsequence
                ans = max(ans, f[x][y])  # Track maximum
        
        return ans
# Test the solution
sol = Solution()

# Example from problem description
print(sol.maximumLength([3, 8, 5, 7], 4))  # Output: 3
# Explanation: Subsequence [3, 5, 7] has (3+5)%4 = 0 and (5+7)%4 = 0

# Additional test cases
print(sol.maximumLength([1, 2, 3, 4, 5], 3))  # Output: 4
print(sol.maximumLength([7, 7, 7, 7], 5))     # Output: 4
print(sol.maximumLength([4, 4, 4, 4], 1))     # Output: 4

# Edge cases
print(sol.maximumLength([], 5))               # Output: 0
print(sol.maximumLength([10, 20, 30], 1))     # Output: 3
