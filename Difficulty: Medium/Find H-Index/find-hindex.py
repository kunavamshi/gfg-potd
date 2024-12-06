class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations.sort(reverse=True)  # Sort in descending order
        
        h_index = 0
        for i in range(n):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index



#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends