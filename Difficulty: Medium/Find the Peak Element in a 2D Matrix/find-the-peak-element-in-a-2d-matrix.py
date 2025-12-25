class Solution:
    def findPeakGrid(self, mat):
        n, m = len(mat), len(mat[0])
        left, right = 0, m - 1

        while left <= right:
            mid = (left + right) // 2

            # find row index of max element in mid column
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right_val = mat[max_row][mid + 1] if mid + 1 < m else float('-inf')

            if mat[max_row][mid] >= left_val and mat[max_row][mid] >= right_val:
                return [max_row, mid]  # peak found
            elif left_val > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]