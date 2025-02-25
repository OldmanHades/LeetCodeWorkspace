#LeetCode 1524: Number of Sub-arrays with Odd Sum
#Given an array of integers arr, return the number of subarrays with an odd sum.

#Since the answer can be very large, return it modulo 109 + 7.

# Example 1:

# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.

# Example 2:
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.

# Example 3:

# Input: arr = [1,2,3,4,5,6,7]
# Output: 16

 
#Constraints:

 #   1 <= arr.length <= 105
 #   1 <= arr[i] <= 100

MOD = 10**9 + 7

def numOfSubarrays(arr):
    """Return the number of subarrays with an odd sum modulo MOD."""
    even, odd = 1, 0  # even count starts at 1 for the prefix sum of 0
    total = 0
    curr = 0
    for num in arr:
        curr = (curr + num) % 2
        if curr == 0:
            total = (total + odd) % MOD
            even += 1
        else:
            total = (total + even) % MOD
            odd += 1
    return total


if __name__ == '__main__':
    # Example 1:
    print("Example 1:")
    arr = [1, 3, 5]
    print("Input:", arr)
    print("Output:", numOfSubarrays(arr))
    print()

    # Example 2:
    print("Example 2:")
    arr = [2, 4, 6]
    print("Input:", arr)
    print("Output:", numOfSubarrays(arr))
    print()

    # Example 3:
    print("Example 3:")
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Input:", arr)
    print("Output:", numOfSubarrays(arr))
