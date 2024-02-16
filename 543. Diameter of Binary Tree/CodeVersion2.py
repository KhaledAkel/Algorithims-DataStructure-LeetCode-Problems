class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter = 0
        stack = [(root, False)]
        depths = {}
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left_depth = depths.get(node.left, 0)
                    right_depth = depths.get(node.right, 0)
                    diameter = max(diameter, left_depth + right_depth)
                    depths[node] = 1 + max(left_depth, right_depth)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        
        return diameter
