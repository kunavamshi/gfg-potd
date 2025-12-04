class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        # dp[i][j] = optimal cost for keys[i..j]
        dp = [[0] * n for _ in range(n)]

        # prefix sum to get sum of freq in O(1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + freq[i]

        def range_sum(l, r):
            return prefix[r+1] - prefix[l]

        # len = 1 → cost = freq[i]
        for i in range(n):
            dp[i][i] = freq[i]

        # increasing segment length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = range_sum(i, j)
                best = float('inf')

                # choose root r
                for r in range(i, j + 1):
                    left = dp[i][r-1] if r > i else 0
                    right = dp[r+1][j] if r < j else 0
                    best = min(best, left + right + total)

                dp[i][j] = best

        return dp[0][n-1]