#LeetCode 1358: Number of Substrings Containing All Three Characters
#Given a string s consisting only of characters a, b and c.
#Return the number of substrings containing at least one occurrence of all these characters a, b and c.

#Example 1:

#Input: s = "abcabc"
#Output: 10
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

#Example 2:

#Input: s = "aaacb"
#Output: 3
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

#Example 3:

#Input: s = "abc"
#Output: 1

#Constraints:

#3 <= s.length <= 5 x 10^4
#s only consists of a, b or c characters.

#Solution:

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) == 3:
                res += (len(s) - r)
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        return res
    #Example Usage:
s = "abcabc"
print(Solution().numberOfSubstrings(s))