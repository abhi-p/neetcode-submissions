class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        #pair=[(p,s) for p,s in zip(position,speed)]
        pair=[[p,s,(target-p)/s] for p,s in zip(position,speed)]

        pair.sort(reverse=True)

        stack=[]
        for p,s,t in pair:
            if stack and stack[-1]>=t:
                continue
            else:
                stack.append(t)

        return len(stack)



            
