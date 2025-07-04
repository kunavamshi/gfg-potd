class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict

        freq = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                k -= 1
            freq[arr[right]] += 1

            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1

            result += right - left + 1

        return result