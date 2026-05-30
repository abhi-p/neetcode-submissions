class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj={i:[] for i in range(numCourses)}
        for dep,src in prerequisites:
            adj[src].append(dep)
        visit=set()
        topSort=[]
        path=set()
        def dfs(src):
            if src in path:
                return False
            if src in visit:
                return True
            path.add(src)
            visit.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            topSort.append(src)
            path.remove(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        topSort.reverse()

        return topSort









        return 