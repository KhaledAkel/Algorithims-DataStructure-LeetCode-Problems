class Solution:
    def trap(self, height: List[int]) -> int:
        before, after = [0]*len(height), [0]*len(height)
        out = 0

        # [0,4,4,4,4,4]
        Max = max(height[0], 0)
        for i in range(1,len(height)):
            Max = max(height[i], Max)
            before[i] = Max
        
        # [5,5,5,5,5,0]
        Max = max(height[-1] , 0)
        for i in range(len(height)-2, -1, -1):
            Max = max(height[i], Max)
            after[i] = Max
        
        for i in range(len(height)):
            if before[i] > height[i] < after[i]:
                out += min(before[i], after[i]) - height[i]
        
        return out


        
