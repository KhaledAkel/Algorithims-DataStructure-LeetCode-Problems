# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, path, count):
            if not root:
                return count
            
            for i in range(len(path)):
                if sum(path[i:]) == targetSum:
                    count += 1
                    
            count = dfs(root.left, path + [root.left.val] if root.left else [], count)
            count = dfs(root.right, path + [root.right.val] if root.right else [], count)

            return count

        if not root:
            return 0
        
        return dfs(root, [root.val], 0)
