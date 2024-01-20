class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        
        def binarySearch(nums, a, b, target):
            while a <= b:
                mid = (a + b) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    a = mid + 1
                else:
                    b = mid - 1
            return -1

        while a <= b:
            mid = (a + b) // 2

            if nums[mid] == target:
                return mid

            if nums[a] <= target <= nums[mid]:
                return binarySearch(nums, a, mid, target)
            elif nums[mid] <= target <= nums[b]:
                return binarySearch(nums, mid, b, target)
            elif nums[mid] >= nums[a]:
                a = mid + 1
            else:
                b = mid - 1

        return -1
