class Solution:
    def fill(self, grid):
        if not grid:
            return grid

        n, m = len(grid), len(grid[0])

        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c):
            # Mark as safe
            grid[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'O':
                    dfs(nr, nc)

        # Step 1: Run DFS from all border 'O's to mark safe regions
        for i in range(n):
            if grid[i][0] == 'O':
                dfs(i, 0)
            if grid[i][m-1] == 'O':
                dfs(i, m-1)
        for j in range(m):
            if grid[0][j] == 'O':
                dfs(0, j)
            if grid[n-1][j] == 'O':
                dfs(n-1, j)

        # Step 2: Replace remaining 'O' (surrounded ones) with 'X'
        # and revert '#' back to 'O'
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == '#':
                    grid[i][j] = 'O'

        return grid