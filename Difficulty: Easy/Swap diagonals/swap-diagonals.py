class Solution:
    def swapDiagonal(self, mat):
        n = len(mat)
        for i in range(n):
            mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]
        return mat