class Solution:
    def minCoins(self, coins, target):
        # Initialize DP array with a large value
        dp = [float('inf')] * (target + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum 0
        
        # Compute minimum coins for each amount up to the target
        for coin in coins:
            for amount in range(coin, target + 1):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        
        return dp[target] if dp[target] != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends