class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        lis = []

        def dfs(root, level):
            nonlocal lis
            if not root:
                return
            if level == len(lis):
                lis.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return lis
