# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        if root == None:
            return None
        while stack:
            node = stack.pop()
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

        
