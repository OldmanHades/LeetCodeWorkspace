#LeetCode 1123: Lowest Common Ancestor of Deepest Leaves
#Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

#Recall that:

#    The node of a binary tree is a leaf if and only if it has no children
#    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
#    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
#Input: root = [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#Explanation: We return the node with value 2, colored in yellow in the diagram.
#The nodes coloured in blue are the deepest leaf-nodes of the tree.
#Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

#Example 2:

#Input: root = [1]
#Output: [1]
#Explanation: The root is the deepest node in the tree, and it's the lca of itself.

#Example 3:

#Input: root = [0,1,3,null,2]
#Output: [2]
#Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

#Constraints:

#    The number of nodes in the tree will be in the range [1, 1000].
#    0 <= Node.val <= 1000
#    The values of the nodes in the tree are unique.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Return (LCA, height)
        def dfs(node, height):
            if not node:
                return (None, 0)
            left_node, left_height = dfs(node.left, height + 1)
            right_node, right_height = dfs(node.right, height + 1)
            if left_height == right_height:
                return (node, left_height + 1)
            elif left_height < right_height:
                return (right_node, right_height + 1)
            else:
                return (left_node, left_height + 1)
        node, _ = dfs(root, 0)
        return node

#Example Usage:

# Helper function to build a tree from list representation
def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Example 1
values = [3,5,1,6,2,0,8,None,None,7,4]
root = build_tree(values)

# Create solution instance and find the LCA of deepest leaves
solution = Solution()
result = solution.lcaDeepestLeaves(root)
print(f"Example 1:")
print(f"Input: root = {values}")
print(f"Output: LCA of deepest leaves has value {result.val}")
print(f"Expected: 2 (as described in the problem)")

# Verify Example 2
values2 = [1]
root2 = build_tree(values2)
result2 = solution.lcaDeepestLeaves(root2)
print(f"\nExample 2:")
print(f"Input: root = {values2}")
print(f"Output: LCA of deepest leaves has value {result2.val}")
print(f"Expected: 1 (as described in the problem)")

# Verify Example 3
values3 = [0,1,3,None,2]
root3 = build_tree(values3)
result3 = solution.lcaDeepestLeaves(root3)
print(f"\nExample 3:")
print(f"Input: root = {values3}")
print(f"Output: LCA of deepest leaves has value {result3.val}")
print(f"Expected: 2 (as described in the problem)")
