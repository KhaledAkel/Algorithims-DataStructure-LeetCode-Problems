# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, MIN, MAX):
            if not root:
                return True
            
            if MIN < root.val < MAX:
                return True and (dfs(root.left, MIN, root.val) and dfs(root.right, root.val, MAX))

            else:
                return False

        return dfs(root, float("-inf"), float("+inf"))
            
        
