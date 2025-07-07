class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            curr = arr[i % n]
            while stack and stack[-1] <= curr:
                stack.pop()
            if i < n:
                res[i] = stack[-1] if stack else -1
            stack.append(curr)
        return res