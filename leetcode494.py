# LeetCode 494: Target Sum
# You are given an integer array nums and an integer target
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then
# concatenate all the integers


def findTargetSumWays(nums, target):
    """
    Finds the number of ways to assign '+' or '-' to each number in nums such that the sum equals target.
    """
    count = 0
    n = len(nums)

    def backtrack(index, current_sum):
        nonlocal count
        if index == n:
            if current_sum == target:
                count += 1
            return

        backtrack(index + 1, current_sum + nums[index])
        backtrack(index + 1, current_sum - nums[index])

    backtrack(0, 0)
    return count


# Example usage
nums = [2, 2, 2, 2, 2]
target = 6
result = findTargetSumWays(nums, target)
print(f"Number of ways to reach target {target}: {result}")
