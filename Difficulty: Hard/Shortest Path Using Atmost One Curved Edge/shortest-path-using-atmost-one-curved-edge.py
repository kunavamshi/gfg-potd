import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, V, a, b, edges):
        # Build adjacency list: node -> list of (nbr, straightWeight, curvedWeight)
        g = defaultdict(list)
        for x, y, w1, w2 in edges:
            g[x].append((y, w1, w2))
            g[y].append((x, w1, w2))

        INF = 10**18
        dist = [[INF, INF] for _ in range(V)]   # dist[node][state]
        
        pq = []
        dist[a][0] = 0
        heapq.heappush(pq, (0, a, 0))   # (dist, node, usedCurved?)

        while pq:
            d, node, used = heapq.heappop(pq)

            if d != dist[node][used]:
                continue

            # Explore edges
            for nxt, w1, w2 in g[node]:

                # 1) Straight edge always allowed
                nd = d + w1
                if nd < dist[nxt][used]:
                    dist[nxt][used] = nd
                    heapq.heappush(pq, (nd, nxt, used))

                # 2) Curved edge allowed only if we haven't used one yet
                if used == 0:
                    nd = d + w2
                    if nd < dist[nxt][1]:
                        dist[nxt][1] = nd
                        heapq.heappush(pq, (nd, nxt, 1))

        ans = min(dist[b][0], dist[b][1])
        return ans if ans < INF else -1