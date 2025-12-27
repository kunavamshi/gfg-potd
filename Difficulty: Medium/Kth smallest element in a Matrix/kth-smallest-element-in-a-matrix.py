class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        low, high = mat[0][0], mat[n-1][n-1]

        def count_le(x):
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if mat[i][j] <= x:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            return cnt

        while low < high:
            mid = (low + high) // 2
            if count_le(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low