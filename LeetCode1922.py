#LeetCode 1922: Count Good Numbers
#A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

#For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

#Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

#A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

#Example 1:

#Input: n = 1
#Output: 5
#Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

#Example 2:

#Input: n = 4
#Output: 400

#Example 3:

#Input: n = 50
#Output: 564908303

 

#Constraints:

#    1 <= n <= 1015

#Solution:
from typing import List
import math

class Solution:
    MOD = 10**9 + 7
    
    def pow(self, x, n):
        if n == 0:
            return 1
        res = 1
        x %= self.MOD
        while n > 0:
            if n % 2:
                res = (res * x) % self.MOD
            n = n // 2
            x = (x * x) % self.MOD
        return res
    
    def countGoodNumbers(self, n):
        # At even indices (0, 2, 4...), we have 5 options (0, 2, 4, 6, 8)
        # At odd indices (1, 3, 5...), we have 4 options (2, 3, 5, 7)
        even_positions = (n + 1) // 2  # Ceiling division for even positions (including 0)
        odd_positions = n // 2  # Floor division for odd positions
        
        # Total combinations: 5^(even_positions) * 4^(odd_positions)
        return (self.pow(5, even_positions) * self.pow(4, odd_positions)) % self.MOD

#Example Usage:
n = 1
solution = Solution()
result = solution.countGoodNumbers(n)
print(f"Good numbers of length {n}: {result}")  # Expected output: 5

# Example 2
n = 4
result = solution.countGoodNumbers(n)
print(f"Good numbers of length {n}: {result}")  # Expected output: 400

# Example 3
n = 50
result = solution.countGoodNumbers(n)
print(f"Good numbers of length {n}: {result}")  # Expected output: 564908303
