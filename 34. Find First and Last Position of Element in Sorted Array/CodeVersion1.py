class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function to find the leftmost (first) index of the target
        def find_leftmost(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        # Function to find the rightmost (last) index of the target
        def find_rightmost(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        left = find_leftmost(nums, target)
        right = find_rightmost(nums, target) - 1
        
        # Check if the target is not in the list
        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
