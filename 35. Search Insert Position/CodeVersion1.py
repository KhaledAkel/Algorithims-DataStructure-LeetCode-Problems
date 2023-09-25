class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high)//2


        while  high >= low:

            if nums[high] < target:
                return high + 1
            
            if nums[low] > target:
                return low


            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
           
            if nums[mid] > target:
                high = mid

            mid = (low+high)//2

        if target < nums[low]:
            return low
        else:
            return high
