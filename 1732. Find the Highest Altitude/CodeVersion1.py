class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        MAX ,current= 0, 0

        for i in range(len(gain)):
            current = current + gain[i]
            MAX = max(current, MAX)

        return MAX

        
