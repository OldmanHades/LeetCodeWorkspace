#LeetCode 1780: Check if Number is a Sum of Powers of Three
#Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

#An integer y is a power of three if there exists an integer x such that y == 3x.

#Example 1:

#Input: n = 12
#Output: true
#Explanation: 12 = 31 + 32

#Example 2:

#Input: n = 91
#Output: true
#Explanation: 91 = 30 + 32 + 34

#Example 3:

#Input: n = 21
#Output: false


class Solution:
    def checkPowersofThree(self, n: int) -> bool:

        # Find largest power of 3^i <= n
        i = 0
        while 3**(i+1) <= n:
            i += 1
       
       # Remove largest powers
        while i >= 0:
           power = 3**i
           if power <= n:
               n -= power
           if power <= n:
               return False
           i -= 1
        return n == 0

#Example Usage:
n = 12
print(Solution().checkPowersofThree(n))