#LeetCode916: Word Subsets
#You are given two string arrays words1 and words2.
from typing import List
from collections import defaultdict, Counter

#A string b is a subset of string a if every letter in b occurs in a including multiplicity.

#    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

#A string a from words1 is universal if for every string b in words2, b is a subset of a.

#Return an array of all the universal strings in words1. You may return the answer in any order.

 

#Example 1:

#Input: words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

#Output: ["facebook","google","leetcode"]

#Example 2:

#Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

#Output: ["leetcode"]

#Example 3:

#Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

#Output: ["cccbb"]

 

#Constraints:

#    1 <= words1.length, words2.length <= 104
#    1 <= words1[i].length, words2[i].length <= 10
#    words1[i] and words2[i] consist only of lowercase English letters.
#    All the strings of words1 are unique.


#Solution

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)
        for w in words2:
            count_w = Counter(w)
            for c, cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)
        
        res = []
        for w in words1:
            count_w = Counter(w)
            flag = True
            for c, cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res

#Example Usage:
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
#Output = ["facebook","google","leetcode"]

sol = Solution()
print(sol.wordSubsets(words1, words2))

