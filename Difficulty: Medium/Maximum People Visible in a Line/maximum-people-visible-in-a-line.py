class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        # Previous greater or equal element index
        prev_ge = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            prev_ge[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Next greater or equal element index
        next_ge = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_ge[i] = stack[-1] if stack else n
            stack.append(i)
        
        ans = 0
        for i in range(n):
            left_visible = i - prev_ge[i] - 1
            right_visible = next_ge[i] - i - 1
            ans = max(ans, left_visible + right_visible + 1)
        
        return ans