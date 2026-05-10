class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        

        adj={}
        for i in range(n):
            adj[i]=[]
        for s,d in edges:
            adj[s].append(d)

        topSort=[]
        visited=set()
        path=set()

        def dfs(n):
            if n in visited:
                return True
            if n in path:
                return False

            path.add(n)
            
            for n2 in adj[n]:
                if not dfs(n2):
                    return False
            visited.add(n)

            topSort.append(n)
            path.remove(n)
            return True



        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort

    
