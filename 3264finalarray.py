# Leetcode 3264. Final Array After K Multiplications Operations
# Given an interger array nums, an integer k, and an integer multiplier, return the final array after performing k operations.
# You need to perform K operations on nums, In each operation.
# Find the minimum value in x nums. If there are multiple occurrences of the minimum value, select the one that appears first
# Replace the selected minimum value x with x * multiplier
# Return an integer array denoting the final state of nums after performing all k operations

# input nums = [2, 1, 3, 5, 6]
# k = 5
# multiplier = 2
# Output: [8, 4, 6, 5, 5]

# Output: [8, 4, 6, 5, 5]

import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        res = nums[::]

        min_heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            n, i = heapq.heappop(min_heap)
            res[i] *= multiplier
            heapq.heappush(min_heap, (res[i], i))

        return res


if __name__ == "__main__":
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    s = Solution()
    print(s.getFinalState(nums, k, multiplier))
