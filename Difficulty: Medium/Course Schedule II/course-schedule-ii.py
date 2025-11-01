class Solution:
    def findOrder(self, n, prerequisites):
        # Build adjacency list and in-degree array
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        # Queue for courses with no prerequisites
        from collections import deque
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        order = []
        
        while q:
            node = q.popleft()
            order.append(node)
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # If we could schedule all courses, return order
        if len(order) == n:
            return order
        else:
            return []