class Solution:
    def findMinDiff(self, arr, M):
        n = len(arr)
        
        # Edge case
        if M == 0 or n == 0 or M > n:
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize answer
        min_diff = float('inf')
        
        # Step 3: Sliding window of size M
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff