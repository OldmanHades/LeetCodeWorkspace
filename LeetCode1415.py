#LeetCode 1415: The k-th Lexicographical String of All Happy Strings of Length n.
#A happy string is a string that:
#consists only of letters of the set {'a', 'b', 'c'}.
#s[i] != s[i + 1] for all values of i from 1 to s.length - 1. (string is 1-indexed)
#For example strings "abc", "ac", "b" and "abcbabcncb" are all happy strings and strings "aa", "baa", and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
#Return the k-th string of this list or return an empty string if there are less than k happy strings of length n.

# Example 1:
# Input: n =1, k = 3
# Output: "c"
# Explanation: This list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

# Example 2:

#Input: n = 1, k = 4
#Output: ""
#Explanation: There are only 3 happy strings of length 1.

#Example 3:

#Input: n = 3, k = 9
#Output: "cab"
#Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

 

#Constraints:

 #   1 <= n <= 10
 #   1 <= k <= 100


def getKthHappyString(n: int, k: int) -> str:
    """
    Returns the k-th lexicographical happy string of length n.
    A happy string consists only of 'a', 'b', 'c' with no adjacent characters the same.
    Returns "" if there are fewer than k happy strings of length n.

    Args:
        n (int): Length of the happy string (1 <= n <= 10).
        k (int): Position in lexicographical order (1 <= k <= 100).

    Returns:
        str: The k-th happy string or "" if it doesn't exist.
    """
    counter = [0]  # Mutable counter to track number of strings generated
    result = [""]  # Mutable result to store the k-th string

    def backtrack(current, length):
        """
        Recursively builds happy strings and stops when the k-th string is found.

        Args:
            current (str): Current string being built.
            length (int): Current length of the string.

        Returns:
            bool: True if the k-th string is found, False otherwise.
        """
        # Base case: string reaches desired length
        if length == n:
            counter[0] += 1
            if counter[0] == k:
                result[0] = current
                return True
            return False

        # Try appending 'a', 'b', 'c' in lexicographical order
        for char in 'abc':
            # Ensure no adjacent characters are the same
            if not current or char != current[-1]:
                if backtrack(current + char, length + 1):
                    return True
        return False

    # Start backtracking from empty string
    backtrack("", 0)
    return result[0]

# Test the function with the provided examples
if __name__ == "__main__":
    print(getKthHappyString(1, 3))  # Output: "c"
    print(getKthHappyString(1, 4))  # Output: ""
    print(getKthHappyString(3, 9))  # Output: "cab"