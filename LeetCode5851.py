#LeetCode 5851: Find Unique Binary String
#Given an array of strings nums containing n unique binary strings each of length n, return a binary string length n that does not appear in nums. If there a multiple answers you may return any of them.

# Example 1:
# Input: nums = ["01", "10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

class Solution:
    def findDifferentBinaryStrings(self, nums: list[str]) -> list[str]:
        strSet = set(nums)
        solutions = []  # list to store all valid binary strings
        n = len(nums)
        
        def backtrack(i, cur):
            # when we've set all positions, check if the generated string is valid
            if i == n:
                candidate = "".join(cur)
                if candidate not in strSet:
                    solutions.append(candidate)
                return
            
            # try putting '0' at position i
            cur[i] = "0"
            backtrack(i + 1, cur)
            # try putting '1' at position i
            cur[i] = "1"
            backtrack(i + 1, cur)
        
        # initialize the list with dummy characters; it will be overwritten by recursion
        backtrack(0, ["0"] * n)
        return solutions

# Example usage:
nums = ["01", "10"]
print(Solution().findDifferentBinaryStrings(nums))
