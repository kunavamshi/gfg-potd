class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place elements at correct index
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                # Swap arr[i] with arr[arr[i] - 1]
                correct_index = arr[i] - 1
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
        
        # Step 2: Find the first missing positive
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all values are in place
        return n + 1