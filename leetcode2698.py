#LeetCode 2698: Find the Punishment Number of an Integer
#Given a positive integer n, return the punishment number of that integer. The punishment number of an integer is defined as the sum of its digits.

#Example 1:
#Input n = 10
#Output = 182
#Explanation: There are exactly 3 integers i that satisfy the conditions in the statement.

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(i, cur: int, target: int, string: str):
            """Recursively partition the string to check if it can sum up to the target number."""
            if i == len(string) and cur == target:
                return True
            for j in range(i, len(string)):
                # Try partitioning the string from i to j+1 and accumulate the sum
                if partition(j + 1, cur + int(string[i:j+1]), target, string):
                    return True
            return False
        res = 0

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i*i)):
                res += i * i
        return res

n = 10
print(Solution().punishmentNumber(n))