class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        stack = []
        prev = [0] * n
        next_ = [0] * n
        
        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                prev[i] = stack[-1]
            else:
                prev[i] = -1
                
            stack.append(i)
        
        stack.clear()
        
        # Next Less Element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                next_[i] = stack[-1]
            else:
                next_[i] = n
                
            stack.append(i)
        
        result = 0
        
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            result += arr[i] * left * right
        
        return result