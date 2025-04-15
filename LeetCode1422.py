#LeetCode 1422: Maximum Score After Splitting a String
#Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

#The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

#Example 1:

#Input: s = "011101"
#Output: 5 
#Explanation: 
#All possible ways of splitting s into two non-empty substrings are:
#left = "0" and right = "11101", score = 1 + 4 = 5 
#left = "01" and right = "1101", score = 1 + 3 = 4 
#left = "011" and right = "101", score = 1 + 2 = 3 
#left = "0111" and right = "01", score = 1 + 1 = 2 
#left = "01110" and right = "1", score = 2 + 1 = 3

#Example 2:

#Input: s = "00111"
#Output: 5
#Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

#Example 3:

#Input: s = "1111"
#Output: 3

 

#Constraints:

#    2 <= s.length <= 500
#    The string s consists of characters '0' and '1' only.

#Solution:
from typing import List

def maxScore(s: str) -> int:
    max_score = 0
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        score = left.count('0') + right.count('1')
        max_score = max(max_score, score)
    return max_score

# Example Usage:
# Each test prints the input, expected output, and actual output for verification.

# Example 1:
s1 = "011101"
expected1 = 5
print(f"Input: {s1}\nExpected Output: {expected1}\nActual Output: {maxScore(s1)}\n")

# Example 2:
s2 = "00111"
expected2 = 5
print(f"Input: {s2}\nExpected Output: {expected2}\nActual Output: {maxScore(s2)}\n")

# Example 3:
s3 = "1111"
expected3 = 3
print(f"Input: {s3}\nExpected Output: {expected3}\nActual Output: {maxScore(s3)}\n")

