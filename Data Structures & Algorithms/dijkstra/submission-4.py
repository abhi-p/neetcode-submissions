import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj={}
        for i in range(n):
            adj[i]=[]
        for edge in edges:
            s,e,d=edge
            adj[s].append([d,e])

        shortest={}

        minHeap=[[0,src]]

        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1]=w1
            #print(adj)
            for neigh in adj[n1]:
                d2,n2=neigh
                if n2 not in shortest:
                    heapq.heappush(minHeap,[w1+d2,n2])
            #print(minHeap)
        for e in range(n):
            if e not in shortest:
                shortest[e]=-1
        return shortest