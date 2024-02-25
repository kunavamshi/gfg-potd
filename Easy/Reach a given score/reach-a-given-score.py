class Solution:
    def count(self, n: int) -> int:
        # Create a list to store the counts for each score from 0 to n
        dp = [0] * (n + 1)
        
        # Base case: there's 1 way to score 0 points
        dp[0] = 1
        
        # Iterate through each possible score
        for i in range(3, n + 1):
            # Add the counts for each possible move (3, 5, 10)
            dp[i] += dp[i - 3]
        for i in range(5, n + 1):
            dp[i] += dp[i - 5]
        for i in range(10, n + 1):
            dp[i] += dp[i - 10]
        
        # Return the count for the total score
        return dp[n]

# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))