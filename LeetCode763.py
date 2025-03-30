#LeetCode 763: Partition Labels
#You are given a string s consisting of lowercase english letters.

#We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

#Return a list of integers representing the size of these substrings in the order they appear in the string.

#Example 1:

#Input: s = "xyxxyzbzbbisl"

#Output: [5, 5, 1, 1, 1]

#Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

#Example 2:

#Input: s = "abcabc"

#Output: [6]

#Constraints:

#1 <= s.length <= 100

#Import libraries
from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res
#Example Usage:
s = "xyxxyzbzbbisl"
print(Solution().partitionLabels(s))

#Example Usage 2:
s = "abcabc"
print(Solution().partitionLabels(s))
