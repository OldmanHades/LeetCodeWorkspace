#LeetCode 416: Partition Equal Subset Sum
#You are given an array of positive integers nums.

#Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

#Example 1:

#Input: nums = [1,2,3,4]
#Output: true
#Explanation: The array can be partitioned as [1, 4] and [2, 3].

#Example 2:

#Input: nums = [1,2,3,4,5]
#Output: false

#Constraints:

#    1 <= nums.length <= 100
#    1 <= nums[i] <= 50

#Solution
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

#Example Usage:
nums = [1,2,3,4]
print(Solution().canPartition(nums))
#Output: True
