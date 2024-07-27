class Solution:
    def countMin(self, s):
        n = len(s)
        
        # Create a table to store results of subproblems
        dp = [[0 for x in range(n)] for y in range(n)]
        
        # Strings of length 1 are palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Build the table. The outer loop is for the length of the substring
        for cl in range(2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        
        # Length of longest palindromic subsequence
        lps = dp[0][n - 1]
        
        # Minimum insertions to form a palindrome
        return n - lps



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends