class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, curr_sum = 0, 0, 0
        minlength = float("inf")

        while end < len(nums):
            curr_sum += nums[end]
            end+=1

            while start<end and curr_sum >= target:
                curr_sum -= nums[start]
                start += 1

                minlength = min(minlength, end-start+1)

        
        return minlength if minlength <float("inf") else 0
