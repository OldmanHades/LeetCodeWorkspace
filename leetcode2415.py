# LeetCode 2415. Reverse Odd Levels of a Perfect Binary Tree
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.

# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

# The level of a node is the number of edges along the path between it and the root node.
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            current_level_nodes = []
            next_level_nodes = deque()

            # Process nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            # Reverse values at odd levels
            if level % 2 != 0:
                values = [node.val for node in current_level_nodes]
                reversed_values = values[::-1]
                for i in range(len(current_level_nodes)):
                    current_level_nodes[i].val = reversed_values[i]

            queue = next_level_nodes
            level += 1

        return root

    # Create a sample tree


root = TreeNode(7)
root.left = TreeNode(7)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(8)
root.right.left = TreeNode(9)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(2)
root.left.right.right = TreeNode(2)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(3)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(4)

solution = Solution()
modified_root = solution.reverseOddLevels(root)


# You can then perform a level-order traversal on modified_root to verify the results
def print_level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(current_level)


print_level_order(modified_root)
# Expected Output (values at odd levels are reversed):
# [7]
# [7, 7]
# [9, 9, 8, 8]
# [1, 1, 2, 2, 3, 3, 4, 4]
