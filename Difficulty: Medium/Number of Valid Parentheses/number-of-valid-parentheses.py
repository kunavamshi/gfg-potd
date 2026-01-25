class Solution:
    def findWays(self, n):
        # code here
        if n % 2 == 1:
            return 0
        
        m = n // 2  # number of pairs
        dp = [0] * (m + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            total = 0
            for j in range(i):
                total += dp[j] * dp[i - 1 - j]
            dp[i] = total
        
        return dp[m]