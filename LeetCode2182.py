#LeetCode 2182: Construct String With Repeat Limit
#You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

#Return the lexicographically largest repeatLimitedString possible.

#A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

#Example 1:

#Input: s = "cczazcc", repeatLimit = 3
#Output: "zzcccac"
#Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
#The letter 'a' appears at most 1 time in a row.
#The letter 'c' appears at most 3 times in a row.
#The letter 'z' appears at most 2 times in a row.
#Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
#The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
#Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

#Example 2:

#Input: s = "aababab", repeatLimit = 2
#Output: "bbabaa"
#Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
#The letter 'a' appears at most 2 times in a row.
#The letter 'b' appears at most 2 times in a row.
#Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
#The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
#Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

 

#Constraints:

#    1 <= repeatLimit <= s.length <= 105
#    s consists of lowercase English letters.

#Solution:

import collections
import heapq

def repeat_limited_string(s: str, repeat_limit: int) -> str:
    """
    Construct the lexicographically largest string using the characters of s
    such that no character appears more than repeat_limit times consecutively.
    """
    # Count the frequency of each character in the input string
    freq = collections.Counter(s)
    # Build a max-heap using negative ASCII values to sort by largest character
    heap = [(-ord(ch), ch, count) for ch, count in freq.items()]
    heapq.heapify(heap)

    result_parts = []  # List to collect chunks of the resulting string

    # Continue constructing until no characters remain
    while heap:
        neg_ord, ch, count = heapq.heappop(heap)
        # Determine how many times we can append this character consecutively
        use = min(count, repeat_limit)
        # Append the allowed number of this character
        result_parts.append(ch * use)
        count -= use

        # If there are leftover occurrences of this character
        if count > 0:
            if not heap:
                # No other character to separate, so break out
                break
            # Pop the next largest character to insert as a separator
            neg_ord2, ch2, count2 = heapq.heappop(heap)
            # Append exactly one of this second character
            result_parts.append(ch2)
            count2 -= 1
            # Push back the second character if it still has remaining count
            if count2 > 0:
                heapq.heappush(heap, (neg_ord2, ch2, count2))
            # Push back the first character with its remaining count
            heapq.heappush(heap, (neg_ord, ch, count))

    # Join all parts and return the final string
    return ''.join(result_parts)

if __name__ == "__main__":
    # Example 1
    s1, limit1 = "cczazcc", 3
    print(f"Input: s = {s1!r}, repeatLimit = {limit1}")
    print("Output:", repeat_limited_string(s1, limit1))  # Expected: "zzcccac"
    print()

    # Example 2
    s2, limit2 = "aababab", 2
    print(f"Input: s = {s2!r}, repeatLimit = {limit2}")
    print("Output:", repeat_limited_string(s2, limit2))  # Expected: "bbabaa"
