from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the current sum and maximum sum to the first element
        currSum = nums[0]
        maxSum = nums[0]

        # Start iterating from the second element since the first is already considered
        for i in range(1, len(nums)):
            # Update the current sum to the maximum of current element alone or current sum + current element
            currSum = max(nums[i], currSum + nums[i])
            # Update the maximum sum to the maximum of maxSum and currSum
            maxSum = max(maxSum, currSum)
        
        return maxSum

