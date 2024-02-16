class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, False)]
        depth = {}

        while stack:
            node, visited = stack.pop()

            if visited:
                left = depth.get(node.left, 0)
                right = depth.get(node.right, 0)
                if abs(left-right) > 1:
                    return False
                depth[node] = 1 + max(left, right)

            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        return True
