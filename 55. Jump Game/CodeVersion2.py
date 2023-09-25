class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def CheckPosition(position):
            if position == len(nums) - 1:
                return True

            steps = min(position + nums[position], len(nums)-1)
            for i in range(position+1, steps+1):
                if CheckPosition(i):
                    return True
            return False
        return CheckPosition(0)
