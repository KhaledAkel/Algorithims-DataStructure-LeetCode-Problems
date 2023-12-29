# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, [])]
        goal = [[], []]

        while stack:
            node, ancestors = stack.pop()

            if not node:
                continue
            
            if node == p:
                goal[0] = ancestors + [node]
            
            if node == q:
                goal[1] = ancestors + [node]

            stack.append((node.left, ancestors + [node]))
            stack.append((node.right, ancestors + [node]))

        result = None
        for a, b in zip(goal[0], goal[1]):
            if a == b:
                result = a

        return result
