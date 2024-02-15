class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            left = dfs(root.left)  # Depth of left subtree
            right = dfs(root.right)  # Depth of right subtree
            
            diameter = max(diameter, left + right)  # Update diameter
            
            # Return the depth of current subtree
            return 1 + max(left, right)
        
        dfs(root)
        return diameter
