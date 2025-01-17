class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        if n == 2:
            return [arr[1], arr[0]]

        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        # Compute prefix product
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]

        # Compute suffix product
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]

        # Compute result
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends