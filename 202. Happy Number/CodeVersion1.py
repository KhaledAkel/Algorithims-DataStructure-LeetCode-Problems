class Solution:
    def isHappy(self, n: int, visited=None) -> bool:
        
        if visited is None:
            visited = set()  
    
        if n == 1:
            return True
        
        if n in visited:
            return False
        
        visited.add(n) 
        new_num = sum(int(digit) ** 2 for digit in str(n))
        
        return self.isHappy(new_num, visited)
