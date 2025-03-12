#LeetCode 889: Construct Binary Tree from Preorder and Inorder Traversal
#Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

#If there exist multiple answers, you can return any of them.

#Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
#Output: [1,2,3,4,5,6,7]

#Example 2:

#Input: preorder = [1], postorder = [1]
#Output: [1]

#Constraints:

#1 <= preorder.length <= 30
#1 <= preorder[i] <= preorder.length
#All the values of preorder are unique.
#postorder.length == preorder.length
#1 <= postorder[i] <= postorder.length
#All the values of postorder are unique.
#It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

#Solution:
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        """String representation of the tree (inorder traversal)"""
        result = []
        self._inorder_traversal(result)
        return str(result)
    
    def _inorder_traversal(self, result):
        """Helper for inorder traversal"""
        if self.left:
            self.left._inorder_traversal(result)
        result.append(self.val)
        if self.right:
            self.right._inorder_traversal(result)

# Function to print tree level by level
def print_tree_level_order(root):
    if not root:
        return "Empty tree"
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        
        # Check if the level has only None values
        if any(val is not None for val in level):
            result.append(level)
    
    return result

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_val_to_idx = {}
        for i, n in enumerate(postorder):
            post_val_to_idx[n] = i
        
        N = len(preorder)  # Define N as the length of preorder

        def build(i1, i2, j1):
            if i1 > i2:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]
                mid = post_val_to_idx[left_val]
                left_size = mid - j1 + 1
                root.left = build(i1 + 1, i1 + left_size, j1)
                root.right = build(i1 + left_size + 1, i2, mid + 1)
            return root

        return build(0, N - 1, 0)
    
#Example Usage:
preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
tree = Solution().constructFromPrePost(preorder, postorder)
print("Tree (inorder traversal):", tree)
print("Tree level by level:", print_tree_level_order(tree))