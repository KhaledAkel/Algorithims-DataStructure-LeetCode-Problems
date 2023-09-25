class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = (len(nums)//2)
        if len(nums) <= 2:
            return nums[0]
        if nums[mid] == nums[mid+1]:
            return nums[mid+1] 
        if nums[mid] == nums[mid-1]:
            return nums[mid-1]

