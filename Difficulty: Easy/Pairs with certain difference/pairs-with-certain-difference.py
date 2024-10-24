#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Sort the array in ascending order
        arr.sort()
        
        # Initialize sum of pairs
        max_sum = 0
        
        # Traverse the sorted array from the end
        i = N - 1
        while i > 0:
            # If the difference between arr[i] and arr[i-1] is less than K
            if arr[i] - arr[i-1] < K:
                # Add both to max_sum and skip these two elements
                max_sum += arr[i] + arr[i-1]
                i -= 2
            else:
                # If no pair is formed, move to the previous element
                i -= 1
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


        print("~")
if __name__ == "__main__":
    main()


# } Driver Code Ends