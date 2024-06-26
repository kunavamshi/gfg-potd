class Solution:
    def findCoverage(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        coverage_sum = 0
        
        # Directions are left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Check all four directions
                    for direction in directions:
                        new_i, new_j = i + direction[0], j + direction[1]
                        if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] == 1:
                            coverage_sum += 1
        
        return coverage_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends