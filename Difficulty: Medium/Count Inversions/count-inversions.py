class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr):
        # Helper function to merge two halves and count split inversions.
        def merge_and_count(temp, left, mid, right):
            i, j, k = left, mid + 1, left
            inv_count = 0

            # Merge two sorted subarrays
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    # Inversion found: all elements from arr[i] to arr[mid] are greater than arr[j]
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            # Copy remaining elements from left subarray, if any
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            # Copy remaining elements from right subarray, if any
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy sorted elements back into the original array
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        # Helper function to use merge sort and count inversions
        def merge_sort_and_count(temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                # Count inversions in the left half
                inv_count += merge_sort_and_count(temp, left, mid)

                # Count inversions in the right half
                inv_count += merge_sort_and_count(temp, mid + 1, right)

                # Count split inversions while merging
                inv_count += merge_and_count(temp, left, mid, right)

            return inv_count

        # Create a temporary array and start merge sort
        n = len(arr)
        temp = [0] * n
        return merge_sort_and_count(temp, 0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends