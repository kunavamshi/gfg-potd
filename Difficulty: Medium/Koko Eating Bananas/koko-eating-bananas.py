class Solution:
    def kokoEat(self, arr, k):
        left, right = 1, max(arr)
        
        while left < right:
            mid = (left + right) // 2
            
            hours = 0
            for pile in arr:
                hours += (pile + mid - 1) // mid
            
            if hours > k:
                left = mid + 1
            else:
                right = mid
        
        return left