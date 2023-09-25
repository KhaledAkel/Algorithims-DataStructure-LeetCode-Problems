class Solution:
    def isHappy(self, n: int) -> bool:
        
        for _ in range(10):
            n = [int(x) for x in str(n)]
            sum = 0
            for i in n:
                sum += i**2
            if sum == 1:
                return True
            n = sum
        
        return False
