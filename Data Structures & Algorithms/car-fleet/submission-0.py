class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posCarPair=[(position[i],speed[i],(target-position[i])/speed[i]) for i in range(len(speed))]

        posCarPair.sort()
        print(posCarPair)

        p,s,t=posCarPair[-1]
        nextFleetTime=t
        fleet=1
        for i in range(len(posCarPair)-2,-1,-1):
            p,s,t=posCarPair[i]
            if t<=nextFleetTime:
                continue
            else:
                fleet+=1
                nextFleetTime=t
        return fleet


        