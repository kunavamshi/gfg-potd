class Solution:
    def findMinCycle(self, V, edges):
        INF = float('inf')
        graph = [[INF] * V for _ in range(V)]

        # Build adjacency matrix
        for u, v, w in edges:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)

        # Initialize distance same as graph
        dist = [[graph[i][j] for j in range(V)] for i in range(V)]

        min_cycle = INF

        # Try every node k as intermediate
        for k in range(V):
            # Try all pairs i, j < k to find cycle through k
            for i in range(k):
                for j in range(i+1, k):
                    if graph[i][k] != INF and graph[k][j] != INF and dist[i][j] != INF:
                        min_cycle = min(min_cycle, dist[i][j] + graph[i][k] + graph[k][j])
            # Floyd-Warshall update
            for i in range(V):
                for j in range(V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return -1 if min_cycle == INF else min_cycle



#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        obj = Solution()
        res = obj.findMinCycle(V, edges)

        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends