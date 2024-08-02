class Solution:
    def editDistance(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from str1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters into str1

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1],    # Insert
                                   dp[i - 1][j],    # Remove
                                   dp[i - 1][j - 1] # Replace
                                  ) + 1

        return dp[m][n]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends