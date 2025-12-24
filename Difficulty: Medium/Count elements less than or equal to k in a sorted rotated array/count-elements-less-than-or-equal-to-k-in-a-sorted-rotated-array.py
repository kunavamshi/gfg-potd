class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0

        # 1. Find pivot (index of minimum element)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid
        pivot = lo

        # Helper: count elements <= x in sorted subarray [l, r]
        def count_leq(l, r):
            lo, hi = l, r
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo - l

        # 2. Count in both sorted parts
        count = 0
        if pivot > 0:
            count += count_leq(0, pivot - 1)
        count += count_leq(pivot, n - 1)

        return count
        