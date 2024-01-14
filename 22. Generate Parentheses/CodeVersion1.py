class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('(', 1, 0)]
        actions = ['(', ')']
        res = []

        while stack:
            cur, opened, closed = stack.pop()

            if len(cur) == n*2:
                res.append(cur)
                continue
            
            for action in actions:
                if action == '(' and opened<n:
                    stack.append((cur+'(', opened+1, closed))
                elif action == ')' and closed<opened:
                    stack.append((cur+')', opened, closed+1))
                else:
                    continue
        return res




            

        
