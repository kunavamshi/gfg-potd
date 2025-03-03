from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        min_deque, max_deque = deque(), deque()
        left = 0
        max_len, start_idx = 0, 0

        for right in range(len(arr)):
            # Maintain min deque (increasing order)
            while min_deque and arr[min_deque[-1]] > arr[right]:
                min_deque.pop()
            min_deque.append(right)

            # Maintain max deque (decreasing order)
            while max_deque and arr[max_deque[-1]] < arr[right]:
                max_deque.pop()
            max_deque.append(right)

            # Shrink window if condition is violated
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            # Update max subarray info
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start_idx = left

        return arr[start_idx:start_idx + max_len]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends