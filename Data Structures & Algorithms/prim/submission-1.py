class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adj={}
        for i in range(n):
            adj[i]=[]
        
        for s,d,w in edges:
            adj[s].append((d,w))
            adj[d].append((s,w))
        MST=[]
        visited=set()
        minHeap=[[0,edges[0][0]]]
        mstSum=0
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            mstSum+=w1
            
            for edge in adj[n1]:
                n2,w2=edge
                if n2 not in visited:
                    heapq.heappush(minHeap,[w2,n2])

        #print(mstSum)

        if len(visited)!=n:
            return -1 
        return mstSum


