class Solution:
    def searchInsertK(self, arr, k):
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l + r) // 2
            if arr[m] == k:
                return m
            elif arr[m] < k:
                l = m + 1
            else:
                r = m - 1
        
        return l