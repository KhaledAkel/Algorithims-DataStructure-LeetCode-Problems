# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, "L", 0)]  # Each element in the stack is a tuple (node, direction, length)
        max_length = 0

        while stack:
            node, direction, length = stack.pop()

            max_length = max(max_length, length)

            if direction == "L":
                if node.left:
                    stack.append((node.left, "R", length + 1))
                if node.right:
                    stack.append((node.right, "L", 1))
            else:
                if node.right:
                    stack.append((node.right, "L", length + 1))
                if node.left:
                    stack.append((node.left, "R", 1))

        return max_length
