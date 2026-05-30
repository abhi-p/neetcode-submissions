class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj=defaultdict(list)
        for src,dest,time in times:
            adj[src].append((dest,time))

        minHeap=[(0,k)]
        t=0
        visit=set()
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visit:
                continue
        
            t=w1
            visit.add(n1)
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        print(visit)
        return t if len(visit) == n else -1

