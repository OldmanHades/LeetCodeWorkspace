# Leet2683.py
# LeetCode 2683: Neighboring Bitwise XOR
# A 0 indexed array derived with length n is derived by computing the bitwise XOR of adjacent values in a binary string of original length n.

# Specifically for each index i in the range [0, n-1]:
# if i = n -1 then derived[i] = original [i]  ⊕ original [0]
# else derived[i] = original [i]  ⊕ original [i+1]
# Given the derived array, return the original array if there was one.
# otherwise return true with the array  or false if it doesn't exist
# a binary array is an array containing only 0s and 1s

# Example 1:
# Input derived = [1,1,0]
# Output: true


def doesValidArrayExist(derived):
    n = len(derived)

    if n == 1:
        return [derived[0]]

    original = [0] * n

    original[0] = 0

    for i in range(n - 1):
        original[i + 1] = original[i] ^ derived[i]

    if original[n - 1] ^ original[0] != derived[n - 1]:
        return False

    return original


derived = [1, 1, 0]
result = doesValidArrayExist(derived)
print(result)
