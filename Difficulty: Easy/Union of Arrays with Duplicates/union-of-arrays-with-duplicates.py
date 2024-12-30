class Solution:    
    # Function to return the count of the number of elements in the union of two arrays.
    def findUnion(self, a, b):
        # Using a set to store distinct elements from both arrays
        union_set = set(a).union(set(b))
        return len(union_set)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends