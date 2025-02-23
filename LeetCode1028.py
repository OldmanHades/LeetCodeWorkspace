#LeetCode 1028: Recover a Tree From Preorder Traversal
# We run a preorder depth first search DFS on the root of a binary tree. At each node in this traversal, we output D dashes where D is the depth of this node, then we output the value of this node. If the depth of node D, the depth of it's immediate child is D + 1. The depth of the root node is 0.
# If a node only has one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its' root.

# Example 1:
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]



# Example Usage:
# Input: traversal = "1-2--3---4-5--6---7"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def recoverFromPreorder(traversal: str) -> TreeNode:
    stack = []
    i = 0
    n = len(traversal)
    while i < n:
        depth = 0
        # Count dashes to determine the depth
        while i < n and traversal[i] == '-':
            depth += 1
            i += 1
        # Parse the number value
        val_start = i
        while i < n and traversal[i].isdigit():
            i += 1
        val = int(traversal[val_start:i])
        node = TreeNode(val)
        # Adjust the stack to have the correct parent at top
        while len(stack) > depth:
            stack.pop()
        if stack:
            if stack[-1].left is None:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
    # The root is the first element in the stack
    while len(stack) > 1:
        stack.pop()
    return stack[0] if stack else None


def treeToList(root: TreeNode) -> list:
    # Level order traversal to convert tree into list form
    if not root:
        return []
    result = []
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
         result.pop()
    return result


if __name__ == '__main__':
    # Example Usage:
    traversal = "1-2--3---4-5--6---7"
    root = recoverFromPreorder(traversal)
    output = treeToList(root)
    print(output)