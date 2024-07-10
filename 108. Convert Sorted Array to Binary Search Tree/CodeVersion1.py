# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sorted_list_to_bst(nums):
            if not nums:
                return None
            
            # Find the middle index
            mid = len(nums) // 2
            
            # The middle element becomes the root
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree
            root.left = sorted_list_to_bst(nums[:mid])
            
            # Recursively build the right subtree
            root.right = sorted_list_to_bst(nums[mid + 1:])
            
            return root

        return sorted_list_to_bst(nums)
