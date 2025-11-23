class Solution:
    def maxRemove(self, stones):
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb: 
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        # Create DSU nodes for all rows and col nodes
        for x, y in stones:
            row = x
            col = y + 10001
            
            if row not in parent:
                parent[row] = row
                rank[row] = 0
            if col not in parent:
                parent[col] = col
                rank[col] = 0

            union(row, col)

        # Count unique connected components
        seen = set()
        for x, y in stones:
            seen.add(find(x))  # just using row is enough

        # max removable = total stones - components
        return len(stones) - len(seen)