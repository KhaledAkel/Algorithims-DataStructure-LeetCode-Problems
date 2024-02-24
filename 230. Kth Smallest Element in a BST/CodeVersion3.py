# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, lis):
            if not root:
                return []
            
            dfs(root.left, lis)
            lis.append(root.val)
            dfs(root.right, lis)
            
        lis = []
        dfs(root, lis)
        return lis[k-1]
