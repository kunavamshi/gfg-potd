class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flips = 0
        curr_flips = 0
        is_flipped = [0] * n   # marks where flips start

        for i in range(n):
            # Remove flip effect that ends at i
            if i >= k:
                curr_flips ^= is_flipped[i - k]

            # If current bit is 0 after considering flips, we must flip here
            if (arr[i] ^ curr_flips) == 0:
                if i + k > n:  # can't flip (out of bounds)
                    return -1
                flips += 1
                curr_flips ^= 1
                is_flipped[i] = 1

        return flips