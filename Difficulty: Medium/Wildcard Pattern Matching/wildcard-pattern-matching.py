class Solution:
    def wildCard(self, txt, pat):
        n, m = len(txt), len(pat)
        
        # dp[i][j] = whether pat[0..j-1] matches txt[0..i-1]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Empty pattern matches empty text
        dp[0][0] = True

        # '*' can match empty sequence — initialize first row
        for j in range(1, m + 1):
            if pat[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pat[j - 1] == '?' or pat[j - 1] == txt[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[j - 1] == '*':
                    # '*' matches empty sequence (dp[i][j-1]) or any sequence (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[n][m]