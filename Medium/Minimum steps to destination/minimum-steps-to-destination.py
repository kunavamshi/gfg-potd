#User function Template for python3

class Solution:
    def minSteps(self, d):
        steps = 0
        total = 0
        while total < d or (total - d) % 2 != 0:
            steps += 1
            total += steps
        return steps

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends