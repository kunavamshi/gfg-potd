from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        res = []

        for i in range(len(arr)):
            # Remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Start recording results when first window completes
            if i >= k - 1:
                res.append(arr[dq[0]])

        return res