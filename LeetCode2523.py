#LeetCode 2523: Closest Prime Numbers in Range
#Given two positive integers left and right, find the two integers num1 and num2 such that:

#    left <= num1 < num2 <= right .
#    Both num1 and num2 are 
#
#    .
#    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

#Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

#Example 1:

#Input: left = 10, right = 19
#Output: [11,13]
#Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
#The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
#Since 11 is smaller than 17, we return the first pair.

#Example 2:

#Input: left = 4, right = 6
#Output: [-1,-1]
#Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

#Constraints:

#    1 <= left <= right <= 106

from math import sqrt

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        
        def get_primes():
            is_prime = [True] * (right +1)
            is_prime[0] = is_prime[1] = False

            for n in range(2, int(sqrt(right +1)) +1):
                if not is_prime[n]:
                    continue
                for m in range(n + n, right +1, n):
                    is_prime[m] = False
            primes = []
            for i in range(len(is_prime)):
                if is_prime[i] and i >= left:
                    primes.append(i)
            return primes


        primes = get_primes()
        res = [-1,-1]
        diff = right - left + 1

        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]

        return res


#Example Usage:

Left = 10
right = 19
print(Solution().closestPrimes(Left, right))
