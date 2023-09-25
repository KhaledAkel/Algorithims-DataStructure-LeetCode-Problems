# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for j in range(len(nums)):
            for k in range(j+1, len(nums)):
                if nums[j] + nums[k] == target:
                    return [j,k]
