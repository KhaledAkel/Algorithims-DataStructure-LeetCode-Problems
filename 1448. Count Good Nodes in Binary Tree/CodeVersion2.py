# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, MAX, count):
            if root:
                if root.val >= MAX:
                    count += 1
                count = dfs(root.left, max(MAX, root.val), count)
                count = dfs(root.right, max(MAX, root.val), count)
            return count

        return dfs(root, float('-inf'), 0)
