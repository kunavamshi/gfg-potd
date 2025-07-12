class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)       # number of rows
        m = len(mat[0])    # number of columns

        # Create DP table same size as mat
        dp = [[0] * m for _ in range(n)]

        # Fill the dp table from right to left
        for col in range(m - 1, -1, -1):
            for row in range(n):
                # Gold collected on going to the cell on the right
                right = dp[row][col + 1] if col < m - 1 else 0

                # Gold collected on going to the right-up cell
                right_up = dp[row - 1][col + 1] if row > 0 and col < m - 1 else 0

                # Gold collected on going to the right-down cell
                right_down = dp[row + 1][col + 1] if row < n - 1 and col < m - 1 else 0

                # Update dp table
                dp[row][col] = mat[row][col] + max(right, right_up, right_down)

        # The max value in the first column is the answer
        return max(dp[row][0] for row in range(n))