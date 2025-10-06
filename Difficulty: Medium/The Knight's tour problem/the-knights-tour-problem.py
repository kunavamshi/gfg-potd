class Solution:
    def knightTour(self, n):
        # Initialize chessboard with -1 (unvisited)
        board = [[-1 for _ in range(n)] for _ in range(n)]

        # Knight's possible moves
        moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
        moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Starting point
        board[0][0] = 0

        # Recursive helper function
        def solve(x, y, move_count):
            # Base case: all cells visited
            if move_count == n * n:
                return True

            # Try all next moves
            for i in range(8):
                nx, ny = x + moves_x[i], y + moves_y[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                    board[nx][ny] = move_count
                    if solve(nx, ny, move_count + 1):
                        return True
                    # Backtrack
                    board[nx][ny] = -1
            return False

        # Start recursion
        if solve(0, 0, 1):
            return board
        else:
            return []