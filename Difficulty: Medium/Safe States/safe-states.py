from collections import deque, defaultdict

class Solution:
    def safeNodes(self, V, edges):
        # Step 1: Build graph and reverse graph
        graph = defaultdict(list)
        indegree = [0] * V
        
        for u, v in edges:
            graph[v].append(u)  # reverse graph
            indegree[u] += 1    # original indegree

        # Step 2: Queue all terminal nodes (nodes with 0 outgoing edges)
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * V
        
        # Step 3: Topological sort on reverse graph
        while q:
            node = q.popleft()
            safe[node] = True
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Step 4: Collect all safe nodes
        ans = [i for i in range(V) if safe[i]]
        return sorted(ans)