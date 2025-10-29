from collections import deque

class Solution:
    def diameter(self, V, edges):
        # Build adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Helper BFS function to find farthest node and distance
        def bfs(start):
            visited = [-1] * V
            visited[start] = 0
            q = deque([start])
            farthest_node = start
            max_dist = 0
            
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[node] + 1
                        q.append(neighbor)
                        if visited[neighbor] > max_dist:
                            max_dist = visited[neighbor]
                            farthest_node = neighbor
            return farthest_node, max_dist
        
        # Step 1: BFS from any node (0)
        farthest, _ = bfs(0)
        
        # Step 2: BFS from the farthest node found
        _, diameter = bfs(farthest)
        
        return diameter