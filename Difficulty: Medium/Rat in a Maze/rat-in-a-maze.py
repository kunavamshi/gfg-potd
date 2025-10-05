class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        ans = []

        # If start or end cell is blocked
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return ans

        # Directions: (direction_char, row_change, col_change)
        directions = [
            ('D', 1, 0),   # Down
            ('L', 0, -1),  # Left
            ('R', 0, 1),   # Right
            ('U', -1, 0)   # Up
        ]

        visited = [[False for _ in range(n)] for _ in range(n)]

        def backtrack(row, col, path):
            # If destination is reached
            if row == n - 1 and col == n - 1:
                ans.append(path)
                return

            # Mark current cell as visited
            visited[row][col] = True

            # Explore all four directions
            for move, dr, dc in directions:
                new_r, new_c = row + dr, col + dc

                if (0 <= new_r < n and 0 <= new_c < n and 
                    maze[new_r][new_c] == 1 and not visited[new_r][new_c]):
                    backtrack(new_r, new_c, path + move)

            # Backtrack: Unmark current cell
            visited[row][col] = False

        # Start from (0, 0)
        backtrack(0, 0, "")

        # Return lexicographically sorted paths
        ans.sort()
        return ans