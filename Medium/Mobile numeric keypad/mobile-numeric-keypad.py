#User function Template for python3
class Solution:
    def getCount(self, n):
        if n == 1:
            return 10
        
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 0, 5, 7, 9],
            9: [9, 6, 8]
        }
        
        # Initialize the dp table
        dp = [[0] * 10 for _ in range(n + 1)]
        
        # Base case for sequences of length 1
        for i in range(10):
            dp[1][i] = 1
        
        # Fill the dp table for lengths from 2 to n
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = sum(dp[length - 1][neighbor] for neighbor in neighbors[digit])
        
        # Sum up all sequences of length n ending at any digit
        return sum(dp[n][digit] for digit in range(10))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends