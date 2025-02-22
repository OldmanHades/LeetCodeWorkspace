# LeetCode 1079: Letter Tile Possibilities
# You have n tiles, where each tile has one letter tiles [i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

#Exmaple 1:
# Input: tiles = "AAB"
# Output: 8

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        
        def backtrack():
            res = 0

            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1

            return res

        return backtrack()





#Example Usage:
tiles = "AAABBC"
result = Solution().numTilePossibilities(tiles)
print(f"Number of possible non-empty sequences of letters: {result}")