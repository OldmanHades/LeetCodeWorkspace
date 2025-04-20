#LeetCode 1475: Final Prices With a Special Discount in a Shop
#You are given an integer array prices where prices[i] is the price of the ith item in a shop.

#There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

#Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.



#Example 1:

#Input: prices = [8,4,6,2,3]
#Output: [4,2,4,2,3]
#Explanation:
#For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
#For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
#For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
#For items 3 and 4 you will not receive any discount at all.

#Example 2:

#Input: prices = [1,2,3,4,5]
#Output: [1,2,3,4,5]
#Explanation: In this case, for all items, you will not receive any discount at all.

#Example 3:

#Input: prices = [10,1,1,6]
#Output: [9,0,1,6]

#Constraints:

#1 <= prices.length <= 500
#1 <= prices[i] <= 1000

from typing import List

def final_prices(prices: List[int]) -> List[int]:
    """
    Calculates the final prices after applying a special discount.

    For each item i, the discount is the price of the first item j to its right (j > i)
    such that prices[j] <= prices[i]. If no such item exists, there is no discount.

    Args:
        prices: A list of integers representing the initial prices of items.

    Returns:
        A list of integers representing the final prices after applying discounts.
    """
    n = len(prices)
    answer = prices.copy() # Initialize final prices with original prices [1]
    for i in range(n):
        for j in range(i + 1, n):
            # Find the first item j to the right of i with price <= price[i] [1]
            if prices[j] <= prices[i]:
                answer[i] = prices[i] - prices[j] # Apply the discount [1]
                break # Stop searching for discount for item i once found [1]
    return answer # Return the list of final prices [1]

# Example Usage:
# Using the examples provided in the LeetCode problem description [2]

# Example 1
prices1 = [8, 4, 6, 2, 3]
output1 = final_prices(prices1)
print(f"Input: {prices1}")
print(f"Output: {output1}") # Expected: [4, 2, 4, 2, 3] [2]

# Example 2
prices2 = [1, 2, 3, 4, 5]
output2 = final_prices(prices2)
print(f"\nInput: {prices2}")
print(f"Output: {output2}") # Expected: [1, 2, 3, 4, 5] [2]

# Example 3
prices3 = [10, 1, 1, 6]
output3 = final_prices(prices3)
print(f"\nInput: {prices3}")
print(f"Output: {output3}") # Expected: [9, 0, 1, 6] [2]
