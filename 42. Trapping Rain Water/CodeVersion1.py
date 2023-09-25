class Solution:
    def trap(self, height: List[int]) -> int:
        output =0
        for i in range(len(height)-1):
            leftmax = max(height[:i+1])
            rightmax = max(height[i:])
            water = min(leftmax, rightmax)-height[i]
            if water > 0:
                output += water
            
        return output
