#LeetCode 2471: Minimum Number of Operations to Sort a Binary Tree by Level
#You are given the root of a binary tree with unique values.

#In one operation, you can choose any two nodes at the same level and swap their values.

#Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

#The level of a node is the number of edges along the path between it and the root node.

#Example 1:
#Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
#Output: 3
#Explanation:
#- Swap 4 and 3. The 2nd level becomes [3,4].
#- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
#- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
#We used 3 operations so return 3.
#It can be proven that 3 is the minimum number of operations needed.

#Example 2:
#Input: root = [1,3,2,7,6,5,4]
#Output: 3
#Explanation:
#- Swap 3 and 2. The 2nd level becomes [2,3].
#- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
#- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
#We used 3 operations so return 3.
#It can be proven that 3 is the minimum number of operations needed.

#Example 3:
#Input: root = [1,2,3,4,5,6]
#Output: 0
#Explanation: Each level is already sorted in increasing order so return 0.

 

#Constraints:

#    The number of nodes in the tree is in the range [1, 105].
#    1 <= Node.val <= 105
#    All the values of the tree are unique.

#Solution
import collections # Use 'import collections' instead of 'from collections import deque' if using other parts later, or be specific
from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build tree from list (for testing)
# Handles LeetCode's level-order list representation with None for missing nodes
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    # Use collections.deque directly since it's imported at the top
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()

        # Process left child
        if i < len(nodes) and nodes[i] is not None: # Add boundary check for i
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i >= len(nodes):
            break

        # Process right child
        if nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root

# --- Main Solution Class ---

class Solution:
    def _min_swaps_to_sort(self, arr: List[int]) -> int:
        """
        Calculates the minimum number of swaps to sort an array
        using cycle decomposition.
        """
        n = len(arr)
        if n <= 1:
            return 0

        # Create a mapping from value to its original index
        val_to_idx = {val: i for i, val in enumerate(arr)}
        # Create the sorted version of the array
        sorted_arr = sorted(arr)

        visited = [False] * n
        swaps = 0

        for i in range(n):
            # If element is already visited or is in its correct sorted position
            if visited[i] or arr[i] == sorted_arr[i]:
                continue

            # Found an element that is not in its correct place, start cycle detection
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                # Find the value that *should* be at index j in the sorted array
                correct_val_at_j = sorted_arr[j]
                # Find the original index of that correct value in the unsorted array
                j = val_to_idx[correct_val_at_j]
                cycle_size += 1

            # A cycle of size k requires k-1 swaps
            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the minimum operations (swaps) to sort the tree by level.
        """
        if not root:
            return 0

        total_swaps = 0
        # Use collections.deque directly
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            current_level_values = []
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate swaps needed for the current level and add to total
            # Use self._min_swaps_to_sort since it's part of the same class
            total_swaps += self._min_swaps_to_sort(current_level_values)

        return total_swaps


# --- Example Usage (Remains the same, but now uses the top-level definitions) ---
solver = Solution()

print("--- Running Examples ---")

# Example 1
nodes1 = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
root1 = build_tree(nodes1) # Uses the top-level build_tree
print(f"\nExample 1 Input Tree (List): {nodes1}")
result1 = solver.minimumOperations(root1)
print(f"Example 1 Output: {result1}") # Expected: 3

# Example 2
nodes2 = [1, 3, 2, 7, 6, 5, 4]
root2 = build_tree(nodes2)
print(f"\nExample 2 Input Tree (List): {nodes2}")
result2 = solver.minimumOperations(root2)
print(f"Example 2 Output: {result2}") # Expected: 3

# Example 3
nodes3 = [1, 2, 3, 4, 5, 6]
root3 = build_tree(nodes3)
print(f"\nExample 3 Input Tree (List): {nodes3}")
result3 = solver.minimumOperations(root3)
print(f"Example 3 Output: {result3}") # Expected: 0

print("\n--- End Examples ---")