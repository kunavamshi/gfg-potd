class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill DP table
        for length in range(2, n + 1):  # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends