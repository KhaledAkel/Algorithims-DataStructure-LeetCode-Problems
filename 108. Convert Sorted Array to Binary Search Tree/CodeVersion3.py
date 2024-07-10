# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Initialize the root of the BST
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # Stack to hold the nodes and their corresponding bounds in the nums array
        stack = [(root, 0, mid - 1, mid + 1, len(nums) - 1)]

        while stack:
            node, left_start, left_end, right_start, right_end = stack.pop()

            # Process left child
            if left_start <= left_end:
                left_mid = (left_start + left_end) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left_start, left_mid - 1, left_mid + 1, left_end))

            # Process right child
            if right_start <= right_end:
                right_mid = (right_start + right_end) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, right_start, right_mid - 1, right_mid + 1, right_end))

        return root

        return sorted_list_to_bst(nums, 0, len(nums)-1)
