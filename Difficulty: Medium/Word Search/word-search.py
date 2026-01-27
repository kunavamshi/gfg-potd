class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        L = len(word)

        def dfs(i, j, idx):
            # matched entire word
            if idx == L:
                return True

            # boundary + mismatch check
            if i < 0 or j < 0 or i >= n or j >= m or mat[i][j] != word[idx]:
                return False

            # mark visited
            temp = mat[i][j]
            mat[i][j] = '#'

            # explore 4 directions
            found = (
                dfs(i+1, j, idx+1) or
                dfs(i-1, j, idx+1) or
                dfs(i, j+1, idx+1) or
                dfs(i, j-1, idx+1)
            )

            # backtrack
            mat[i][j] = temp
            return found

        # try starting from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False