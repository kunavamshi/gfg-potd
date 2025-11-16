class Solution:
    def LCIS(self, a, b):
        n = len(a)
        m = len(b)

        # dp[j] = length of LCIS ending with b[j]
        dp = [0] * m

        for i in range(n):
            current_max = 0
            for j in range(m):
                if a[i] == b[j]:
                    dp[j] = current_max + 1
                elif a[i] > b[j]:
                    current_max = max(current_max, dp[j])

        return max(dp)