import math

class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in arr)

        low, high = 1, max(arr)
        while low < high:
            mid = (low + high) // 2
            if compute_sum(mid) <= k:
                high = mid
            else:
                low = mid + 1
        return low