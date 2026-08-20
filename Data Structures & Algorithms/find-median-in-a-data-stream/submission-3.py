class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        self.count=0


#         6,1,3,7,4,5,2,8
#  minHeap     maxHeap
#   [5,6,7,8]         [-4,-3,-2,-1]
                
    def addNum(self, num: int) -> None:

        if self.minHeap and num>self.minHeap[0]:
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-1*num)

        if len(self.minHeap)-len(self.maxHeap)>1:       
            val=heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-1*val)
        
        if len(self.maxHeap)-len(self.minHeap)>1:
            val=heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-1*val)

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            return 0

        if len(self.minHeap)==len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -1*self.maxHeap[0]
        