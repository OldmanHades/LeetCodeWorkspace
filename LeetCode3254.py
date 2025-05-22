# LeetCode 3254: Find the Power of K-Size Subarrays I
# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

#   Its maximum element if all of its elements are consecutive and sorted in ascending order.
#   -1 otherwise.

# You need to find the power of all

# of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


# Example 1:

# Input: nums = [1,2,3,4,3,2,5], k = 3

# Output: [3,4,-1,-1,-1]

# Explanation:

# There are 5 subarrays of nums of size 3:

#   [1, 2, 3] with the maximum element 3.
#   [2, 3, 4] with the maximum element 4.
#    [3, 4, 3] whose elements are not consecutive.
#    [4, 3, 2] whose elements are not sorted.
#    [3, 2, 5] whose elements are not consecutive.

# Example 2:

# Input: nums = [2,2,2,2,2], k = 4

# Output: [-1,-1]

# Example 3:

# Input: nums = [3,2,3,2,3,2], k = 2

# Output: [-1,3,-1,3,-1]


# Constraints:

#    1 <= n == nums.length <= 500
#    1 <= nums[i] <= 105
#    1 <= k <= n

from typing import List


class Solution:
    def findPower(self, nums: List[int], k: int) -> List[int]:
        results = []
        n = len(nums)

        # According to constraints: 1 <= k <= n

        for i in range(n - k + 1):
            # Current subarray is nums[i ... i+k-1]
            is_consecutive_sorted = True

            if k == 1:
                # A single element subarray is always consecutive and sorted.
                # Its power is the element itself.
                results.append(nums[i])
                continue

            # Check for k > 1
            # Iterate from the first element up to the second to last in the window
            for j in range(k - 1):
                # Check if nums[i+j+1] is exactly one greater than nums[i+j]
                if nums[i + j + 1] != nums[i + j] + 1:
                    is_consecutive_sorted = False
                    break

            if is_consecutive_sorted:
                # If consecutive and sorted, the max element is the last one: nums[i+k-1]
                results.append(nums[i + k - 1])
            else:
                results.append(-1)
        return results


# Example Usage:
nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
solution = Solution()
result = solution.findPower(nums, k)
print(result)  # Output: [3, 4, -1, -1, -1]
