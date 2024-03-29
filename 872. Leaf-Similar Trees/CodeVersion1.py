# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, seq):
            if not root:
                return
            if not (root.left or root.right):
                seq.append(root.val)
            dfs(root.left, seq)
            dfs(root.right, seq)
            return seq

        return dfs(root1, []) == dfs(root2, [])

            
        
