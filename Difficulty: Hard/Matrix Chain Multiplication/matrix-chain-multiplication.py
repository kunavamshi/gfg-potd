class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)  # Number of matrices = len(arr) - 1
        dp = [[0] * n for _ in range(n)]  # DP table initialization

        for length in range(2, n):  # Sub-chain lengths
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')  # Initialize to a large value

                for k in range(i, j):  # Try different partition points
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)  # Store min cost
        
        return dp[1][n-1]  # The final answer (cost to multiply matrices from 1 to n-1)
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends