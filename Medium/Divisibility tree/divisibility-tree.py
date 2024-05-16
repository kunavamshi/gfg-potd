
from typing import List
from collections import defaultdict


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        counts = [0]*(n+1)
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node,prev,counts,graph):
            size = 1
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                size += dfs(neigh,node,counts,graph)

            counts[node] = size
            return size

        dfs(1,-1,counts,graph)
        ans = 0
        for i in range(2,n+1):
            if counts[i] % 2 == 0:
                ans += 1

        return ans

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

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends