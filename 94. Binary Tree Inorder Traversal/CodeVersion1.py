# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def inorderTrav(root):
            nonlocal inorder
            if not root:
                return 
            inorderTrav(root.left)
            inorder.append(root.val)
            inorderTrav(root.right)
        inorderTrav(root)
        return inorder
        
