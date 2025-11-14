class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        INF = 10**18
        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF

                # step merges
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])

                # If we can reduce to 1 pile, add merge cost
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += get_sum(i, j)

        return dp[0][n - 1]