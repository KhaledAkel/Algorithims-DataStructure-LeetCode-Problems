class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before, after = 1, 1
        answer=[1]*len(nums)

        for i in range(1,len(nums)):
            before *= nums[i-1]
            answer[i] = before
        
        for i in range(len(nums)-2,-1,-1 ):
            after *= nums[i+1]
            answer[i] *= after
        return answer
