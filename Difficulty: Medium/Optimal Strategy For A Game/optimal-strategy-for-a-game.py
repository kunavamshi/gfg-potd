class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = arr[i]
        for i in range(n-1):
            dp[i][i+1] = max(arr[i], arr[i+1])
        
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Fetch dp values without checking conditions
                a = dp[i+2][j]   if i+2 <= j else 0
                b = dp[i+1][j-1] if i+1 <= j-1 else 0
                c = dp[i][j-2]   if i <= j-2 else 0

                # Compute optimal pick
                left  = arr[i] + (b if a > b else a)
                right = arr[j] + (b if c > b else c)

                dp[i][j] = left if left > right else right

        return dp[0][n-1]