from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)         # Step 1: Frequency map
        res = [-1] * n              # Initialize result
        stack = []                  # Monotonic stack

        for i in range(n - 1, -1, -1):  # Traverse from right to left
            # Maintain stack with elements having higher frequency
            while stack and freq[arr[i]] >= freq[arr[stack[-1]]]:
                stack.pop()

            if stack:
                res[i] = arr[stack[-1]]
            stack.append(i)

        return res