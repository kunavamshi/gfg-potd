class Solution:
    def maxCircularSum(self, arr):
        total_sum = 0
        
        max_ending = min_ending = arr[0]
        max_sum = min_sum = arr[0]
        
        total_sum = arr[0]
        
        for i in range(1, len(arr)):
            total_sum += arr[i]
            
            # Standard Kadane for max subarray
            max_ending = max(arr[i], max_ending + arr[i])
            max_sum = max(max_sum, max_ending)
            
            # Kadane for min subarray
            min_ending = min(arr[i], min_ending + arr[i])
            min_sum = min(min_sum, min_ending)
        
        # If all numbers are negative
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)