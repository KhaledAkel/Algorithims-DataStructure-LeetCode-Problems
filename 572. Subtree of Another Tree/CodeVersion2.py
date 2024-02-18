class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a, b):
            stack = [(a, b)]
            while stack:
                node1, node2 = stack.pop()
                if node1.val != node2.val:
                    return False
                if (not node1.left and node2.left) or (node1.left and not node2.left):
                    return False
                if (not node1.right and node2.right) or (node1.right and not node2.right):
                    return False
                if node1.left and node2.left:
                    stack.append((node1.left, node2.left))
                if node1.right and node2.right:
                    stack.append((node1.right, node2.right))
            return True
        
        stack = [(root, subRoot)]
        while stack:
            node1, node2 = stack.pop()
            if sameTree(node1, node2):
                return True
            if node1.left:
                stack.append((node1.left, node2))
            if node1.right:
                stack.append((node1.right, node2))
        return False
