#LeetCode 1800: Maximum Ascending Subarray Sum
# Given an array of positive integers nums, return the maximum ascending subarray sum.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if numsl < numsl+1 < ... < numsr-1 < numsr.

# Example 1:
# Input: nams = [10, 20, 30, 5, 10, 50]
# Output: 65
# Explanation: The subarray [30, 5, 10] has the maximum ascending sum 30 + 5 + 10 = 65.

# Example 2:
# Input: nums = [10, 20, 30, 40, 50]
# Output: 150
# Explanation: The subarray [10, 20, 30, 40, 50] has the maximum ascending sum 10 + 20 + 30 + 40 + 50 = 150.

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0
        current_sum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
        return max_sum


# Example Usage:
nums = [10, 30, 5, 7, 8, 9, 22, 110, 50, 40, 80, 11, 61, 88]
print(Solution().maxAscendingSum(nums))