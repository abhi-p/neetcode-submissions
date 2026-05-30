class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj=defaultdict(list)

        for i,edg in enumerate(edges):
            src,dest = edg
            adj[src].append((dest,succProb[i]))
            adj[dest].append((src,succProb[i]))


        minHeap=[(-1,start_node)]
        visit=set()
        while minHeap:
            w1,n1=heapq.heappop(minHeap)

            if n1==end_node:
                return -w1
            
            if n1 in visit:
                continue
            
            visit.add(n1)
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1*w2,n2))

            
        return 0