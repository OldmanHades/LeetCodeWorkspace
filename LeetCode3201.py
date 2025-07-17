'''You are given an integer array nums. A subsequence sub of nums with length x is valid if it satisfies the condition that the parity (modulo 2) of the sum of every pair of consecutive elements is the same: (sub + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x-2] + sub[x-1]) % 2.

The task is to return the length of the longest such valid subsequence. A subsequence is derived by deleting some or no elements from the array without changing the order of the remaining elements.

Constraints:

2 <= nums.length <= 2 * 10^5

1 <= nums[i] <= 10^7

Examples:

Input: nums = [1][2][6][3]
Output: 3
Explanation: The entire array [1][2][6][3] is valid since all consecutive sums have even parity (e.g., (1+2)%2=1, (2+3)%2=1, (3+4)%2=1).

Input: nums = [1][2][1][1][2][1][2]
Output: 6
Explanation: A valid subsequence like [1][2][1][2][1][2] satisfies the condition.

Input: nums = [1][6]
Output: 2
Explanation: [1][6] is valid with (1+3)%2=0
'''
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        dp = [[0] * 2 for _ in range(2)]
        ans = 0
        for num in nums:
            num %= 2
            for i in range(2):
                dp[i][num] = dp[num][i] + 1
                ans = max(ans, dp[i][num])
        return ans
#Example Usage:
nums = [1,2,6,3]
sol = Solution()
print(sol.maximumLength(nums))

