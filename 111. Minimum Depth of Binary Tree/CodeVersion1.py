# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If either the left or right subtree is empty, return the depth of the non-empty subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both subtrees are non-empty, return the minimum depth among them
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
