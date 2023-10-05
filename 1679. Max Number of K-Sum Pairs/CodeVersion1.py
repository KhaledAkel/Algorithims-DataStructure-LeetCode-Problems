class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        left , right = 0, len(nums)-1
        count = 0

        while (left < right) and (left < len(nums)-1) and (right > 0) :
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1

            elif nums[left] + nums[right] > k:
                right -=1

            else:
                left += 1

        return count



        
