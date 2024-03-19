class Solution:
    def maximumWeight(self, n, edges, q, queries):
        ans = 0
        
        def root(i, parent):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(a, b, parent, sz):
            nonlocal ans
            ra = root(a, parent)
            rb = root(b, parent)
            if ra == rb:
                return sz[ra] * sz[ra]
            if sz[ra] < sz[rb]:
                ra, rb = rb, ra
                a, b = b, a
            ans += sz[ra] * sz[rb]
            parent[rb] = ra
            sz[ra] += sz[rb]
            return ans
        
        parent = [i for i in range(n + 1)]
        sz = [1] * (n + 1)
        wt = sorted([(w, (a, b)) for a, b, w in edges])
        
        mp = {}
        for w, (a, b) in wt:
            mp[w] = union(a, b, parent, sz)
        
        res = []
        for query in queries:
            val = max([v for k, v in mp.items() if k <= query], default=0)
            res.append(val)
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())

        edges = [[0 for j in range(3)] for i in range(n-1)]
        for i in range(n-1):
            input_line = [int(x) for x in input().strip().split()]       
            for j in range (3):
                edges[i][j]=input_line[j]

        q = int(input())
        queries = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.maximumWeight(n, edges, q, queries)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends