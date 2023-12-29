class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        def dfs(root, level, lis):
            if not root:
                return lis
            if level == len(lis):
                lis.append(root.val)
            lis = dfs(root.right, level + 1, lis)
            lis = dfs(root.left, level + 1, lis)
            return lis

        return dfs(root, 0, [])
