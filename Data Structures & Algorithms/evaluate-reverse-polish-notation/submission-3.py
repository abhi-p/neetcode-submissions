class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numStack=[]
        signs={"+","-","*","/"}
        for i in range(len(tokens)):
            if tokens[i] not in signs:
                numStack.append(tokens[i])

            elif tokens[i] in signs:
                if tokens[i]=="+":
                    numStack.append(int(numStack.pop())+int(numStack.pop()))
                elif tokens[i]=="-":
                    v1,v2=int(numStack.pop()),int(numStack.pop())
                    numStack.append(v2-v1)
                elif tokens[i]=="*":
                    numStack.append(int(numStack.pop())*int(numStack.pop()))
                else:
                    v1,v2=int(numStack.pop()),int(numStack.pop())
                    numStack.append(v2/v1)
        return int(numStack.pop())


        