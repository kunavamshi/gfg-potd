from collections import deque

class Solution:
    def orangesRotting(self, mat):
        if not mat:
            return -1
        
        n, m = len(mat), len(mat[0])
        queue = deque()
        fresh_oranges = 0
        
        # Step 1: Store initial positions of rotten oranges & count fresh ones
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh_oranges += 1
        
        # If no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        time_taken = 0
        
        # Step 2: BFS traversal
        while queue:
            i, j, time = queue.popleft()
            time_taken = max(time_taken, time)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1:
                    mat[ni][nj] = 2  # Rot the fresh orange
                    fresh_oranges -= 1
                    queue.append((ni, nj, time + 1))
        
        # Step 3: If fresh oranges remain, return -1; else return time_taken
        return -1 if fresh_oranges > 0 else time_taken

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends