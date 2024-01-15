class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedMap = {position[i]:speed[i] for i in range(len(position))}
        stack = []
        position.sort(reverse=True)

        for pos in position:
            if stack and stack[-1] >= ((target-pos)/speedMap[pos]):
                continue
            stack.append((target-pos)/speedMap[pos])
        
        return len(stack)







        
