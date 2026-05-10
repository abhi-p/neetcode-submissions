class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations={'+','-','*','/'}

        ret=None
        evalStack=[]
        for i in range(len(tokens)):
            #print(evalStack)
            if tokens[i] not in operations:
                evalStack.append(int(tokens[i]))
                #print('num: ', tokens[i])
            else:
                num2=evalStack.pop()
                num1=evalStack.pop()

                if tokens[i] =='+':
                    #print('adding: ', num1,num2)
                    evalStack.append(num1+num2)
                elif tokens[i]=='-':
                    #print('sub: ', num1,num2)
                    evalStack.append(num1-num2)
                elif tokens[i]=='*':
                    #print('multi: ', num1,num2)
                    evalStack.append(num1*num2)
                elif tokens[i]=='/':
                   # print('divide: ', num1,num2)

                    evalStack.append(int(num1/num2))
        return evalStack[-1] 
            