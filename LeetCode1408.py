#LeetCode 1408: String Matching in an Array
#Given an array of string words, return all strings in words that are a

#of another word. You can return the answer in any order.

 

#Example 1:

#Input: words = ["mass","as","hero","superhero"]
#Output: ["as","hero"]
#Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
#["hero","as"] is also a valid answer.

#Example 2:

#Input: words = ["leetcode","et","code"]
#Output: ["et","code"]
#Explanation: "et", "code" are substring of "leetcode".

#Example 3:

#Input: words = ["blue","green","bu"]
#Output: []
#Explanation: No string of words is substring of another string.

 

#Constraints:

#    1 <= words.length <= 100
#    1 <= words[i].length <= 30
#    words[i] contains only lowercase English letters.
#    All the strings of words are unique.

#Solution:
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

#Example Usage:
words = ["mass","as","hero","superhero"]
print(Solution().stringMatching(words)) #Output: ["as","hero"]
