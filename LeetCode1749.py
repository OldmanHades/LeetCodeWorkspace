#LeetCode 1749: Maximum Absoluite Sum of Any Subarray.
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

#Return the maximum absolute sum of any (possibly empty) subarray of nums.

#Note that abs(x) is defined as follows:

#    If x is a negative integer, then abs(x) = -x.
#    If x is a non-negative integer, then abs(x) = x.

 

#Example 1:

#Input: nums = [1,-3,2,3,-4]
#Output: 5
#Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

#Example 2:

#Input: nums = [2,-5,1,-4,3,-2]
#Output: 8
#Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

 

#Constraints:

#   1 <= nums.length <= 105
#   -104 <= nums[i] <= 104

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        min_pre, max_pre = 0, 0
        cur = 0
        res = 0

        for n in nums:
            cur += n
            # Update result by comparing with current max absolute difference
            res = max(res, max(abs(cur - min_pre), abs(cur - max_pre)))
            min_pre = min(min_pre, cur)
            max_pre = max(max_pre, cur)
        return res


#Example Usage:
nums = [1,-3,2,3,-4]
print(Solution().maxAbsoluteSum(nums))

#Example Usage 2:
nums = [2,-5,1,-4,3,-2]
print(Solution().maxAbsoluteSum(nums))
