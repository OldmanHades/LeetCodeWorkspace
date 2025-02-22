#LeetCode 1790: Check if One String Swap Can Make Strings Equal
#You are given two strings s1 and s2 of equal length. A string swap is when you choose 2 indices in a string (not necessarily different) and swap the characters at these indices.
#Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

#Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: Swap s1[3] and s2[4], s1 = "bank", s2 = "kanb"

#Example 2:
# Input: s1 = "attack", s2 = "check"
# Output: false
# Explanation: No possible swap can make s1 equal to s2.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2:
                    return False
        return True

# Example Usage:
s1 = "head"
s2 = "deah"
print(Solution().areAlmostEqual(s1, s2))

# Example Usage 2:
s1 = "size"
s2 = "zise"
print(Solution().areAlmostEqual(s1, s2))

# Example Usage 3:
s1 = "light"
s2 = "tighl"
print(Solution().areAlmostEqual(s1, s2))

# Example Usage 4:
s1 = "attack"
s2 = "defend"
print(Solution().areAlmostEqual(s1, s2))