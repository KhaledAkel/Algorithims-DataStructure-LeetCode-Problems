class Solution:
    def trap(self, height: List[int]) -> int:
        a, b = 0, len(height)-1
        before, after = height[0], height[-1]
        out = 0

        while a<b:
            if before <= after:
                a += 1
                before = max(before, height[a])
                out += before - height[a]

            else:
                b -= 1
                after = max(after, height[b])
                out += after - height[b]
        return out









        
