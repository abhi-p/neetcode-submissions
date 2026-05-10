class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj={ i: [] for i in range(numCourses)}

        for src,dest in prerequisites:
            if src in adj:
                adj[src].append(dest)

        

        visit=set()
        print(adj)
        def dfs(src):
            if src in visit:
                return False

            if adj[src]==[]:
                return True

            visit.add(src)

            for dest in adj[src]:
                if not dfs(dest):
                    return False
            visit.remove(src)
            adj[src]=[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
                    
        return True
