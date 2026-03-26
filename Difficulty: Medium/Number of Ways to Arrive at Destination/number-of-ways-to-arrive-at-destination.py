import heapq

class Solution:
    def countPaths(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Min heap
        pq = []
        heapq.heappush(pq, (0, 0))  # (distance, node)
        
        # Distance and ways arrays
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbor, weight in adj[node]:
                new_dist = curr_dist + weight
                
                # Found shorter path
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))
                
                # Found another shortest path
                elif new_dist == dist[neighbor]:
                    ways[neighbor] += ways[node]
        
        return ways[V - 1]