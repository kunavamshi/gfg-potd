#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # If q is outside the range of possible values in the matrix, return 0
        if q < 2 or q > 2 * n:
            return 0
        
        # Calculate the valid range for i
        start_i = max(1, q - n)
        end_i = min(n, q - 1)
        
        # The number of valid pairs (i, j) such that i + j = q
        return end_i - start_i + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends