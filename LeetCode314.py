#LeetCode 314: Binary Tree Vertical Order Traversal
#Given the root of a binary tree, return the vertical order traversal of its nodes, i.e., the nodes that are vertically aligned.

#Example 1:

#Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]

#Example 2:

#Input: root = [3,9,8,4,0,1,7]
#Output: [[4],[9],[3,0,1],[8],[7]]

#Example 3:

#Input: root = [3,9,8,4,0,1,7]
#Output: [[4],[9],[3,0,1],[8],[7]]

#Constraints:

#    The number of nodes in the tree will be in the range [1, 1000].
#    0 <= Node.val <= 1000
#    The values of the nodes in the tree are unique.

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Dictionary to store nodes at each vertical level
        vertical_levels = defaultdict(list)
        
        # Perform level order traversal (BFS)
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            vertical_levels[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Sort the levels by vertical order
        sorted_levels = sorted(vertical_levels.items())
        
        return [nodes for _, nodes in sorted_levels]

if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Example 1:", Solution().verticalOrder(root1))  # Expected [[9],[3,15],[20],[7]]

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(0)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(7)
    print("Example 2:", Solution().verticalOrder(root2))  # Expected [[4],[9],[3,0,1],[8],[7]]
