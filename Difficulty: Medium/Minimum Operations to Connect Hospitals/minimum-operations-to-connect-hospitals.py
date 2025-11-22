class Solution:
    def minConnect(self, V, edges):
        parent = list(range(V))
        rank = [0] * V
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False   # redundant edge
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1
            return True
        
        redundant = 0
        for u, v in edges:
            if not union(u, v):
                redundant += 1
        
        # count components
        comps = sum(1 for i in range(V) if find(i) == i)
        
        ops_needed = comps - 1
        
        return ops_needed if redundant >= ops_needed else -1