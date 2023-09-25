class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Goal = -1
        Pointer = -2

        while Pointer >= -len(nums):
            if (nums[Pointer] -((-Pointer) - (-Goal))) >= 0:
                Goal = Pointer
            Pointer -= 1
        return True if Goal == -len(nums) else False
