#LeetCode 1726: Tuple with Same Product
#Given an array nums, of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, that is, a != b, b != c, and c != d.

# Example 1:
# Input nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples

# Example 2:
# Input nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples

# Import library
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        #Each tuple has 8 permutations
        # Product counts?
        product_cnt = defaultdict(int)#n1 * n2 -> count
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_cnt[product] += 1

    # 1 Count -> 0 pair -> 0 tuples
    # 2 Count -> 1 pair -> 8 tuples 
    # 3 Count -> 2 pairs -> 24 tuples
    # 4 Count -> 3 pairs -> 48 tuples
    # 5 Count -> 4 pairs -> 80 tuples
    # 6 Count -> 5 pairs -> 120 tuples
    # 7 Count -> 6 pairs -> 160 tuples
    # 8 Count -> 7 pairs -> 192 tuples
    # 9 Count -> 8 pairs -> 224 tuples
    
        res = 0
        for cnt in product_cnt.values():
           pairs =(cnt * (cnt - 1)) // 2
           res += 8 * pairs
        return res


        # Example Usage:
# Example Usage:
nums = [1,3,4,5,6,78,12,15,21,27]
print(Solution().tupleSameProduct(nums))