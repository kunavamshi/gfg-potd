
class Solution:
    # Function should return an integer
    # a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
        start = 0
        
        for end in range(n):
            if arr[end] <= k:
                current_books += arr[end]
                max_books = max(max_books, current_books)
            else:
                current_books = 0
        
        return max_books

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends