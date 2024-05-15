class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if num[0] == "-":
            return False
        
        rev = 0
        for i in range(len(num)-1, -1, -1):
            rev += int(num[i])*(10**i)
        
        return rev == x



        
