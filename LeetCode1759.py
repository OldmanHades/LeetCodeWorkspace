#LeetCode 1769: Minimum Number of Operations to Move All Balls to Each Box:
#You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

#In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

#Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

#Each answer[i] is calculated considering the initial state of the boxes.

 

#Example 1:

#Input: boxes = "110"
#Output: [1,1,3]
#Explanation: The answer for each box is as follows:
#1) First box: you will have to move one ball from the second box to the first box in one operation.
#2) Second box: you will have to move one ball from the first box to the second box in one operation.
#3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

#Example 2:

#Input: boxes = "001011"
#Output: [11,8,5,4,3,4]

 

#Constraints:

#    n == boxes.length
#    1 <= n <= 2000
#    boxes[i] is either '0' or '1'.

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # First pass: Calculate operations for balls to the left
        balls_count = 0  # Number of balls to the left
        balls_sum = 0    # Sum of positions of balls to the left
        for i in range(n):
            answer[i] += i * balls_count - balls_sum  # Operations for balls to the left
            if boxes[i] == '1':
                balls_count += 1
                balls_sum += i
        
        # Second pass: Calculate operations for balls to the right
        balls_count = 0  # Number of balls to the right
        balls_sum = 0    # Sum of positions of balls to the right
        for i in range(n-1, -1, -1):
            answer[i] += balls_sum - i * balls_count  # Operations for balls to the right
            if boxes[i] == '1':
                balls_count += 1
                balls_sum += i
        
        return answer

#Example Usage:
boxes = "110"
print(Solution().minOperations(boxes))
#Output: [1,1,3]