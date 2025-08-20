class Solution:
    def searchMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        left, right = 0, n*m - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, m)
            mid_val = mat[row][col]

            if mid_val == x:
                return True

            # Find first and last elements for comparison
            left_val = mat[left // m][left % m]
            right_val = mat[right // m][right % m]

            # Left half is sorted
            if left_val <= mid_val:
                if left_val <= x < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if mid_val < x <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1

        return False