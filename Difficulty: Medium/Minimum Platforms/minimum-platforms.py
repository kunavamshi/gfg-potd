class Solution:
    def minimumPlatform(self, arr, dep):
        # Sorting arrival and departure times
        arr.sort()
        dep.sort()
        
        n = len(arr)
        platforms = 0  # Tracks the required platforms at any time
        max_platforms = 0  # Stores the maximum platforms needed
        
        i, j = 0, 0  # Two pointers for arrivals and departures
        
        # Traverse both sorted lists
        while i < n and j < n:
            if arr[i] <= dep[j]:  # Train arrives before the last one departs
                platforms += 1
                i += 1
            else:  # A train departs
                platforms -= 1
                j += 1
            
            max_platforms = max(max_platforms, platforms)
        
        return max_platforms


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends