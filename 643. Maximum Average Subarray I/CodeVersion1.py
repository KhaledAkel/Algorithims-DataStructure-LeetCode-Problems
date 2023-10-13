class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]/1
        MAX = sum(nums[:k])
        SUM = MAX

        for i in range(k, len(nums)):
            SUM += nums[i] - nums[i-k]
            if SUM > MAX:
                MAX = SUM
            
        return MAX/k

        
