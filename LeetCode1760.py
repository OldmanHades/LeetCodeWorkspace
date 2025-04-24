#LeetCode 1760: Minimum Limit of Balls in a Bag
#You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

#You can perform the following operation at most maxOperations times:

#    Take any bag of balls and divide it into two new bags with a positive number of balls.
#        For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.

#Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

#Return the minimum possible penalty after performing the operations.

 

#Example 1:

#Input: nums = [9], maxOperations = 2
#Output: 3
#Explanation: 
#- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
#- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
#The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

#Example 2:

#Input: nums = [2,4,8,2], maxOperations = 4
#Output: 2
#Explanation:
#- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
#- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
#- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
#- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
#The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.

 

#Constraints:

#    1 <= nums.length <= 105
#    1 <= maxOperations, nums[i] <= 109

from typing import List

def minimum_size(nums: List[int], maxOperations: int) -> int:
    """
    Find the minimum possible maximum bag size (penalty) after at most maxOperations splits.
    """

    def can_divide(limit: int) -> bool:
        # Check if we can ensure all bags ≤ limit with ≤ maxOperations splits
        ops = 0
        for balls in nums:
            # Each split reduces a bag of size `balls` into chunks ≤ limit.
            # Number of splits needed is ceil(balls/limit) − 1, equivalently (balls-1)//limit
            ops += (balls - 1) // limit
            if ops > maxOperations:
                return False
        return True

    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example usage and proof of correctness:
if __name__ == "__main__":
    # Example 1:
    # nums = [9], maxOperations = 2
    # Expected output: 3
    print(minimum_size([9], 2))     # 3

    # Example 2:
    # nums = [2,4,8,2], maxOperations = 4
    # Expected output: 2
    print(minimum_size([2,4,8,2], 4))  # 2