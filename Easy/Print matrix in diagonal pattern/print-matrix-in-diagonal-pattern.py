# Your task is to complete this function

class Solution:
    def matrixDiagonally(self, mat):
        diagonals = [[] for _ in range(len(mat) + len(mat[0]) - 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i + j].append(mat[i][j])

        result = []
        for i, diagonal in enumerate(diagonals):
            if i % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends