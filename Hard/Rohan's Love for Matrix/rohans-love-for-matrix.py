class Solution:
    def multiply(self, a, b):
        mod = 1000000007
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += a[i][k] * b[k][j]
                    c[i][j] %= mod
        return c

    def power(self, a, n):
        mod = 1000000007
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = self.multiply(result, a)
            a = self.multiply(a, a)
            n //= 2
        return result

    def firstElement(self, n):
        mod = 1000000007
        a = [[1, 1], [1, 0]]
        result = self.power(a, n)
        return result[1][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends