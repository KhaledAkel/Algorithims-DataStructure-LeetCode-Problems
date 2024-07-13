# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            if not root:
                return
            out.append(root.val)

            if root.left:
                preorder(root.left)
            
            if root.right:
                preorder(root.right)

        out = []
        preorder(root)
        return out
        
