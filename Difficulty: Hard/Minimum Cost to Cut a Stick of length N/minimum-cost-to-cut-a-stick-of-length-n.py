class Solution:
    def minCutCost(self, n, cuts):
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)

        # dp[i][j] = minimum cost to cut the stick between cuts[i] and cuts[j]
        dp = [[0] * m for _ in range(m)]

        # l = interval length
        for l in range(2, m):  # interval size
            for i in range(0, m - l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j],
                                   cuts[j] - cuts[i] + dp[i][k] + dp[k][j])

        return dp[0][m - 1]