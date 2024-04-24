#User function Template for python3
class Solution:
    def ways(self, x, y):
        # Initialize a 2D array to store number of paths
        paths = [[0] * (y + 1) for _ in range(x + 1)]

        # Base case: There is only one path to reach any point on x-axis or y-axis
        for i in range(x + 1):
            paths[i][0] = 1
        for j in range(y + 1):
            paths[0][j] = 1

        # Fill up the array using dynamic programming
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                # Number of paths to reach current point is sum of paths from left and above
                paths[i][j] = (paths[i - 1][j] + paths[i][j - 1]) % 1000000007

        # Return the number of paths from (x, y) to origin
        return paths[x][y]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    x,y=list(map(int,input().split()))
    ob = Solution()
    print(ob.ways(x,y))
# } Driver Code Ends