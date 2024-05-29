
class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        # Initialize a list to store the win/lose status for each amount of coins
        dp = [False] * (n + 1)
        
        # Base case
        dp[0] = False  # If there are no coins left, Geek loses
        
        # Fill the dp list
        for i in range(1, n + 1):
            if (i >= 1 and not dp[i - 1]) or (i >= x and not dp[i - x]) or (i >= y and not dp[i - y]):
                dp[i] = True
        
        # The result for n coins
        return 1 if dp[n] else 0


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends