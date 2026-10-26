class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        total=0
        
        for i in tokens:
            if i =='+':
                total=int(stack[-2])+int(stack[-1])
                for i in range(2):
                    stack.pop(-1)
                stack.append(total)
            elif i =='-':
                total=int(stack[-2])-int(stack[-1])
                for i in range(2):
                    stack.pop(-1)
                stack.append(total)
            elif i =='*':
                total=int(stack[-2])*int(stack[-1])
                for i in range(2):
                    stack.pop(-1)
                stack.append(total)
            elif i =='/':
                total=int(int(stack[-2])/int(stack[-1]))
                for i in range(2):
                    stack.pop(-1)
                stack.append(total)
            else:
                stack.append(int(i))
        return stack[0]
           