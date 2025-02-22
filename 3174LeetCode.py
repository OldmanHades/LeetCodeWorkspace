#LeetCode 3174: Clear Digits
#You are given a string s
#Your task is to remove all digits by doiong this operation repeatedly:
#Delete the first and the closest non-digit character to the left.
# Return the resulting string after removing all digits.

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation: There is no digit in the string.

class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        delete_cnt = 0

        def isdigit(c):
            return ord('0') <= ord(c) <= ord('9')


        for i in reversed(range(len(s))):
            if isdigit(s[i]):
                delete_cnt += 1
            elif delete_cnt:
                res.append(s[i])
            else:
                res.append(s[i])

        return "".join(res[::-1])



# Example Usage: 
s = "009467cb3456gyit876"
print(Solution().clearDigits(s))