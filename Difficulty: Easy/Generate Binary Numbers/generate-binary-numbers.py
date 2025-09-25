from collections import deque

class Solution:
    def generateBinary(self, n):
        result = []
        queue = deque()
        queue.append("1")

        for _ in range(n):
            current = queue.popleft()
            result.append(current)
            queue.append(current + "0")
            queue.append(current + "1")
        
        return result