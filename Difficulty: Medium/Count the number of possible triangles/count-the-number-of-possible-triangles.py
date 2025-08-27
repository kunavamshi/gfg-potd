class Solution:
    def countTriangles(self, arr):
        n = len(arr)
        arr.sort()
        count = 0
        
        # Fix the largest element one by one
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    # All elements between i and j form valid triangles
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count