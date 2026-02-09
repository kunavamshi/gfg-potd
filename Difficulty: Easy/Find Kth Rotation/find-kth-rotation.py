class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than last element,
            # minimum is in right half
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                # minimum is in left half including mid
                high = mid
        
        return low