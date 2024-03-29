class Solution:
    def isEularCircuitExist(self, v, adj):
        # Check if every vertex has even degree
        for vertex in range(v):
            if len(adj[vertex]) % 2 != 0:
                return 0
        
        # Check if the graph is connected
        visited = [False] * v
        self.dfs(adj, visited, 0)  # Start DFS traversal from vertex 0
        
        # If any vertex is not visited, the graph is not connected
        for vertex in range(v):
            if not visited[vertex] and adj[vertex]:
                return 0
        
        return 1

    def dfs(self, adj, visited, vertex):
        visited[vertex] = True
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                self.dfs(adj, visited, neighbor)



#{ 
 # Driver Code Starts
#Initial Template for python3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEularCircuitExist(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends