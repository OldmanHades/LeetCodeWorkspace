# LeetCode 1752: Check if Array is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of times. Otherwise, return false.

# Example 1:
# Input nums = [3,4,5,1,2]
# Output: true
# Explanation: The array was originally [1,2,3,4,5] which is sorted and rotated.

# Example 2:
# Input nums = [2,1,2,5,3,4]
# Output: false
# Explanation: The array was not originally sorted and rotated.

# Example 3:
# Input nums = [3,4,5,1,2]
# Output: false
# Explanation: The array was not originally sorted and rotated.

class Solution:
    def check(self, nums: list[int]) -> bool:
        N = len(nums)
        count = 1
        if N == 1:
            return True
        for i in range(1, 2 * N):
           if nums[(i -1) % N] <= nums[i % N]:
               count += 1
        else:
            count = 1
        if count == N:
            return True
        return False

# Example Usage:
nums = [3,4,5,1,2]
print(Solution().check(nums))