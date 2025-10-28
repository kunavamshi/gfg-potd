from collections import deque

class Solution:
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        dist = [[-1]*m for _ in range(n)]
        q = deque()

        # Step 1: Initialize BFS with all 1's
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        # 4 possible directions (up, down, left, right)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS traversal
        while q:
            i, j = q.popleft()

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and dist[x][y] == -1:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))

        return dist