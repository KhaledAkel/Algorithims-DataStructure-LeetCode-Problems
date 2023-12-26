# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]
        count = 0

        while stack:
            node, MAX = stack.pop()
            if node:
                if node.val >= MAX:
                    count += 1
                MAX = max(MAX, node.val)
                stack.append((node.left, MAX))
                stack.append((node.right, MAX)) 
        return count
