# LeetCode 862: Shortest SubArray with Sum at Least K
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

# A subarray is a contiguous part of an array.


# Example 1:

# Input: nums = [1], k = 1
# Output: 1

# Example 2:

# Input: nums = [1,2], k = 4
# Output: -1

##Input: nums = [2,-1,2], k = 3
# Output: 3


# Constraints:

#    1 <= nums.length <= 105
#   -105 <= nums[i] <= 105
#    1 <= k <= 109

# Solution:
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        prefix_sum = 0
        prefix_sum_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum - k in prefix_sum_map:
                min_length = min(min_length, i - prefix_sum_map[prefix_sum - k])

            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return min_length if min_length != float("inf") else -1

    # Example Usage:


nums = [1]  # Ouput = 1
k = 1
print(Solution().shortestSubarray(nums, k))

nums = [1, 2]  # Output = -1
k = 4
print(Solution().shortestSubarray(nums, k))
