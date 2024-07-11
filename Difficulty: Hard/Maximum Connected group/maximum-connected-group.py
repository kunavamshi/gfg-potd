from typing import List, Tuple, Dict

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Directions for traversing up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x: int, y: int, idx: int) -> int:
            stack = [(x, y)]
            grid[x][y] = idx
            size = 0
            while stack:
                cx, cy = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = idx
                        stack.append((nx, ny))
            return size
        
        # Step 1: Identify all connected components of 1's
        component_sizes = {}
        component_index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, component_index)
                    component_sizes[component_index] = size
                    component_index += 1
        
        # Step 2: Find the largest group of connected 1's with one change
        max_size = max(component_sizes.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Find adjacent unique component indices
                    adjacent_components = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            adjacent_components.add(grid[ni][nj])
                    
                    # Calculate the size of the new component formed by changing grid[i][j] to 1
                    new_size = 1 + sum(component_sizes[idx] for idx in adjacent_components)
                    max_size = max(max_size, new_size)
        
        return max_size




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

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends