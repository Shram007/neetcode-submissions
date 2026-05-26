class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ''' 
        nodemap = {i: [] for i in range(n)}
        if len(edges) > (n - 1):
            return False    
        for x, y in edges:
            nodemap[x].append(y)

        visiting = set()

        def dfs(x):
            if x in visiting: return False
            if nodemap[x] == []: return True

            visiting.add(x)
            for y in nodemap[x]:
                if not dfs(y): return False
            visiting.remove(x)
            nodemap[x] = []
            return True

        for c in range(n):
            if not dfs(c): return False
        return True 
        '''

        # Using BFS
        if len(edges) > (n-1): return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        q = deque([(0, -1)])
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent: continue
                if nei in visit: return False

                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n

