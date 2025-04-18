# LeetCode 1014: Best Sightseeing Pair

# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

# Example 1:

# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

# Example 2:

# Input: values = [1,2]
# Output: 2

# Constraints:

#     2 <= values.length <= 5 * 104
#     1 <= values[i] <= 1000

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Calculates the maximum score of a sightseeing pair (i, j) with i < j.

        The score is defined as values[i] + values[j] + i - j.
        This can be rewritten by grouping terms involving i and j separately:
        score = (values[i] + i) + (values[j] - j).

        To maximize this score for a pair (i, j) where i < j, we can iterate
        through all possible ending indices `j` (from 1 to n-1). For a fixed `j`,
        the term `values[j] - j` is constant. To maximize the total score, we
        need to maximize the term `values[i] + i` over all possible starting
        indices `i` where `i < j`.

        We can maintain a variable that tracks the maximum value of `values[k] + k`
        seen so far, for all indices `k` that are less than the current index `j`.

        Args:
            values: A list of integers representing the value of each spot.

        Returns:
            The maximum score possible for any pair (i, j) with i < j.
        """
        n = len(values)

        # The problem guarantees n >= 2, so we don't need a separate n < 2 check.
        # The loop starting at j=1 correctly covers the minimum case n=2.

        # max_val_plus_i stores the maximum value of values[k] + k for k < current_j.
        # Initialize with the first element (k=0).
        max_val_plus_i = values[0] + 0

        # Initialize max_score. Scores can potentially be negative (e.g., small values, large distance).
        # Initialize with a value lower than any possible score, or use the score of the first pair (0, 1).
        # Using negative infinity is a safe way to ensure the first calculated score updates max_score.
        max_score = -float('inf')

        # Iterate through possible ending spots j, starting from the second spot (index 1)
        # because i must be less than j.
        for j in range(1, n):
            # For the current index j, the potential score with the best possible i < j is:
            # (max_values_i_plus_i_for_i_less_than_j) + (values[j] - j)
            current_score_for_j = max_val_plus_i + (values[j] - j)

            # Update the overall maximum score found so far
            max_score = max(max_score, current_score_for_j)

            # Before moving to the next index (j+1), we need to update max_val_plus_i.
            # The maximum value of values[k] + k for k < j+1 could be either:
            # 1. The previous maximum for k < j (which is stored in max_val_plus_i)
            # 2. The value for the current index j (values[j] + j)
            # So, we update max_val_plus_i to include the possibility of index j being the 'i' for future 'j's.
            max_val_plus_i = max(max_val_plus_i, values[j] + j)

        return max_score

# --- Example Usage ---

# Example 1
values1 = [8, 1, 5, 2, 6]
expected1 = 11
result1 = Solution().maxScoreSightseeingPair(values1)
print(f"Input: {values1}")
print(f"Output: {result1}")
print(f"Expected: {expected1}")
print(f"Test Pass: {result1 == expected1}")

print("-" * 20)

# Example 2
values2 = [1, 2]
expected2 = 2
result2 = Solution().maxScoreSightseeingPair(values2)
print(f"Input: {values2}")
print(f"Output: {result2}")
print(f"Expected: {expected2}")
print(f"Test Pass: {result2 == expected2}")

print("-" * 20)

# Additional Test Case: max score from non-adjacent points
values3 = [1, 7, 3, 9, 2]
# i=1, j=3: values[1]+values[3]+1-3 = 7+9+1-3 = 14
expected3 = 14
result3 = Solution().maxScoreSightseeingPair(values3)
print(f"Input: {values3}")
print(f"Output: {result3}")
print(f"Expected: {expected3}")
print(f"Test Pass: {result3 == expected3}")

print("-" * 20)

# Additional Test Case: involves potentially smaller scores
values4 = [10, 1, 1, 1]
# i=0, j=1: 10+1+0-1 = 10
# i=0, j=2: 10+1+0-2 = 9
# i=0, j=3: 10+1+0-3 = 8
# i=1, j=2: 1+1+1-2 = 1
# i=1, j=3: 1+1+1-3 = 0
# i=2, j=3: 1+1+2-3 = 1
expected4 = 10
result4 = Solution().maxScoreSightseeingPair(values4)
print(f"Input: {values4}")
print(f"Output: {result4}")
print(f"Expected: {expected4}")
print(f"Test Pass: {result4 == expected4}")

print("-" * 20)

# Additional Test Case: Increasing values
values5 = [1, 2, 3, 4, 5]
# i=3, j=4: 4+5+3-4 = 8
expected5 = 8
result5 = Solution().maxScoreSightseeingPair(values5)
print(f"Input: {values5}")
print(f"Output: {result5}")
print(f"Expected: {expected5}")
print(f"Test Pass: {result5 == expected5}")
