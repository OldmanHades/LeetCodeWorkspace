# LeetCode 2516: Take K of Each Character from Left and Right
# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.


# Example 1:

# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation:
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.

# Example 2:

# Input: s = "a", k = 1
# Output: -1
# Explanation: It is not possible to take one 'b' or 'c' so return -1.


# Constraints:

#    1 <= s.length <= 105
#    s consists of only the letters 'a', 'b', and 'c'.
#    0 <= k <= s.length

# Solution
from collections import Counter


def takeCharacters(s: str, k: int) -> int:
    n = len(s)
    total_count = Counter(s)

    # Check if it's even possible to get at least k of each character
    for ch in "abc":
        if total_count[ch] < k:
            return -1

    max_window_len = 0
    curr_count = Counter()
    left = 0

    for right in range(n):
        curr_count[s[right]] += 1

        while left <= right and any(
            curr_count[ch] > total_count[ch] - k for ch in "abc"
        ):
            curr_count[s[left]] -= 1
            left += 1

        max_window_len = max(max_window_len, right - left + 1)

    return n - max_window_len


# Example 1
print(takeCharacters("aabaaaacaabc", 2))  # Output: 8

# Example 2
print(takeCharacters("a", 1))  # Output: -1
