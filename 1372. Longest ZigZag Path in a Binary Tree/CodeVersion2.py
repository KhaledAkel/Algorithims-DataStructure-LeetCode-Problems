# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def dfs(root, direction, length):
            nonlocal maxLength
            if not root:
                return 0
            
            maxLength = max(maxLength, length)
            
            if direction == "L":
                dfs(root.left, "R", length+1)
                dfs(root.right, "L", 1)
            else:
                dfs(root.right, "L", length+1)
                dfs(root.left, "R", 1)
            return maxLength

        return dfs(root, "L", 0)
