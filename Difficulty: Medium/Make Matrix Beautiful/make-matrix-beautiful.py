class Solution:
    def balanceSums(self, mat):
        n = len(mat)

        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(n)) for j in range(n)]

        target_sum = max(max(row_sum), max(col_sum))

        operations = 0
        for i in range(n):
            operations += target_sum - row_sum[i]

        return operations