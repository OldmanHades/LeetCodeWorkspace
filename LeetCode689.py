#LeetCode 689: Maximum Sum of 3 Non-Overlapping Subarrays
#Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

#Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

#Example 1:

#Input: nums = [1,2,1,2,6,7,5,1], k = 2
#Output: [0,3,5]
#Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
#We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.

#Example 2:

#Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
#Output: [0,2,4]

 

#Constraints:

#    1 <= nums.length <= 2 * 104
#    1 <= nums[i] < 216
#    1 <= k <= floor(nums.length / 3)

#Solution:
from typing import List

class Solution:
    """
    Solution for LeetCode 689: Maximum Sum of 3 Non-Overlapping Subarrays.
    """

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Finds three non-overlapping subarrays of length k with the maximum total sum.
        Returns the starting indices of these subarrays.
        """
        n = len(nums)
        # Compute prefix sums for efficient window sum calculation
        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + nums[idx]

        # Calculate sum of every subarray of length k
        k_sums = [0] * (n - k + 1)
        for idx in range(n - k + 1):
            k_sums[idx] = prefix[idx + k] - prefix[idx]

        # left[i] = starting index of max k_sums in [0..i]
        left = [0] * len(k_sums)
        max_idx = 0
        for idx in range(len(k_sums)):
            if k_sums[idx] > k_sums[max_idx]:
                max_idx = idx
            left[idx] = max_idx

        # right[i] = starting index of max k_sums in [i..end]
        right = [0] * len(k_sums)
        max_idx = len(k_sums) - 1
        for idx in range(len(k_sums) - 1, -1, -1):
            if k_sums[idx] >= k_sums[max_idx]:
                max_idx = idx
            right[idx] = max_idx

        # Find best combination of three windows
        result = [0, 0, 0]
        max_total = 0
        # Middle window starting index j from k to len(k_sums)-k
        for j in range(k, len(k_sums) - k):
            i_idx = left[j - k]
            l_idx = right[j + k]
            total = k_sums[i_idx] + k_sums[j] + k_sums[l_idx]
            if total > max_total:
                max_total = total
                result = [i_idx, j, l_idx]
        return result

if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 1, 2, 6, 7, 5, 1]
    k1 = 2
    print("Example 1:")
    print("Input:", nums1, "k =", k1)
    print("Output:", Solution().maxSumOfThreeSubarrays(nums1, k1))
    print("Expected: [0, 3, 5]\n")

    # Example 2
    nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    k2 = 2
    print("Example 2:")
    print("Input:", nums2, "k =", k2)
    print("Output:", Solution().maxSumOfThreeSubarrays(nums2, k2))
    print("Expected: [0, 2, 4]")
