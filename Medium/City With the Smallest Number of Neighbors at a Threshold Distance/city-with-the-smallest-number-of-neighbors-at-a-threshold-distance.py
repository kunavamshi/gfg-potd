import heapq
from typing import List

class Solution:
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build adjacency list representation of the graph
        graph = {i: [] for i in range(n)}
        for edge in edges:
            u, v, wt = edge
            graph[u].append((v, wt))
            graph[v].append((u, wt))

        # Function to find shortest paths using Dijkstra's algorithm
        def dijkstra(src):
            distance = [float('inf')] * n
            distance[src] = 0
            pq = [(0, src)]  # (distance, vertex)
            while pq:
                dist, node = heapq.heappop(pq)
                if dist > distance[node]:
                    continue
                for neighbor, weight in graph[node]:
                    if dist + weight < distance[neighbor]:
                        distance[neighbor] = dist + weight
                        heapq.heappush(pq, (distance[neighbor], neighbor))
            return distance

        min_cities_reachable = float('inf')
        city_with_min_cities = -1

        # Iterate through each city and find the number of reachable cities
        for city in range(n):
            distances = dijkstra(city)
            reachable_cities = sum(1 for dist in distances if dist <= distanceThreshold)
            if reachable_cities < min_cities_reachable or (reachable_cities == min_cities_reachable and city > city_with_min_cities):
                min_cities_reachable = reachable_cities
                city_with_min_cities = city

        return city_with_min_cities



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends