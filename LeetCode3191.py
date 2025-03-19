#LeetCode 3191: Minimum Operations to Make Binary Array Elements Equal to 1.
#You can do the following operation on the array any number of times (possibly zero):

#    Choose any 3 consecutive elements from the array and flip all of them.

#Flipping an element means changing its value from 0 to 1, and from 1 to 0.

#Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

#Example 1:

#Input: nums = [0,1,1,1,0,0]

#Output: 3

#Explanation:
#We can do the following operations:

#    Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
#    Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
#    Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

#Example 2:

#Input: nums = [0,1,1,1]

#Output: -1

#Explanation:
#It is impossible to make all elements equal to 1.

 

#Constraints:

#    3 <= nums.length <= 105
#    0 <= nums[i] <= 1

#Solution:
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1

        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                flip(nums, i)
                flip(nums, i + 1)
                flip(nums, i + 2)
                res += 1
        if not nums[-1] or not nums[-2]:
            return -1
        return res

    #Example Usage:
nums = [0,1,1,1,0,0]
print(Solution().minOperations(nums))
