# LeetCode 2381: Shifting Letters II
# Efficient difference array solution with detailed comments and example usage

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Applies a series of shift operations to the input string s according to the shifts array.
        Each shift is a range update: [start, end, direction], where direction=1 means shift right (forward),
        and direction=0 means shift left (backward). Uses a difference array for efficiency.
        """
        n = len(s)
        # Initialize the difference array for range updates
        diff = [0] * (n + 1)

        # Apply each shift operation as a range update
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # Compute the prefix sum to get the net shift for each character
        res = []
        shift = 0
        for i in range(n):
            shift += diff[i]
            # Shift the character, wrapping around the alphabet
            offset = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(ord('a') + offset))

        return ''.join(res)

# Example Usage:
# Test case 1
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]  # Output should be "ace"
print(Solution().shiftingLetters(s, shifts))  # Expected output: "ace"

# Test case 2
s2 = "dztz"
shifts2 = [[0, 0, 0], [1, 1, 1]]  # Output should be "catz"
print(Solution().shiftingLetters(s2, shifts2))  # Expected output: "catz"

