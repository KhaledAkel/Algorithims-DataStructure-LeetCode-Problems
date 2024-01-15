class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                temp, index = stack.pop()
                answer[index] = i - index
            stack.append((temperatures[i], i))
        return answer

        
