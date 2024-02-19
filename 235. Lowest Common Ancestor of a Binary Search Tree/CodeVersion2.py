class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if (p.val <= root.val <= q.val) or (p.val >= root.val >= q.val):
                return root
            elif root.val <= p.val:
                root = root.right
            else:
                root = root.left
        
