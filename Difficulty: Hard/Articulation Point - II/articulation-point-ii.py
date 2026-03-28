class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        visited = [False] * V
        ap = [False] * V
        
        time = 0
        
        def dfs(u):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            children = 0
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: Root node
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    
                    # Case 2: Non-root node
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                        
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        # Handle disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        result = [i for i in range(V) if ap[i]]
        
        return result if result else [-1]