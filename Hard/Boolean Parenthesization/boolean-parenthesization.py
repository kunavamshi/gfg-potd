#User function Template for python3

class Solution:
    def countWays(self, n, s):
        mod = 1003
        # Initialize DP array
        dp_true = [[0] * n for _ in range(n)]
        dp_false = [[0] * n for _ in range(n)]

        # Fill the diagonal for single symbols
        for i in range(n):
            if s[i] == 'T':
                dp_true[i][i] = 1
            else:
                dp_false[i][i] = 1

        # Iterate over lengths of subexpressions
        for length in range(3, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                dp_true[i][j] = 0
                dp_false[i][j] = 0

                for k in range(i + 1, j, 2):
                    if s[k] == '&':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_true[i][k - 1] * dp_false[k + 1][j]) % mod + \
                                          (dp_false[i][k - 1] * dp_true[k + 1][j]) % mod + \
                                          (dp_false[i][k - 1] * dp_false[k + 1][j]) % mod
                    elif s[k] == '|':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_true[k + 1][j]) % mod + \
                                         (dp_true[i][k - 1] * dp_false[k + 1][j]) % mod + \
                                         (dp_false[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_false[i][k - 1] * dp_false[k + 1][j]) % mod
                    elif s[k] == '^':
                        dp_true[i][j] += (dp_true[i][k - 1] * dp_false[k + 1][j]) % mod + \
                                         (dp_false[i][k - 1] * dp_true[k + 1][j]) % mod
                        dp_false[i][j] += (dp_true[i][k - 1] * dp_true[k + 1][j]) % mod + \
                                          (dp_false[i][k - 1] * dp_false[k + 1][j]) % mod

                    dp_true[i][j] %= mod
                    dp_false[i][j] %= mod

        return dp_true[0][n - 1] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends