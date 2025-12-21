from bisect import bisect_left, bisect_right

class Solution:
    def countXInRange(self, arr, queries):
        res = []
        n = len(arr)

        for l, r, x in queries:
            left = bisect_left(arr, x)
            right = bisect_right(arr, x) - 1

            if left > right:
                res.append(0)
            else:
                lo = max(left, l)
                hi = min(right, r)
                res.append(max(0, hi - lo + 1))

        return res