class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # Dictionary to store the last seen index of each element
        last_seen = {}

        # Iterate over the array
        for i, num in enumerate(arr):
            # Check if num is already in last_seen and within distance k
            if num in last_seen and i - last_seen[num] <= k:
                return True
            # Update the last seen index of num
            last_seen[num] = i
        
        # No duplicates found within k distance
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends