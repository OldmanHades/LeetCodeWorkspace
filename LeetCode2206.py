#LeetCode 2206: Divide Array Into Equal Pairs
#You are given an integer array nums consisting of 2 * n integers.

#You need to divide nums into n pairs such that:

#    Each element belongs to exactly one pair.
#    The elements present in a pair are equal.

#Return true if nums can be divided into n pairs, otherwise return false.


#Example 1:

#Input: nums = [3,2,3,2,2,2]
#Output: true
#Explanation: 
#There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
#If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

#Example 2:

#Input: nums = [1,2,3,4]
#Output: false
#Explanation: 
#There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


#Constraints:

#    nums.length == 2 * n
#    1 <= n <= 500
#    1 <= nums[i] <= 500

#Solution:
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        # Use a dictionary to count the frequency of each number
        frequency = {}
        
        # Count the frequency of each number in the array
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Check if each number appears an even number of times
        for count in frequency.values():
            if count % 2 != 0:
                return False
        
        # If all numbers appear an even number of times, we can form pairs
        return True

# Example usage:
if __name__ == "__main__":
    # Example 1
    nums1 = [3, 2, 3, 2, 2, 2]
    print(f"Example 1: {Solution().divideArray(nums1)}")  # Expected: True
    
    # Example 2
    nums2 = [1, 2, 3, 4]
    print(f"Example 2: {Solution().divideArray(nums2)}")  # Expected: False
    
    # Additional test case
    nums3 = [1, 1, 2, 2, 3, 3]
    print(f"Additional test: {Solution().divideArray(nums3)}")  # Expected: True