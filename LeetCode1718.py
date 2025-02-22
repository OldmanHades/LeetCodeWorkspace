# LeetCode 1718: Construct the Lexicographically Largest Number
# Given an integer n, find a sequence that satisfies the following conditions:
# This integer i occurs once in the sequence.
# Each integer between 2 amd m occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurences of i is exactly i.

#The distance between two numbers on the sequence a[i] and a[j] is the absolute difference of their indices. [j-i].

#Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        size = 2 * n - 1
        res = [0] * size
        used = [False] * (n + 1)

        def backtrack(pos):
            if pos == size:
                return True
            if res[pos] != 0:
                return backtrack(pos + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[pos] = 1
                    used[1] = True
                    if backtrack(pos + 1):
                        return True
                    res[pos] = 0
                    used[1] = False
                else:
                    if pos + num >= size or res[pos + num] != 0:
                        continue
                    res[pos] = num
                    res[pos + num] = num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    res[pos] = 0
                    res[pos + num] = 0
                    used[num] = False
            return False

        backtrack(0)
        return res


# Example Usage:
n = 3
print(Solution().constructDistancedSequence(n))