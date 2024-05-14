
from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        # Directions for moving: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_diff = float('inf')
        
        # Helper function to check if a given move is within bounds
        def is_valid_move(x, y):
            return 0 <= x < rows and 0 <= y < columns
        
        # Helper function to perform Dijkstra's algorithm
        def dijkstra():
            min_effort = [[max_diff] * columns for _ in range(rows)]
            min_effort[0][0] = 0
            pq = [(0, 0, 0)]  # (effort, row, column)
            
            while pq:
                effort, x, y = heapq.heappop(pq)
                
                # If we reached the bottom-right cell, return the minimum effort
                if x == rows - 1 and y == columns - 1:
                    return effort
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid_move(nx, ny):
                        new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                        if new_effort < min_effort[nx][ny]:
                            min_effort[nx][ny] = new_effort
                            heapq.heappush(pq, (new_effort, nx, ny))
        
        return dijkstra()





#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends