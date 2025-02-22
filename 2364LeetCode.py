#LeetCode 2364: Count Number of Bad Pairs
# You are given a 0-indexed integer array nums. A pair of indices [i, j] is a bad pair if nums[i] == nums[j] and i < j. Return the number of bad pairs.
# Ruturn the number of bad pairs.


#n^2 for every number and every pair?

#Preprocess?
#Find the good pairs?
#Total pairs - good pairs = bad pairs

# Example 1:
# Input nums = [4,1,3,3]
# Output: 5

from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        # Calculate total number of pairs using combination formula: n*(n-1)//2
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        # good_pairs counts pairs (i, j) with i < j where nums[i] - i == nums[j] - j
        good_pairs = 0
        count = defaultdict(int)
        
        # Iterate through each index, using the adjusted value as key
        for i in range(n):
            key = nums[i] - i  # adjust the value with index to group matching pairs
            good_pairs += count[key]  # add all previous indices that form a good pair with current index
            count[key] += 1
        
        # Bad pairs are all pairs minus the good pairs
        return total_pairs - good_pairs


# Example Usage:
nums = [5,7,2,5,7,1]
#nums = [4,1,3,3]
print(Solution().countBadPairs(nums))