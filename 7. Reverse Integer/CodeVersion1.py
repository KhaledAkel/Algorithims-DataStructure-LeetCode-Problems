class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        neg = x < 0

        if neg:
            number = number[1:]

        res = 0
        for i in range(len(number)-1, -1,-1):
            res += (int(number[i]))*(10**(i))

        if res < -2**(31)  or  res > (2**(31)-1):
            return 0
        
        return res if neg == False else res*-1








        
