#LeetCode 2461: Maximum Sum of Distinct Subarrays With Length K
#You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

#    The length of the subarray is k, and
#    All the elements of the subarray are distinct.

#Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,5,4,2,9,9,9], k = 3
#Output: 15
#Explanation: The subarrays of nums with length 3 are:
#- [1,5,4] which meets the requirements and has a sum of 10.
#- [5,4,2] which meets the requirements and has a sum of 11.
#- [4,2,9] which meets the requirements and has a sum of 15.
#- [2,9,9] which does not meet the requirements because the element 9 is repeated.
#- [9,9,9] which does not meet the requirements because the element 9 is repeated.
#We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

#Example 2:

#Input: nums = [4,4,4], k = 3
#Output: 0
#Explanation: The subarrays of nums with length 3 are:
#- [4,4,4] which does not meet the requirements because the element 4 is repeated.
#We return 0 because no subarrays meet the conditions.

 

#Constraints:

#    1 <= k <= nums.length <= 105
#    1 <= nums[i] <= 105

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # If k is larger than array length, no valid subarray exists
        if k > len(nums):
            return 0

        count = {}         # Tracks frequency of each number in the window
        current_sum = 0    # Sum of elements in the current window
        max_sum = 0        # Maximum sum found among valid windows
        left = 0           # Left index of the sliding window

        for right, value in enumerate(nums):
            # Add the new element on the right
            count[value] = count.get(value, 0) + 1
            current_sum += value

            # If there's a duplicate, shrink window from the left
            while count[value] > 1:
                left_val = nums[left]
                count[left_val] -= 1
                current_sum -= left_val
                left += 1

            # Once window size reaches k, consider it and then slide forward
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                # Remove the leftmost element to prepare for next window
                left_val = nums[left]
                count[left_val] -= 1
                current_sum -= left_val
                left += 1

        return max_sum


# Example Usage and Debugging
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 5, 4, 2, 9, 9, 9]
    k1 = 3
    print("Example 1 Output:", solution.maximumSubarraySum(nums1, k1))  # Expected: 15

    # Example 2
    nums2 = [4, 4, 4]
    k2 = 3
    print("Example 2 Output:", solution.maximumSubarraySum(nums2, k2))  # Expected: 0
