class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(arr)):
            # If we include a zero in the window
            if arr[right] == 0:
                zero_count += 1

            # If more than k zeros, shrink from the left
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            # Update max length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len