class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            
            if char != "]":
                stack.append(char)
            
            else:
                tempString = ""
                while stack[-1] != "[":
                    tempString = stack[-1] + tempString
                    stack.pop()
                
                stack.pop()  # remove [

                tempNumber = ""
                while stack and stack[-1].isdigit():
                    tempNumber = stack[-1] + tempNumber
                    stack.pop()


                tempString = tempString * int(tempNumber)
                stack.append(tempString)
                
        return "".join(stack)



         
        
