#LeetCode 1092: Shortest Common Supersequence
#Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
#A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

#Example 1:

#Input: str1 = "abac", str2 = "cab"
#Output: "cabac"
#Explanation: 
#str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
#str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
#The answer provided is the shortest such string that satisfies these properties.

#Example 2:

#Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
#Output: "aaaaaaaa"

 

#Constraints:

    #1 <= str1.length, str2.length <= 1000
    #str1 and str2 consist of lowercase English letters.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # First find the longest common subsequence (LCS)
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill dp table for LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Build the shortest common supersequence
        i, j = m, n
        result = []
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                # Common character - add only once
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                # Character from str1
                result.append(str1[i-1])
                i -= 1
            else:
                # Character from str2
                result.append(str2[j-1])
                j -= 1
        
        # Add remaining characters
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        # Reverse and join the result
        return ''.join(result[::-1])

# Example Usage: #Please print all possible solutions
str1 = "abac"
str2 = "cab"
result = Solution().shortestCommonSupersequence(str1, str2)

# Write results to a file
with open("d:\\leetcode\\LeetCodeWorkspace\\result.txt", "w") as f:
    f.write(f"Input str1: {str1}\n")
    f.write(f"Input str2: {str2}\n")
    f.write(f"Result: {result}\n")
    f.write(f"Is str1 a subsequence? {all(c in result for c in str1)}\n")
    f.write(f"Is str2 a subsequence? {all(c in result for c in str2)}\n")