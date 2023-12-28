# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]
        sumCount = 0

        while stack:
            node, path = stack.pop()

            for i in range(len(path)):
                if sum(path[i:]) == targetSum:
                    sumCount += 1

            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))

        return sumCount
