#LeetCode 2161: Paritition Array According to Given Pivot
#You are given a 0-indexed integer array nums and an integer pivot. Rearrage nums such that the following conditions are met:
#Every element less than pivot appears before every element greater than pivot.
#Every element equal to pivot appears in between the elements less than and greater than pivot.
#The relative order of the elements less than pivot and elements greater than pivot is maintained.
#Return nums after the rearrangement.

#Example 1:
#Input nums = [9,12,5,10,14,3,10] pivot = 10
#Output: [9,5,3,10,10,12,14]

#Example 2:
#Input nums = [-3,4,3,2], pivot = 2
#Output: [-3,2,4,3]


class Solution:
    def partitionArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        p = []
        greater = []

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                p.append(n)
        
        return less + p + greater
    
#Example Usage:
if __name__ == "__main__":
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    print(Solution().partitionArray(nums, pivot))