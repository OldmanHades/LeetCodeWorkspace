#LeetCode 2226: Maximum Candies Allocated to K Children
#You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

#You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

#Return the maximum number of candies each child can get.

#Example 1:

#Input: candies = [5,8,6], k = 3
#Output: 5
#Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

#Example 2:

#Input: candies = [2,5], k = 11
#Output: 0
#Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

#Constraints:

#    1 <= candies.length <= 105
#    1 <= candies[i] <= 107
#    1 <= k <= 1012

#Solution:

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        # Edge case: If the total number of candies is less than k,
        # it's impossible to distribute at least 1 candy to each child
        total_candies = sum(candies)
        if total_candies < k:
            return 0
        
        # Binary search to find the maximum number of candies each child can get
        # The lower bound is 1 (minimum candies a child can get)
        # The upper bound is the maximum pile size (or total/k if that's smaller)
        left = 1
        right = min(max(candies), total_candies // k)
        
        result = 0
        
        while left <= right:
            # Try the middle value as our candidate answer
            mid = (left + right) // 2
            
            # Check if we can give 'mid' candies to at least k children
            children_served = self.can_serve_children(candies, mid)
            
            if children_served >= k:
                # We can serve at least k children with 'mid' candies each
                # This is a potential answer, but let's try to find a larger one
                result = mid
                left = mid + 1
            else:
                # We cannot serve k children with 'mid' candies each
                # We need to reduce the number of candies per child
                right = mid - 1
                
        return result
    
    def can_serve_children(self, candies: list[int], candies_per_child: int) -> int:
        """
        Returns the number of children we can serve if each child gets exactly
        candies_per_child candies.
        """
        total_children = 0
        
        for pile in candies:
            # Calculate how many children we can serve from this pile
            # Each child gets exactly candies_per_child candies
            total_children += pile // candies_per_child
            
        return total_children


# Test code
if __name__ == "__main__":
    print("Starting tests...")
    sol = Solution()
    
    # Test with example 1
    # candies = [5,8,6], k = 3
    # Expected output: 5
    test1_candies = [5, 8, 6]
    test1_k = 3
    test1_result = sol.maximumCandies(test1_candies, test1_k)
    print(f"Test 1: candies = {test1_candies}, k = {test1_k}")
    print(f"Result: {test1_result}")
    print(f"Expected: 5")
    print()
    
    # Test with example 2
    # candies = [2,5], k = 11
    # Expected output: 0
    test2_candies = [2, 5]
    test2_k = 11
    test2_result = sol.maximumCandies(test2_candies, test2_k)
    print(f"Test 2: candies = {test2_candies}, k = {test2_k}")
    print(f"Result: {test2_result}")
    print(f"Expected: 0")
    print()
    
    # Additional test
    # candies = [1,2,3,4,5], k = 6
    # Expected output: 2
    test3_candies = [1, 2, 3, 4, 5]
    test3_k = 6
    test3_result = sol.maximumCandies(test3_candies, test3_k)
    print(f"Test 3: candies = {test3_candies}, k = {test3_k}")
    print(f"Result: {test3_result}")
    print(f"Expected: 2 (we can create 6 piles of size 2)")
