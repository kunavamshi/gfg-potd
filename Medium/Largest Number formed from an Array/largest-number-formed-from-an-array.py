

class Solution:

    def printLargest(self, n, arr):
        # Custom comparison function to sort strings
        def compare(a, b):
            # Concatenate a + b
            ab = a + b
            # Concatenate b + a
            ba = b + a
            # Compare the concatenated strings
            if ab < ba:
                return 1
            elif ab > ba:
                return -1
            else:
                return 0

        # Sort the array of strings using custom comparison function
        arr.sort(key=functools.cmp_to_key(compare))
        
        # Concatenate sorted strings and return
        return ''.join(arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends