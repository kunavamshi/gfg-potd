class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')

        # Loop over left and right columns
        for left in range(m):
            temp = [0] * n

            for right in range(left, m):
                # Add the current column to each row's sum
                for i in range(n):
                    temp[i] += mat[i][right]

                # Apply Kadane's algorithm on this temp array
                max_sum = max(max_sum, self.kadane(temp))

        return max_sum

    def kadane(self, arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far