from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        stack = []
        
        # Step 1: Push first half into stack
        for _ in range(n // 2):
            stack.append(q.popleft())
        
        # Step 2: Enqueue stack elements back
        while stack:
            q.append(stack.pop())
        
        # Step 3: Move first half to rear
        for _ in range(n // 2):
            q.append(q.popleft())
        
        # Step 4: Push first half again into stack
        for _ in range(n // 2):
            stack.append(q.popleft())
        
        # Step 5: Interleave
        while stack:
            q.append(stack.pop())
            q.append(q.popleft())
        
        return q