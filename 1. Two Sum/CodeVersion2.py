class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        HashMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in HashMap:
                return [HashMap[target-nums[i]],i]
            HashMap[nums[i]] = i
