# LeetCode 3151: Special Array
# Ab array is considered special if every pair of its adjacent elements contain two numbers with different parity. If one element is even then the other has to be odd.
# You are given an array of integers nums. Return true if name is a special array, otherwise, return false.

# Example 1:
# Input nums = [1]
# Output: true
# Explanation: There is only one element, so the answer is true.

# Example 2:
# Input nums = [2, 1, 4]
# Output: true
# Explanation: No two adjacent elements have the same parity.

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] & 1 == nums[i - 1] & 1:
                return False
        return True

# Example usage 3:
nums = [5, 2, 4, 1, 8]
print(Solution().isArraySpecial(nums))

