from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        sums = {}
        result = (1, root.val)

        while queue:
            node, level = queue.popleft()

            if level not in sums:
                sums[level] = node.val
            else:
                sums[level] += node.val
            
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        for key in sums:
            if sums[key] > result[1]:
                result = (key, sums[key])

        return result[0]
