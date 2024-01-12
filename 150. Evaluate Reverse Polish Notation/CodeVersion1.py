class Solution:
    def isNumber(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        out = 0

        for ele in tokens:
            if self.isNumber(ele):
                stack.append(int(ele))
            else:
                if ele == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1+num2)

                elif ele == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1-num2)
                
                elif ele == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1*num2)
                
                else:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(int(num1 / num2))
        return stack.pop()

        
