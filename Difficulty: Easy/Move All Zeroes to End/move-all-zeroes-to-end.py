class Solution:
    def pushZerosToEnd(self, arr):
        pos = 0  # position to place next non-zero
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1