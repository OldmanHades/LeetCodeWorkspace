#LeetCode 2401: Longest Nice Subarray
# You are given an array of positive integers nums.
# A subarray of nums is called nice if there are no repeated values in it.
# Return the length of the longest nice subarray of nums.
# A subarray is an array that can be derived from another array by deleting some elements of it without changing the order of the remaining elements.

# Example 1:

# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.

# Example 2:

# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


# Import library
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0 #bitmask
        l = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            res = max(res,r - l + 1)
            cur = cur | nums[r]
        return res
# Example Usage:
if __name__ == "__main__":
    nums = [1,3,8,48,10]
    print(Solution().longestNiceSubarray(nums))
