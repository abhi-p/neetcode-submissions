class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adj={}

        for i in range(n):
            adj[i]=[]

        for src,dest in edges:
            adj[src].append(dest)

        topSort=[]
        visit=set()
        visiting=set()

        def dfs(src):

            if src in visit:
                return True
            if src in visiting:
                return False
        
            visiting.add(src)

            for dest in adj[src]:
                if not dfs(dest):
                    return False
            visiting.remove(src)
            visit.add(src)

            topSort.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []

        
        topSort.reverse()

        return topSort


        