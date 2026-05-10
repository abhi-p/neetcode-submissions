class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        ret=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            
            while len(stack)!=0 and stack[-1][0]<t:
                #print(i,stack,temperatures[i],ret)
                st,si=stack.pop()
                ret[si]=i-si

                
            stack.append((t,i))


        print(ret)

            





        
        return ret
                
