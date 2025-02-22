#LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray
# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

# Example 1:
# Input nums = [1, 4, 3, 3, 2]
# Output: 2

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        count = 1
        max_count = 1
        result = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                temp.append(nums[i])
            elif nums[i] < nums[i-1]:
                count = 1
                temp = [nums[i-1], nums[i]]
            else:
                temp = [nums[i]]
            if count > max_count:
                max_count = count
                result = temp
        print("The longest increasing or decreasing subarray is:", result)
        return max_count


# Example Usage:
nums = [1, 5, 6, 7, 3, 8, 22, 88, 77, 44, 32, 19, 1, 5, 7, 9, 11]
print(Solution().longestSubarray(nums))