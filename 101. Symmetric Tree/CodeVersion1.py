# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            # Base cases
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            # Check current nodes and their subtrees recursively
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        # Edge case: if the root is None, it's symmetric by definition
        if not root:
            return True
        
        # Call the helper function with left and right subtrees of the root
        return isMirror(root.left, root.right)
