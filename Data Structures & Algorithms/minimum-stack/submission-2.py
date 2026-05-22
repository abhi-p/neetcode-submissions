class MinStack:

    def __init__(self):
        self.minStack=[]
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack and not self.minStack:
            self.stack.append(val)
            self.minStack.append(val)

        elif val<=self.minStack[-1]:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)  

    def pop(self) -> None:
        val=self.stack.pop()
        if val==self.minStack[-1]:
            self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
