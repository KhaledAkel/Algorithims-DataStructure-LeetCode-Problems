
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array in ascending order
        closest = sum(nums[:3])

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if abs(target - currSum) < abs(closest - target):
                    closest = currSum
                
                if currSum < target:
                    left += 1
                else:
                    right -= 1

        return closest
