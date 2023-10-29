class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
                if stack[-1] + ast == 0: stack.pop(); break
                elif stack[-1] + ast > 0: break
                else: stack.pop()
            else: stack.append(ast)
        
        return stack
