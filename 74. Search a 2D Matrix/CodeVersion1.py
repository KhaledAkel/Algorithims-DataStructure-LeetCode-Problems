class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            a, b = 0, len(nums) - 1

            while a <= b:
                mid = (a + b) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    a = mid + 1
                else:
                    b = mid - 1
            return False

        for nums in matrix:
            if nums[0] <= target <= nums[-1]:
                return binarySearch(nums, target)
