#LeetCode 2375: Construct Smallest Number from DI String
# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n +1 is created using the following conditions:
# num consists of the digits '1' to '9', where each digit is used at most once.
# if pattern[i] == 'I', then num[i] < num[i + 1]
# if pattern[i] == 'D', then num[i] > num[i + 1]
# Return the lexicographically smallest possible string num that meets the conditions.

# Example 1:
# Pattern = "IIIDIDDD"
# Output: "123549876"

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
        return "".join(res)


# Example Usage:
pattern = "IIIDIDDD"
print(Solution().smallestNumber(pattern))