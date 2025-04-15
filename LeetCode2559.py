#LeetCode 2559: Count Vowel Strings in Ranges
#You are given a 0-indexed array of strings words and a 2D array of integers queries.

#Each query queries[i] = [li, ri] asks us to find the number of strings present at the indices ranging from li to ri (both inclusive) of words that start and end with a vowel.

#Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

#Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

#Example 1:

#Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
#Output: [2,3,0]
#Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
#The answer to the query [0,2] is 2 (strings "aba" and "ece").
#The answer to the query [1,4] is 3 (strings "ece", "aa", "e").
#The answer to the query [1,1] is 0.
#We return [2,3,0].

#Example 2:

#Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
#Output: [3,2,1]
#Explanation: Every string satisfies the conditions, so we return [3,2,1].

 

#Constraints:

#    1 <= words.length <= 105
#    1 <= words[i].length <= 40
#    words[i] consists only of lowercase English letters.
#    sum(words[i].length) <= 3 * 105
#    1 <= queries.length <= 105
#    0 <= li <= ri < words.length

# Solution
from typing import List


def countVowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    """
    Counts the number of strings in the given ranges that start and end with a vowel.
    Uses prefix sums for efficient query answering.
    Args:
        words (List[str]): The list of words.
        queries (List[List[int]]): The list of queries, each as [li, ri].
    Returns:
        List[int]: The answer for each query.
    """
    # Define the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Helper function to check if a word starts and ends with a vowel
    def is_vowel_string(word: str) -> bool:
        """Check if the word starts and ends with a vowel."""
        return word[0] in vowels and word[-1] in vowels

    # Precompute a prefix sum of vowel-string counts
    n = len(words)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if is_vowel_string(words[i]) else 0)

    # Process each query using the prefix sum
    ans = []
    for li, ri in queries:
        # The number of vowel-strings in [li, ri] is prefix[ri+1] - prefix[li]
        ans.append(prefix[ri + 1] - prefix[li])
    return ans


if __name__ == "__main__":
    # Example 1
    words1 = ["aba", "bcb", "ece", "aa", "e"]
    queries1 = [[0, 2], [1, 4], [1, 1]]
    # Expected output: [2, 3, 0]
    print("Example 1 Output:", countVowelStrings(words1, queries1))

    # Example 2
    words2 = ["a", "e", "i"]
    queries2 = [[0, 2], [0, 1], [2, 2]]
    # Expected output: [3, 2, 1]
    print("Example 2 Output:", countVowelStrings(words2, queries2))
