class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            
            #[(38,1),(30,2)]
            #[1,]
            while stack and stack[-1][0]<temperatures[i]:
                temp,index=stack.pop()
                res[index]=i-index


            stack.append((t,i))

        return res
                

        