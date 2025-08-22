import bisect

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Define search space
        low = min(row[0] for row in mat)     # smallest element
        high = max(row[-1] for row in mat)   # largest element
        
        desired = (n * m + 1) // 2  # median position
        
        while low < high:
            mid = (low + high) // 2
            
            # Count how many numbers <= mid
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count < desired:
                low = mid + 1
            else:
                high = mid
        
        return low